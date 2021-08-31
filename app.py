# import the flask class
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations as c
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import*
import plotly.graph_objects as go
import plotly
import dash
#import chart_studio.tools as tls
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from flask import Flask, render_template
# instantiate the object class
app=Flask(__name__)

# decorator with url to view the site

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=Flask(__name__)

colors = {
    'background': '#2F4F4F',
    'text': '#7FDBFF'
}

# function always follows a decorator
# create dataframe based on initial data
df = pd.read_csv(r'C:\Users\John\Desktop\Sample Staffer.csv')

# convert data over to list type
list1 = df['Rep'].tolist()
list2 = df['Total Avg Time'].tolist()

# convert list to dictionary
dictionary = {'list1':'list2'}

# from the dictionary create variables to house the keys/values
eid_dictionary = dict.fromkeys(list1,list2)
test_values = (list1)
test_keys = (list2)

# use zip and convert lists back to dictionary
res = dict(zip(test_keys, test_values))

# identify the avg 
avg = sum(test_keys)/len(test_keys)

# identify top EEs for highest weighted job type

numbers = list(res.items())
# sort by highest val rep
numbers.sort(reverse = True)

rep1= []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
#return all combinations within range
for combo in range(6,7):
    # get all unique combinations
    combos = [tuple(sorted(c)) for c in c(numbers[0:20], combo)]
    for x in combos:
        if (x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0] + x[5][0]) >= avg:
            rep1.append(x[0])
            rep2.append(x[1])
            rep3.append(x[2])
            rep4.append(x[3])
            rep5.append(x[4])
            rep6.append(x[5])

# take every list created and turn them into dataframes with x[0] and x[1] 
# serving as the columns/data then merging the dataframes, summing the values
# and having a column that allows to join them
mon1 = pd.DataFrame(data = rep1)
mon1.rename(columns = {0:'Stats'}, inplace = True )
mon1.rename(columns = {1:'EE'}, inplace = True )

mon2 = pd.DataFrame(data = rep2)
mon1['Stats2']= mon2[0]
mon1['EE-2']= mon2[1]


mon3 = pd.DataFrame(data = rep3)
mon1['Stats3']= mon3[0]
mon1['EE-3']= mon3[1]


mon4 = pd.DataFrame(data = rep4)
mon1['Stats4']= mon4[0]
mon1['EE-4']= mon4[1]

mon5 = pd.DataFrame(data = rep5)
mon1['Stats5']= mon5[0]
mon1['EE-5']= mon5[1]


mon6 = pd.DataFrame(data = rep6)
mon1['Stats6']= mon6[0]
mon1['EE-6']= mon6[1]

# # rename all the columns and then concat the dataframes
# after, sum their values, sort by value sum and 
# create a new df that removes the top 20 combos not equal to one another
mon1['Sum Val'] = (mon1['Stats'] + mon1['Stats2'] + mon1['Stats3'] + mon1['Stats4'] + mon1['Stats5'] + mon1['Stats6']) / 6

# sort values by max 'Sum Val'
mon1= mon1.sort_values(by = 'Sum Val', ascending = False)

# pass the values back to a list type
dict1 = mon1.head(1).to_records()
m1 = dict1[0][1],dict1[0][2]
m2 = dict1[0][3],dict1[0][4]
m3 = dict1[0][5],dict1[0][6]
m4 = dict1[0][7],dict1[0][8]
m5 = dict1[0][9],dict1[0][10]
m6 = dict1[0][11],dict1[0][12]

# remove the top EEs grouped from the original data set
numbers.remove(m1)
numbers.remove(m2)
numbers.remove(m3)
numbers.remove(m4)
numbers.remove(m5)
numbers.remove(m6)

# repeat process for EEs remaining


rep1 = []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
#return all combinations within range
for combo in range(6,7):
    # get all unique combinations
    combos = [tuple(sorted(c)) for c in c(numbers[0:20], combo)]
    for x in combos:
        if (x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0] + x[5][0]) >= avg:
            rep1.append(x[0])
            rep2.append(x[1])
            rep3.append(x[2])
            rep4.append(x[3])
            rep5.append(x[4])
            rep6.append(x[5])

tues1 = pd.DataFrame(data = rep1)
tues1.rename(columns = {0:'Stats'}, inplace = True )
tues1.rename(columns = {1:'EE'}, inplace = True )

tues2 = pd.DataFrame(data = rep2)
tues1['Stats2']= tues2[0]
tues1['EE-2']= tues2[1]


tues3 = pd.DataFrame(data = rep3)
tues1['Stats3']= tues3[0]
tues1['EE-3']= tues3[1]


tues4 = pd.DataFrame(data = rep4)
tues1['Stats4']= tues4[0]
tues1['EE-4']= tues4[1]


tues5 = pd.DataFrame(data = rep5)
tues1['Stats5']= tues5[0]
tues1['EE-5']= tues5[1]


tues6 = pd.DataFrame(data = rep6)
tues1['Stats6']= tues6[0]
tues1['EE-6']= tues6[1]

tues1['Sum Val'] = (tues1['Stats'] + tues1['Stats2'] + tues1['Stats3'] + tues1['Stats4'] + tues1['Stats5'] + tues1['Stats6']) / 6
tues1= tues1.sort_values(by = 'Sum Val', ascending = False)

dict2 = tues1.head(1).to_records()

t1 = dict2[0][1],dict2[0][2]
t2 = dict2[0][3],dict2[0][4]
t3 = dict2[0][5],dict2[0][6]
t4 = dict2[0][7],dict2[0][8]
t5 = dict2[0][9],dict2[0][10]
t6 = dict2[0][11],dict2[0][12]

numbers.remove(t1)
numbers.remove(t2)
numbers.remove(t3)
numbers.remove(t4)
numbers.remove(t5)
numbers.remove(t6)


#numbers = list(res.items())

rep1= []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
#return all combinations within range
for combo in range(6,7):
    # get all unique combinations
    combos = [tuple(sorted(c)) for c in c(numbers[0:20], combo)]
    for x in combos:
        if (x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0] + x[5][0]) >= avg:
            rep1.append(x[0])
            rep2.append(x[1])
            rep3.append(x[2])
            rep4.append(x[3])
            rep5.append(x[4])
            rep6.append(x[5])

wed1 = pd.DataFrame(data = rep1)
wed1.rename(columns = {0:'Stats'}, inplace = True )
wed1.rename(columns = {1:'EE'}, inplace = True )

wed2 = pd.DataFrame(data = rep2)
wed1['Stats2']= wed2[0]
wed1['EE-2']= wed2[1]


wed3 = pd.DataFrame(data = rep3)
wed1['Stats3']= wed3[0]
wed1['EE-3']= wed3[1]


wed4 = pd.DataFrame(data = rep4)
wed1['Stats4']= wed4[0]
wed1['EE-4']= wed4[1]


wed5 = pd.DataFrame(data = rep5)
wed1['Stats5']= wed5[0]
wed1['EE-5']= wed5[1]


wed6 = pd.DataFrame(data = rep6)
wed1['Stats6']= wed6[0]
wed1['EE-6']= wed6[1]

wed1['Sum Val'] = (wed1['Stats'] + wed1['Stats2'] + wed1['Stats3'] + wed1['Stats4'] + wed1['Stats5'] + wed1['Stats6']) / 6
wed1= wed1.sort_values(by = 'Sum Val', ascending = False)

dict3 = wed1.head(1).to_records()

w1 = dict3[0][1],dict3[0][2]
w2 = dict3[0][3],dict3[0][4]
w3 = dict3[0][5],dict3[0][6]
w4 = dict3[0][7],dict3[0][8]
w5 = dict3[0][9],dict3[0][10]
w6 = dict3[0][11],dict3[0][12]

numbers.remove(w1)
numbers.remove(w2)
numbers.remove(w3)
numbers.remove(w4)
numbers.remove(w5)
numbers.remove(w6)

#numbers = list(res.items())

rep1= []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
#return all combinations within range
for combo in range(6,7):
    # get all unique combinations
    combos = [tuple(sorted(c)) for c in c(numbers[0:20], combo)]
    for x in combos:
        if (x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0] + x[5][0]) >= avg:
            rep1.append(x[0])
            rep2.append(x[1])
            rep3.append(x[2])
            rep4.append(x[3])
            rep5.append(x[4])
            rep6.append(x[5])

thurs1 = pd.DataFrame(data = rep1)
thurs1.rename(columns = {0:'Stats'}, inplace = True )
thurs1.rename(columns = {1:'EE'}, inplace = True )

thurs2 = pd.DataFrame(data = rep2)
thurs1['Stats2']= thurs2[0]
thurs1['EE-2']= thurs2[1]


thurs3 = pd.DataFrame(data = rep3)
thurs1['Stats3']= thurs3[0]
thurs1['EE-3']= thurs3[1]


thurs4 = pd.DataFrame(data = rep4)
thurs1['Stats4']= thurs4[0]
thurs1['EE-4']= thurs4[1]


thurs5 = pd.DataFrame(data = rep5)
thurs1['Stats5']= thurs5[0]
thurs1['EE-5']= thurs5[1]


thurs6 = pd.DataFrame(data = rep6)
thurs1['Stats6']= thurs6[0]
thurs1['EE-6']= thurs6[1]
thurs1['Sum Val'] = (thurs1['Stats'] + thurs1['Stats2'] + thurs1['Stats3'] + thurs1['Stats4'] + thurs1['Stats5'] + thurs1['Stats6']) / 6
thurs1= thurs1.sort_values(by = 'Sum Val', ascending = False)

dict4 = thurs1.head(1).to_records()

th1 = dict4[0][1],dict4[0][2]
th2 = dict4[0][3],dict4[0][4]
th3 = dict4[0][5],dict4[0][6]
th4 = dict4[0][7],dict4[0][8]
th5 = dict4[0][9],dict4[0][10]
th6 = dict4[0][11],dict4[0][12]

numbers.remove(th1)
numbers.remove(th2)
numbers.remove(th3)
numbers.remove(th4)
numbers.remove(th5)
numbers.remove(th6)


#numbers = list(res.items())

rep1= []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
#return all combinations within range
for combo in range(6,7):
    # get all unique combinations
    combos = [tuple(sorted(c)) for c in c(numbers[0:20], combo)]
    for x in combos:
        if (x[0][0] + x[1][0] + x[2][0] + x[3][0] + x[4][0] + x[5][0]) >= avg:
            rep1.append(x[0])
            rep2.append(x[1])
            rep3.append(x[2])
            rep4.append(x[3])
            rep5.append(x[4])
            rep6.append(x[5])

fri1 = pd.DataFrame(data = rep1)
fri1.rename(columns = {0:'Stats'}, inplace = True )
fri1.rename(columns = {1:'EE'}, inplace = True )

fri2 = pd.DataFrame(data = rep2)
fri1['Stats2']= fri2[0]
fri1['EE-2']= fri2[1]


fri3 = pd.DataFrame(data = rep3)
fri1['Stats3']= fri3[0]
fri1['EE-3']= fri3[1]


fri4 = pd.DataFrame(data = rep4)
fri1['Stats4']= fri4[0]
fri1['EE-4']= fri4[1]


fri5 = pd.DataFrame(data = rep5)
fri1['Stats5']= fri5[0]
fri1['EE-5']= fri5[1]


fri6 = pd.DataFrame(data = rep6)
fri1['Stats6']= fri6[0]
fri1['EE-6']= fri6[1]

fri1['Sum Val'] = (fri1['Stats'] + fri1['Stats2'] + fri1['Stats3'] + fri1['Stats4'] + fri1['Stats5'] + fri1['Stats6']) / 6
fri1= fri1.sort_values(by = 'Sum Val', ascending = False)

dict5 = fri1.head(1).to_records()

f1 = dict5[0][1],dict5[0][2]
f2 = dict5[0][3],dict5[0][4]
f3 = dict5[0][5],dict5[0][6]
f4 = dict5[0][7],dict5[0][8]
f5 = dict5[0][9],dict5[0][10]
f6 = dict5[0][11],dict5[0][12]

numbers.remove(f1)
numbers.remove(f2)
numbers.remove(f3)
numbers.remove(f4)
numbers.remove(f5)
numbers.remove(f6)

# Calculate change in percentage for achieved sustainment for each df created/their day of the week

c = (mon1['Sum Val'].max() - avg) / avg
c2 = (tues1['Sum Val'].max() - avg) / avg
c3 = (wed1['Sum Val'].max() - avg) / avg
c4 = (thurs1['Sum Val'].max() - avg) / avg
c5 = (fri1['Sum Val'].max() - avg) / avg

# import sample productivity data
knry = pd.read_csv(r'C:\Users\John\Desktop\KNRY\WKDY avg.csv')
#:\Users\John\Desktop\KNRY

# The data below represents the data that needs to be plotted to a grouped chart and then converted to an html file to call it from a webapp

jobs = ['Line Count', 'Piece Count']
jobs2 = ['F Zone Batches', 'F Zone','J Zone']

fig = go.Figure(data = [go.Bar(name = 'Test1', x = jobs, y = [knry['Monday'][0], knry['Monday'][1]]),
                        go.Bar(name = 'Test2', x = jobs,y = [(knry['Monday'][0] * c + knry['Monday'][0]),(knry['Monday'][1] * c2 + knry['Monday'][1])])])


fig2 = go.Figure(data = [go.Bar(name = 'Test3',x = jobs2, y = [knry['Monday'][2],knry['Monday'][3],knry['Monday'][4]]),
                                 go.Bar(name = 'Test4', x = jobs2, y = [(knry['Monday'][2] * c3 + knry['Monday'][2]),
                                                                (knry['Monday'][3] * c4 + knry['Monday'][3]),(knry['Monday'][4] * c5 + knry['Monday'][4])])])


fig.update_layout(barmode='group')
plotly.offline.plot(fig, filename='Line Count.html',auto_open=False)

fig2.update_layout(barmode='group')
plotly.offline.plot(fig, filename='Piece Count.html',auto_open=False)

fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'],
font_color=colors['text'], barmode='group')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
@app.route('/')

@app.route('/Line/')
def Line():
    return render_template("Line.html")

@app.route('/Piece/')
def Piece():
    return render_template("Piece.html")



if __name__ == "__main__":
    app.run(debug = True)