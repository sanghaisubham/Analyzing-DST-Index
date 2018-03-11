import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Slider
from bokeh.layouts import widgetbox, row,column

df=pd.read_csv('DST(Time-Series Format).csv')
df['Datetime'] = pd.to_datetime(df['Datetime'])
df.index=df['Datetime']


# Define a callback function: callback
def callback(attr, old, new):
    
    # Read the current value of the slider: scale
    year = slider.value
    new_data={'x' :df.loc[(str(year))]['Datetime'],'y' :df.loc[(str(year))]['DST Index']}
    # Update source with the new data values
    source.data = new_data
    plot.title.text = 'DST Index Plot for year %d' % year


source = ColumnDataSource(data={
    'x'       : df['1975']['Datetime'],
    'y'       : df.loc['1975']['DST Index']
})
                          

plot = figure(x_axis_type='datetime',x_axis_label='Date', y_axis_label='DST',plot_width=1000)
                          
# Add a line to the plot
plot.line(x='x', y='y', source=source)
#Add the slider
slider = Slider(title='Slider to Change Year',start=1975, end=2018, step=1, value=2000)



# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)