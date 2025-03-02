'''
 # @ Create Time: 2024-07-20 09:24:23.495660
'''

import pathlib
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__, title="fed")

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

def load_data(data_file: str) -> pd.DataFrame:
    '''
    Load data from /data directory
    '''
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("data").resolve()
    return pd.read_csv(DATA_PATH.joinpath(data_file))

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0,
                id='button'),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    # replace with your own data source
    df = load_data("2014_apple_stock.csv")

    if n_clicks % 2 == 0:
        x, y = 'AAPL_x', 'AAPL_y'
    else:
        x, y = 'AAPL_y', 'AAPL_x'

    fig = px.line(df, x=x, y=y)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
