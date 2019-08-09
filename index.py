import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import  csv
import pandas as pd
import plotly.graph_objs as go
from flask import render_template


# Step 1. Launch the application
app = dash.Dash()
@app.route("/about")
def about():
    return render_template("index.html")
# Step 2. Import the dataset
df = pd.read_csv('https://api.thingspeak.com/channels/807292/feeds.csv')


# Step 3. Create a plotly figure
trace_1 = go.Scatter(x = df['created_at'], y = df['field1'],
                    name = 'Measure(ppm)',
                     line=dict(width=2,
                               color='rgb(23, 67, 70)'))
layout = go.Layout(title = 'Alcohol by Time Series',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1], layout = layout)

# Step 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot', figure = fig, animate=True)
                      ])

# Step 5. Add callback functions


# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)