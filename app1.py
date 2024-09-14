import numpy as mp
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, html, dcc
from dash.dependencies import Input ,Output
import plotly.express as px
import numpy as np
import pandas as pd

df=pd.read_csv('state_wise_daily.csv')
total= df['Total'].sum()
active= df[df['Status']=='Confirmed'].loc[:,["Total"]].sum()
recovered = df[df['Status']=='Recovered'].loc[:,["Total"]].sum()
death= df[df['Status']=='Deceased'].loc[:,["Total"]].sum()
options=[
 {'label':'All', 'value':'All'},
 {'label':'Hospitalized', 'value':'Hospitalized'},
 {'label':'Recovered','value':'Recovered'},
 {'label':'Deceased','value':'Deceased'}
]
options1=[
 {'label':'All', 'value':'All'},
 {'label':'Mask', 'value':'Mask'},
 {'label':'Sanitizer','value':'Sanitizer'},
 {'label':'Oxygen','value':'Oxygen'}
]
options2=[
 {'label':'Red Zone', 'value':'Red Zone'},
 {'label':'Blue Zone','value':'Blue Zone'},
 {'label':'Green Zone','value':'Green Zone'},
 {'label':'Orange Zone','value':'Orange Zone'}
]
external_stylesheet = [
    {
        'href' : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        'rel':"stylesheet",
        'integrity':"sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" ,
        'crossorigin':"anonymous"
    }
]
app =Dash(__name__,external_stylesheets=external_stylesheet)

app.layout =html.Div([

# main container
    html.H1('COVID19',className='text-white text-center'),

# first row
    html.Div([

    # total cases 

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Case')
                ],className='card-header'),
                html.Div([
                    html.H4(total)
                ],className='card-body')
            ],className='card text-bg-danger text-center')
        ],className='col-md-3'),

    # active casess 
        html.Div([
             html.Div([
                html.Div([
                    html.H3('Active Case')
                ],className='card-header'),
                html.Div([
                    html.H4(active)
                ],className='card-body')
            ],className='card text-bg-primary text-center')
        ],className='col-md-3'),

    # recovered cases
        html.Div([
             html.Div([
                html.Div([
                    html.H3('Recovered Case')
                ],className='card-header'),
                html.Div([
                    html.H4(recovered)
                ],className='card-body')
            ],className='card text-bg-warning text-center')
        ],className='col-md-3'),

    # total deaths
        html.Div([ html.Div([
                html.Div([
                    html.H3('Total Death')
                ],className='card-header'),
                html.Div([
                    html.H4(death)
                ],className='card-body')
            ],className='card text-bg-success text-center')
            ],className='col-md-3')

    ],className='row'),

# graphs
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph', options=options1, value='All'),
                    dcc.Graph(id='graph')
                ],className='card-body')
            ],className='card bg-info')
        ],className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=options2, value='Status',
                    style={"width": "100%"}),
                    dcc.Graph(id='the_graph')
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-6 ')
    ],className='row mt-10'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options, value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12 ')
    ],className='row mt-10')
],className='Container')

@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):
    if type=='All':
        return {'data':[go.Bar(x=df['State'], y=df['Total'])],
        'layout':go.Layout(title= "State Total Count", plot_bgcolor= 'orange')}
    if type == "Hospitalized":
        return {'data':[go.Bar(x=df['State'], y=df['Hospitalized'])],
        'layout':go.Layout(title= "State Total Count", plot_bgcolor='orange')}
    if type == "Recovered":
        return {'data':[go.Bar(x=df['State'], y=df['Recovered'])],
        'layout':go.Layout(title= "State Total Count", plot_bgcolor='orange')}
    if type == "Deceased":
        return {'data':[go.Bar(x=df['State'], y=df['Deceased'])],
        'layout':go.Layout(title= "State Total Count",plot_bgcolor='orange')}
    
@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):
    if type=='All':
        return {'data':[go.Line(x=df['Status'], y=df['Total'])],
        'layout':go.Layout(title= "Commodities Total Count",plot_bgcolor='pink')}
    if type=='Mask':
        return {'data':[go.Line(x=df['Status'], y=df['Mask'])],
        'layout':go.Layout(title= "Commodities Total Count", plot_bgcolor='pink')}
    if type=='Sanitizer':
        return {'data':[go.Line(x=df['Status'], y=df['Sanitizer'])],
        'layout':go.Layout(title= "Commodities Total Count",plot_bgcolor='pink')}
    if type=='Oxygen':
        return {'data':[go.Line(x=df['Status'], y=df['Oxygen'])],
        'layout':go.Layout(title= "Commodities Total Count",plot_bgcolor='pink')}
    
@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
  piechart = px.pie(data_frame=df,names= my_dropdown, hole=0.3)
  return (piechart)
if __name__ == "__main__":
    app.run_server(debug=True, threaded=True)