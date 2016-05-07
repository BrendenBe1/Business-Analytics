import plotly.plotly as py
from plotly.graph_objs import *
import createDashboard

graph_URLs = []

# First, make some graphs to embed in the dashboard.
# See more examples: https://plot.ly/python
graph_url1 = py.plot({
    'data': [{'x': [1, 2, 3], 'y': [3, 1, 5]}],
    'layout': {
        'title': 'earnings',
        # graphs embedded in dashboards look best if the margins are tightened up
        'margin': {'l': 30, 'r': 30, 'b': 30, 't': 60}
    }
}, filename='dashboard/earnings') # more about privacy settings: https://plot.ly/python/privacy

graph_url2 = py.plot({
    'data': [{'x': [1, 2, 3], 'y': [3, 40, 5]}],
    'layout': {
        'title': 'growth',
        'margin': {'l': 30, 'r': 30, 'b': 30, 't': 60}
    }
}, filename='dashboard/growth')

graph_url3 = py.plot({
    'data': [{'x': [1, 2, 3], 'y': [10, 61, 2]}],
    'layout': {
        'title': 'performance',
        'margin': {'l': 30, 'r': 30, 'b': 30, 't': 60}
    }
}, filename='dashboard/performance')

graph_list = []
employees = {"Zach Kramer" : 50, "Matt Kramer" : 60, "Spencer Cote" : 13}
for data in employees:
    tmp = Bar(x=data, y=employees[data], name=data)
    graph_list.append(tmp)


# Make graph
graph_data = Data(graph_list)
graph_layout = Layout(barmode='stack')
graph_fig = Figure(data=graph_data, layout=graph_layout)
graph_url4 = py.plot(graph_fig, filename='Employee-Hours')


graph_URLs.append(graph_url1)
graph_URLs.append(graph_url2)
graph_URLs.append(graph_url3)
graph_URLs.append(graph_url4)
date = "4-19"
time_type = "Week"

dashboard = createDashboard.createDashboard(graph_URLs, date, time_type)