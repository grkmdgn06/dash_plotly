import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

app.layout = html.Div([
  html.H1('Square Root Slider Graph'),
  dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
  dcc.Slider(
    id='slider-updatemode',
    marks={i: '{}'.format(i) for i in range(20)},
    max=20,
    value=2,
    step=1,
    updatemode='drag',
  ),
])


@app.callback(
  Output('slider-graph', 'figure'),
  [Input('slider-updatemode', 'value')])
def display_value(value):


  x = []
  for i in range(value):
    x.append(i)

  y = []
  for i in range(value):
    y.append(i*i)

  graph = go.Scatter(
    x=x,
    y=y,
    name='Manipulate Graph'
  )
  layout = go.Layout(
    paper_bgcolor='#27293d',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(range=[min(x), max(x)]),
    yaxis=dict(range=[min(y), max(y)]),
    font=dict(color='white'),

  )
  return {'data': [graph], 'layout': layout}



app.layout = html.Div(children=[
    html.H1(children='Merhaba Dash'),
    html.Div(children='''
        DASH: İlk Dash uygulaması.
    '''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Ankara'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'İstanbul'},
            ],
            'layout': {
                'title': 'Dash Veri Görselleştirme'
            }
        }
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)
