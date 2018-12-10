import pandas as pd
from helpers import extract_dataframes, generate_player_list

url = "https://www.pgatour.com/stats/stat."
csv_dir = "../data/PGA_names_raw.csv"

player_list_df = generate_player_list(csv_dir)
# print(player_list_df)
master_df = extract_dataframes(url , player_list_df)
