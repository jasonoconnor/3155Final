import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('vgsales.csv')

app = dash.Dash()

# Global
app.layout = html.Div(children=[
    html.H1(children='Video Game Sale Analytical Tool For Developers In Need',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web Dashboard for Video Game Sales Data Visualization', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Global Sales', style={'color': '#df1e56'}),
    html.Div('This bar chart presents information on Global Sales by Genre or Platform'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a query', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select',
        options=[
            {'label': 'Genre', 'value': 'Genre'},
            {'label': 'Platform', 'value': 'Platform'},
        ],
        value='Genre'
    ),
# North America
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('North American Sales', style={'color': '#df1e56'}),
    html.Div('This bar chart presents information on Video Game Sales by Genre or Platform in North America'),
    dcc.Graph(id='graph2'),
    html.Div('Please select a query', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select2',
        options=[
            {'label': 'Genre', 'value': 'Genre'},
            {'label': 'Platform', 'value': 'Platform'},
        ],
        value='Genre'
    ),
# Europe
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('European Sales', style={'color': '#df1e56'}),
    html.Div('This bar chart presents information on Video Game Sales by Genre or Platform in Europe'),
    dcc.Graph(id='graph3'),
    html.Div('Please select a query', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select3',
        options=[
            {'label': 'Genre', 'value': 'Genre'},
            {'label': 'Platform', 'value': 'Platform'},
        ],
        value='Genre'
    ),
# Japan
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Japanese Sales', style={'color': '#df1e56'}),
    html.Div('This bar chart presents information on Video Game Sales by Genre or Platform in Japan'),
    dcc.Graph(id='graph4'),
    html.Div('Please select a query', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select4',
        options=[
            {'label': 'Genre', 'value': 'Genre'},
            {'label': 'Platform', 'value': 'Platform'},
        ],
        value='Genre'
    )
    ])
# Global
@app.callback(Output('graph1', 'figure'),
              [Input('select', 'value')])
def update_figure(selection):
    new_df = df1.groupby([selection])['Global_Sales'].sum().reset_index()
    new_df = new_df.sort_values(by=['Global_Sales'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df[selection], y=new_df['Global_Sales'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Global Game Sales Sorted By '+selection,
                                                                   xaxis={'title': selection},
                                                                   yaxis={'title': 'Units Sold (in millions)'})}
# North America
@app.callback(Output('graph2', 'figure'),
              [Input('select2', 'value')])
def update_figure(selection):
    new_df = df1.groupby([selection])['NA_Sales'].sum().reset_index()
    new_df = new_df.sort_values(by=['NA_Sales'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df[selection], y=new_df['NA_Sales'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='North American Game Sales Sorted By '+selection,
                                                                   xaxis={'title': selection},
                                                                   yaxis={'title': 'Units Sold (in millions)'})}
# Europe
@app.callback(Output('graph3', 'figure'),
              [Input('select3', 'value')])
def update_figure(selection):
    new_df = df1.groupby([selection])['EU_Sales'].sum().reset_index()
    new_df = new_df.sort_values(by=['EU_Sales'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df[selection], y=new_df['EU_Sales'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='European Game Sales Sorted By '+selection,
                                                                   xaxis={'title': selection},
                                                                   yaxis={'title': 'Units Sold (in millions)'})}
# Japan
@app.callback(Output('graph4', 'figure'),
              [Input('select4', 'value')])
def update_figure(selection):
    new_df = df1.groupby([selection])['JP_Sales'].sum().reset_index()
    new_df = new_df.sort_values(by=['JP_Sales'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df[selection], y=new_df['JP_Sales'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Japanese Game Sales Sorted By '+selection,
                                                                   xaxis={'title': selection},
                                                                   yaxis={'title': 'Units Sold (in millions)'})}



if __name__ == '__main__':
    app.run_server()
