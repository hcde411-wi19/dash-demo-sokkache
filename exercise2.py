# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
stats = ["Total	HP",	"Attack",	"Defense",	"Sp. Atk",	"Sp. Def",	"Speed",
                    "Generation"]
bulbasaur = [318,	45,	49,	49,	65,	65,	45,	1]
charmander = [309,	39,	52,	43,	60,	50,	65,	1]
squirtle = [314,	44,	48,	65,	50,	64,	43,	1]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a comparison of stats for the original 3 starter pokemon
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': stats, 'y': bulbasaur, 'type': 'bar', 'name': 'Bulbasaur'},
                {'x': stats, 'y': charmander, 'type': 'bar', 'name': 'Charmander'},
                {'x': stats, 'y': squirtle, 'type': 'bar', 'name': 'Squirtle'},
            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Statistics of The Original 3 Starter Pokemon'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



