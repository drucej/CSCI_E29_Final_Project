import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from helpers import build_master_dataframes, generate_player_list, process_data_frame, csv_viz
from sklearn.manifold import TSNE
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

url = "https://www.pgatour.com/stats/stat."
csv_dir = "../../data/PGA_names_raw.csv"

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
area = 50*money/(max(money)) 
color = strokes_gained

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
               go.Scatter(
                x=data_embedded_csv[:,1],
                y=data_embedded_csv[:,2],
                text=data_embedded_csv[:,0],
                mode='markers',
                opacity=0.7,
                marker={
                    'size':area,
                    'color' : color
                }
                )
            ],
            'layout': go.Layout(
                hovermode = 'closest',
                height= 800
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



py.iplot(data, filename = "add-hover-text v2")