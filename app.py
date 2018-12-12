import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from final_project.helpers import build_master_dataframes, generate_player_list, process_data_frame, csv_viz
from sklearn.manifold import TSNE
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

url = "https://www.pgatour.com/stats/stat."
csv_dir = "data/PGA_names_raw.csv"
### Get data for tSNE Embedding  ####
# Get current list of PGA players
player_list_df = generate_player_list(csv_dir)

# Get current PGA player statistics
master_df = build_master_dataframes(url , player_list_df)

# Convert data frame to numpy arrays,
data, money, strokes_gained = process_data_frame(master_df)

# Perform tSNE embedding
data_embedded = TSNE(n_components=2 , perplexity = 5.0).fit_transform(data)

# Reshape data and save as appriate csv for visualization
data_embedded_csv = csv_viz(data_embedded , master_df)


### Plot data
area = 75*money/(max(money)) 
color = strokes_gained

app.layout = html.Div(children=[
    html.H1(children='PGA Tour Unsupervised Data Exploration '),

    html.Div(children='''
        Examining player clustering of players via a tSNE embedding.
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