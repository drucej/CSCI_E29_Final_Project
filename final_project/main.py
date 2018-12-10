import pandas as pd
from helpers import extract_dataframes, generate_player_list

url = "https://www.pgatour.com/stats/stat."

master_df = extract_dataframes(url)