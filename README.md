# Analyzing-DST-Index
The disturbance storm time (Dst) index is a measure in the context of space weather. It gives information about the strength of the ring current around Earth caused by solar protons and electrons. This Project aims at analyzing the Disturbance storm time(DST) index using a web tool and then making useful insights and visualizations on the DST index over the last several years.

## Getting Started
**Dependencies**

 + Numpy
 + Pandas
 + Bokeh
 
 
**Running**

To run the project, perform following steps -
1) Run the `Data_Cleaning.ipynb` to regenerate the files `DST(1975-1999).csv` ,`DST(2000-2018).csv` files & the YearData and Month Data Folders .

2) Run `Web_Plotting_Tool.ipynb` file to regenerate `DST(Time-Series Format).csv` & feed in the start & end dates to get a plot of DST Index from start date to end date.

3) Run the command:
`bokeh serve --show Slider_Year.py`,
to run the Year Slider User Interactive application. The slider can be slid and the corresponding graph can be viewed and saved.

4) Run the command:
`bokeh serve --show Drop_Down.py`,
to Run the Year & Month Drop Down User Interactive application. The year and month options can be selected from the drop down to get the corresponding graph which can be viewed and saved.

5) The Database(`Space@DB`) is created which can be queried by the command:
python Querying_Database.py
The output if which can be obtained in file name `query_output.csv`.

6) Finally, run `Analyzing DST Index & Visualizations.ipynb` to get various plots and visualizations.
