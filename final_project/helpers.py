import pandas as pd

def build_master_dataframes(url , names_df):
    table = []
    stats = {'dist' : ['https://www.pgatour.com/stats/stat.101.html' , 'AVG.'], 
            'driving_accuracy' : ['https://www.pgatour.com/stats/stat.102.html', '%'], 
             'iron_less_125' : ['https://www.pgatour.com/stats/stat.330.html', '%'], 
             'iron_more_200' : ['https://www.pgatour.com/stats/stat.326.html' , '%'], 
             'scrambling' : ['https://www.pgatour.com/stats/stat.130.html' , '%'] , 
             'one_putting' : ['https://www.pgatour.com/stats/stat.413.html' , '%']}

    master_df = pd.DataFrame(index = names_df['name'])
    for stat in stats.keys():
        table_temp_stat = pd.read_html(stats[stat][0])
        table_temp_stat = table_temp_stat[1]

        # master_df.set_index(names_df['name'])
        # print(table_temp_stat)
        # print(table_temp_stat)
        # temp_stat = table_temp_stat.iloc[:,-1]
        # print(table_temp_stat)
        # print(table_temp)
        # table = table + table_temp
        # self.words = {word: words.index(word) for word in words}
        # self.vecs = vecs
        # print(names_df['name'])
        # name = 'Bryson DeChambeau'
        # print(table_temp_stat.loc[table_temp_stat['PLAYER NAME'] ==name, 'AVG'].iloc[0])
        # stat_dict = {name: table_temp_stat.loc[table_temp_stat['PLAYER NAME'] ==name, 'AVG'] for name in table_temp_stat['PLAYER NAME']}   # O(1) look up speed :) 
        stat_dict = {name : table_temp_stat.loc[table_temp_stat['PLAYER NAME'] ==name, stats[stat][1]].iloc[0] for name in table_temp_stat['PLAYER NAME']}   # O(1) look up speed :)  
        # print(names_df)

        # print(master_df)
        # print(table_temp_stat['AVG'])
        # names_df['stat'] = float('nan')
        count = 0
        for name in table_temp_stat['PLAYER NAME']:
            count+=1
            if name in master_df.index.values.tolist():
                master_df.at[name,stat] = stat_dict[name]
            else:
            	pass
            # print(master_df)

        master_df = master_df.dropna(axis=0)
        print(master_df)
        # master_df['stat'] =  [stat_dict(name) for name in table_temp_stat['PLAYER NAME']]


        # name_dict = {name:  for stat in temp_stat['stat']}
        # print(name_dict.keys())


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


    # print(name_df_temp)


