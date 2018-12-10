import pandas as pd

def extract_dataframes(url , names_df):
    table = []
    for i in range (100,102):
        table_temp_stat = pd.read_html(url + str(i) + ".html")[1]
        # print(table_temp_stat)
        # temp_stat = table_temp_stat.iloc[:,-1]
        # print(temp_stat)
        # print(table_temp)
        # table = table + table_temp
        # self.words = {word: words.index(word) for word in words}
        # self.vecs = vecs
        # print(names_df['name'])
        stat_dict = {name: table_temp_stat['AVG.'] for name in table_temp_stat['PLAYER NAME']}   # O(1) look up speed :) 
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

    return name_df


    # print(name_df_temp)


