import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
from dataframe import gdp_df

# ---------------------------------------------DASH APP ---------------------------------------------------------------

app = dash.Dash(__name__, meta_tags=[{'name': 'viewport',
                                      'content': 'width=device-width, '
                                                 'initial-scale=1.0, '
                                                 'maximum-scale=1.2, '
                                                 'minimum-scale=0.5,'}])

app.title = "GDP Graph"

app.layout = html.Div([
    dbc.Row([
        html.H1("GDP Graph", style={'font-family': 'serif', 'font-weight': 'bold', 'color': '#a31aff',
                                    'textAlign': 'center', 'outline-color': '#a31aff',
                                    'outline-style': 'outset'})
    ]),
    html.Br(),
    dbc.Row([
        dcc.Tabs(id="tabs-example-graph", children=[
            dcc.Tab(label='USD', value='usd'),
            dcc.Tab(label='INR', value='inr'),
        ]),
        html.Div(id='tabs-content-example-graph')
    ]),
])


@app.callback(Output('tabs-content-example-graph', 'children'),
              [Input('tabs-example-graph', 'value')])
def gdp_graph(tab):
    if tab == 'usd':
        figure = px.line(gdp_df, x='year', y='gdp', markers=True,
                         labels={'year': 'Year', 'gdp': 'GDP in billion U.S dollars'},
                         category_orders=[list(gdp_df['year'])])

        return [
            html.Div(children=[dcc.Graph(figure=figure)])
        ]

    elif tab == 'inr':
        figure = px.line(gdp_df, x='year', y='gdp_inr', markers=True,
                         labels={'year': 'Year', 'gdp_inr': 'GDP in billion INR'}, )

        return [
            html.Div(children=[dcc.Graph(figure=figure)])
        ]


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
