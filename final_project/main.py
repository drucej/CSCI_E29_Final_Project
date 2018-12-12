import pandas as pd
from helpers import build_master_dataframes, generate_player_list, process_data_frame, csv_viz
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.pgatour.com/stats/stat."
csv_dir = "../data/PGA_names_raw.csv"

player_list_df = generate_player_list(csv_dir)
# print(player_list_df)
master_df = build_master_dataframes(url , player_list_df)

# have data frame, do a tSNE!
# convert to numpy arrays,
data, money, strokes_gained = process_data_frame(master_df)
# print(data)
# pre-process data

# perform tSNE embedding
data_embedded = TSNE(n_components=2 , perplexity = 5.0).fit_transform(data)

# save data as appriate csv for visualization
data_embedded_csv = csv_viz(data_embedded , master_df)


# show data
# area = (30 * np.random.rand(data_embedded.shape[0]))**2  # 0 to 15 point radii
area = 200*money/(max(money)) 
color = strokes_gained
plt.scatter(data_embedded[:,0] , data_embedded[:,1] , s = area , c= color, alpha = 0.5)
plt.show()