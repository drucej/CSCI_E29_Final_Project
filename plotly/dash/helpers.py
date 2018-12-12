import pandas as pd
import numpy as np
import csv

def build_master_dataframes(url , names_df):
    table = []
    stats = {'dist' : ['https://www.pgatour.com/stats/stat.101.html' , 'AVG.'], 
            'driving_accuracy' : ['https://www.pgatour.com/stats/stat.102.html', '%'], 
             'iron_less_125' : ['https://www.pgatour.com/stats/stat.330.html', '%'], 
             'iron_more_200' : ['https://www.pgatour.com/stats/stat.326.html' , '%'], 
             'scrambling' : ['https://www.pgatour.com/stats/stat.130.html' , '%'] , 
             'one_putting' : ['https://www.pgatour.com/stats/stat.413.html' , '%'] , 
             'strokes_gained' : ['https://www.pgatour.com/stats/stat.02675.html' , 'AVERAGE'] , 
             'total_money' : ['https://www.pgatour.com/stats/stat.194.html' , 'MONEY']}

    master_df = pd.DataFrame(index = names_df['name'])
    for stat in stats.keys():
        print(stat)
        table_temp_stat = pd.read_html(stats[stat][0])
        table_temp_stat = table_temp_stat[1]

        if stat == 'total_money':
            # table_temp_stat['MONEY'] = table_temp_stat['MONEY'].replace({'\$,':''}, regex = True).astype(float)
            table_temp_stat['MONEY'] = table_temp_stat['MONEY'].replace('[\$,]', '', regex=True).astype(float)

            # table_temp_stat['MONEY'] = table_temp_stat['MONEY'].replace({'\,':''}, regex = True)

        stat_dict ={}
        for name in table_temp_stat['PLAYER NAME']:
            if name in names_df['name'].tolist():
                stat_dict[name] = table_temp_stat.loc[table_temp_stat['PLAYER NAME'] ==name, stats[stat][1]].iloc[0]
            else:
                stat_dict[name] = 'NaN'
        
        
        count = 0
        for name in table_temp_stat['PLAYER NAME']:
            count+=1
            if name in master_df.index.values.tolist():
                master_df.at[name,stat] = stat_dict[name]
            else:
            	pass
            # print(master_df)

        master_df = master_df.dropna(axis=0)
        # print(master_df)
        # master_df['stat'] =  [stat_dict(name) for name in table_temp_stat['PLAYER NAME']]


    return master_df


def generate_player_list(csv_dir):
	# load player list csv as pandas data frame
    name_df_temp = pd.read_csv(csv_dir , names = ('data','name'))   

    # convert names from (last, first) to (first last) to match stats files
    name_df_temp[['last_name','first_name']] = name_df_temp['name'].loc[name_df_temp['name'].str.split().str.len() == 2].str.split(expand=True)
    name_df_temp['last_name'] = name_df_temp['last_name'].str.replace(',', '')

    # remove NaNs
    name_df_temp = name_df_temp.dropna(axis=0)

    # combine into one column
    name_df_temp = name_df_temp['first_name'].map(str) + ' ' + name_df_temp['last_name']  # converts to series? 
    name_df = name_df_temp.to_frame()
    name_df.columns = ['name']
    # print(name_df.to_string())
    # name_df_temp = name_df_temp.drop_duplicates(keep = False, inplace = True)

    return name_df

def process_data_frame(df):

    data = df.values

    money = data[:,-1]
    SG = data[:,-2]
    data = data[:,:-2]
    mean_data = data.mean(axis=0) 
    dev_data = data.std(axis=0)
    normed = (data - mean_data)/dev_data

    return normed , money, SG
    # print(name_df_temp)

def csv_viz(data , master_df):
    names = master_df.index.values
    print(names.shape)
    print(data.shape)
    names = np.expand_dims(names, axis = 1)
    trans_data = np.concatenate([names, data] , axis=1)

	# np.savetxt("pga_data.csv", trans_data, delimiter=",")
    with open('pga_data.csv', 'w') as f:
        csv.writer(f).writerows(trans_data)

    return trans_data


