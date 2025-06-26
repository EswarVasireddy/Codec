import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv")

app = dash.Dash(__name__)

fig = px.scatter(df, x="total_cases", y="total_deaths", size="population",
                 color="continent", hover_name="location", log_x=True)

app.layout = html.Div([
    html.H1("COVID-19 Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)