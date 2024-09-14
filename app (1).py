import numpy as np
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dash
from dash.dependencies import Input, Output

external_stylesheet = [
    {
        'href' : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        'rel':"stylesheet",
        'integrity':"sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" ,
        'crossorigin':"anonymous"
    }
]

covid_df = pd.read_csv("state_wise_daily.csv")
Total_Cases = covid_df.shape[0]
Active_Cases = covid_df[covid_df['Status']=="Confirmed"].shape[0]
Recovered_Cases = covid_df[covid_df['Status']=="Recovered"].shape[0]
Total_Deaths = covid_df[covid_df['Status']=="Deceased"].shape[0]

option1 = [
    {'label':'All','value':'All'},
    {'label':'mask','value':'mask'},
    {'label':'sanitizer','value':'sanitizer'},
    {'label':'oxygen','value':'oxygen'}

]

option2 = [
    {'label':'Red Zone','value':'Red Zone'},
    {'label':'Blue Zone','value':'Blue Zone'},
    {'label':'Green Zone','value':'Green Zone'},
    {'label':'Orange Zone','value':'Orange Zone'}

]

option3 = [
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]

app = dash.Dash(__name__,external_stylesheets=external_stylesheet)

app.layout= html.Div([
    html.H1("Corona Virus Analysis", style={"color":"#fff", "text-align":"center"}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases"),
                    html.H4(Total_Cases)
                ], className="card-body")
            ], className="card bg-success")
        ], className="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases"),
                    html.H3(Active_Cases)
                ], className="card-body")
            ], className="card bg-info")
        ], className="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", ),
                    html.H3(Recovered_Cases, )
                ], className="card-body")
            ], className="card bg-warning")
        ], className="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths"),
                    html.H3(Total_Deaths)
                ], className="card-body")
            ], className="card bg-danger")
        ], className="col-md-3")
    ], className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph', options=option1, value="All"),
                    dcc.Graph(id="Line_graph")
                ], className="card-body")
            ], className="card")
        ], className="col-md-6"),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=option2, value='Status'),
                    dcc.Graph(id='pie_graph')
                ], className="card-body")
            ], className="card")
        ], className="col-md-6")
    ], className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id="picker", options=option3, value="All"),
                    dcc.Graph(id="bar_graph")
                ], className="card-body")
            ], className="card")
        ], className="col-md-12")
    ], className="row")
], className="Container text-white ")   # apne container ko class text-white nhi diya tha or baki to mare me chal raha hai


@app.callback(Output("Line_graph","figure"),[Input('plot-graph','value')])
def generate_graph(type):
    if type=="All":
        return {"data":[go.Line(x=covid_df['Status'],y=covid_df['Total'])],
                        'layout':go.Layout(title="Total Count of Commodities",plot_bgcolor = "pink")}

    if type=="mask":
        return {"data":[go.Line(x=covid_df['Status'],y=covid_df['mask'])],
                        'layout':go.Layout(title="Total Count of Commodities",plot_bgcolor = "pink")}

    if type=="sanitizer":
        return {"data":[go.Line(x=covid_df['Status'],y=covid_df['sanitizer'])],
                        'layout':go.Layout(title="Total Count of Commodities",plot_bgcolor = "pink")}

    if type=="oxygen":
        return {"data":[go.Line(x=covid_df['Status'],y=covid_df['sanitizer'])],
                        'layout':go.Layout(title="Total Count of Commodities",plot_bgcolor = "pink")}


@app.callback(Output("pie_graph","figure"), [Input("my_dropdown","value")])
def generate_graph(my_dropdown):
        piechart=px.pie(data_frame=covid_df,names=my_dropdown, hole=0.3)
        return piechart

@app.callback(Output("bar_graph","figure"), [Input("picker","value")])
def generate_graph(type):
    if type=="All":
        return {"data":[go.Bar(x=covid_df['State'],y=covid_df['Total'])],
                        'layout':go.Layout(title="Total State count",plot_bgcolor="orange")}

    if type=="Hospitalized":
        return {"data":[go.Bar(x=covid_df['state'],y=covid_df['Hospitalized'])],
                        'layout':go.Layout(title="Total State count",plot_bgcolor="orange")}

    if type=="Recovered":
        return {"data":[go.Bar(x=covid_df['state'],y=covid_df['Recovered'])],
                        'layout':go.Layout(title="Total State count",plot_bgcolor="orange")}

    if type=="Deceased":
        return {"data":[go.Bar(x=covid_df['State'],y=covid_df['Deceased'])],
                        'layout':go.Layout(title="Total State count",plot_bgcolor="orange")}



if __name__=="__main__":
    app.run_server(debug=True)