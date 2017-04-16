# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:27:52 2017

@author: Shashwat Pathak
"""

#==============================================================================
# Chapter 1: Import Modules
#==============================================================================
#Document Object
from bokeh.io import curdoc

#Figure object
from bokeh.plotting import figure

#For defining dataset
from bokeh.models import ColumnDataSource

#For defining Layout
from bokeh.layouts import column, row, gridplot, widgetbox

#For Tools
from bokeh.models import HoverTool, TapTool, Slider
from bokeh.models.widgets import Button, Select, DataTable, TableColumn, Tabs, Panel

#For adding Javascript
from bokeh.models import CustomJS

#For Dataframes
import pandas as po

#==============================================================================
# Chapter 2: Setting up Data
#==============================================================================
#Input Data
ip_data = po.DataFrame({'x' : [1, 2, 3, 4, 5],
    'y0' : [1, 2, 3, 4, 5],
    'y1' : [3, 7, 8, 5, 1],
    'y2' : [1, 1, 2, 2, 3],
    'y3' : [4, 4, 4, 4, 4],
    'color' : ['navy'] * 5,
    'desc' : ['A', 'B', 'C', 'D', 'E']})

#Converting to ColumnDataSource
data = ColumnDataSource(data=ip_data)

#==============================================================================
# Chapter 3: Customizing Tools
#==============================================================================
#==============================================================================
# Chapter 3a: JS Callbacks
#==============================================================================
#Tap Tool
tap_callback = CustomJS(code="alert('hello world')")

#Slider Tool
slider_callback = CustomJS(args=dict(source=data), code="""
    var data = source.get('data');
    var f = cb_obj.get('value')
    x = data['x']
    y = data['y0']
    for (i = 0; i < x.length; i++) {
        y[i] = Math.pow(x[i], f)
    }
    source.trigger('change');
""")

#Selection Tool
data.callback = CustomJS(args=dict(source=data), code="""
    var inds = source.get('selected')['1d'].indices;
    var d = source.get('data');
    var y3 = 0
    
    if (inds.length == 0) { return; }
    
    for (i = 0; i < d['color'].length; i++) {
        d['color'][i] = "navy"
    }
    for (i = 0; i < inds.length; i++) {
        d['color'][inds[i]] = "lime"
        y3 += d['y2'][inds[i]]
    }
    
    y3 /= inds.length
    source.get('data')['y3'] = [y3, y3, y3, y3, y3]
    
    source.trigger('change');
""")

#Hover Tool 0
hover0 = HoverTool(
        tooltips=[
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]
    )

#Hover Tool 1
hover1 = HoverTool(
        tooltips=[
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]
    )

#Hover Tool 2
hover2 = HoverTool(
        tooltips=[
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]
    )

#Hover Tool 3
hover3 = HoverTool(
        tooltips=[
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]
    )

#Update DataTable
def update_summary():
    output.columns = [TableColumn(field = input_text.value, title = input_text.value)]
    output.source = ColumnDataSource(po.DataFrame(ip_data.describe()[input_text.value], columns = [input_text.value]))

#==============================================================================
# Chapter 3b: Widget Definitions
#==============================================================================
#Tap Tool
tap = TapTool(callback=tap_callback)

#Slider Tool
slider = Slider(start=0.1, end=4, value=1, step=.1, title="power", callback=slider_callback)

#Button Tool
button = Button(label="Get Summary Stats")
#Select Tool
input_text = Select(title = "Field Select:", value = 'x', options = ip_data.columns.values.tolist())
#Display Table
columns = [TableColumn(field = input_text.value, title = input_text.value)]
output = DataTable(source = ColumnDataSource(po.DataFrame(ip_data.describe()[input_text.value], columns = [input_text.value])), columns = columns, width = 250, height = 250)
#Action Update
button.on_click(update_summary)

#==============================================================================
# Chapter 2: Drawing Glyphs
#==============================================================================
# Universal chart options
plot_options0 = dict(width=250, plot_height=250, tools=[ 'pan', 'wheel_zoom', 'box_select', 'lasso_select', 'help', hover0])
plot_options1 = dict(width=250, plot_height=250, tools=[ 'pan', 'wheel_zoom', 'box_select', 'lasso_select', 'help', tap, hover1])
plot_options2 = dict(width=250, plot_height=250, tools=[ 'pan', 'wheel_zoom', 'box_select', 'lasso_select', 'help', hover2])
plot_options3 = dict(width=250, plot_height=250, tools=[ 'pan', 'wheel_zoom', 'box_select', 'lasso_select', 'help', hover3])

# create a new plot with default tools, using figure
p0 = figure(title="Cool Title y0", **plot_options0)
p1 = figure(title="Cool Title y1", x_range= p0.x_range, \
#            y_range= p0.y_range, \
            **plot_options1)
p2 = figure(title="Cool Title y2", x_range= p0.x_range, \
#            y_range= p0.y_range, \
            **plot_options2)
p3 = figure(title="Cool Title y3", x_range= p0.x_range, \
#            y_range= p0.y_range, \
            **plot_options3)

# Plotting curves
p0.line('x', 'y0', color="orange", line_width = 2, source = data)
p1.circle('x', 'y1', size = 10, line_color = 'black', fill_color="firebrick", alpha=0.6, source = data)
p2.square('x', 'y2', size = 10, line_color = 'black', fill_color="color", alpha=0.6, source = data)
p3.line('x', 'y3', line_width = 2, color="olive", alpha=0.6, source = data)

#==============================================================================
# Chapter 3: Plotting in a Grid
#==============================================================================
# put all the plots in a gridplot
p_univariate = gridplot([[p0, p1], [p2, p3]], toolbar_location='below')
#controls
controls = widgetbox(children = [slider, input_text, button, output], sizing_mode = 'scale_both')

#==============================================================================
# Chapter n: Creating UI
#==============================================================================
#Add plot to Tabs
tab1 = Panel(child = row(controls,p_univariate), title = "Univariate")
tabs = Tabs(tabs = [tab1])

#Add tabs to doc
curdoc().add_root(tabs)

#Add title
curdoc().title ='Project Cyclops'