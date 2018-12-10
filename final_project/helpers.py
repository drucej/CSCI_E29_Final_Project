import pandas as pd

def extract_dataframes(url):
    table = []
    for i in range (100,102):
        table_temp = pd.read_html(url + str(i) + ".html")
        print(table_temp)
        table = table + table_temp

def generate_player_list(csv):
	df = pd.read_csv(csv)

print(df)


