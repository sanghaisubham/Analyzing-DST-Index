import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models.widgets import (Select)
from bokeh.layouts import widgetbox, row,column

df=pd.read_csv('DST(Time-Series Format).csv')
df['Datetime'] = pd.to_datetime(df['Datetime'])
df.index=df['Datetime']


# Define a update_plot function: update_plot
def update_plot(attr, old, new):
    
    # Read the current value of the year and if it is 2018 then only we can select months:01 & 02 only till that date,the value is updated
    if (str(year_select))!='2018':
        month_select.options=['01','02','03','04','05','06','07','08','09','10','11','12']
    else:
        month_select.options=['01','02']
        
    year = year_select.value
    month= month_select.value
    date=str(year)+'-'+str(month)
    
    new_data={'x' :df.loc[(str(date))]['Datetime'],'y' :df.loc[(str(date))]['DST Index']}
    # Update source with the new data values
    source.data = new_data
    #Display the new date for which the Plot is Drawn
    plot.title.text = 'DST Index Plot for Date %s' % date


source = ColumnDataSource(data={
    'x'       : df['1975-01']['Datetime'],
    'y'       : df.loc['1975-01']['DST Index']
})
                          

plot = figure(x_axis_type='datetime',x_axis_label='Date', y_axis_label='DST',plot_width=1000)
year_options=[]
# Add a line to the plot
plot.line(x='x', y='y', source=source)
for i in range(1975,2019):
    year_options.append(str(i))
    
year_select = Select(
    options=year_options,
    value='2000',
    title='Year'
)
year_select.on_change('value', update_plot)
# Attach the update_plot callback to the 'value' property of year_select


month_select = Select(
    options=['01','02','03','04','05','06','07','08','09','10','11','12'],
    value='01',
    title='Month'
)

# Attach the update_plot callback to the 'value' property of month_select

month_select.on_change('value', update_plot)

# Create layout and add to current document
layout = column(widgetbox(year_select,month_select), plot)

# Add the layout to the current document
curdoc().add_root(layout)