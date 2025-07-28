import pandas
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import FixedTicker,HoverTool,ColumnDataSource
from MOTION_DETECTION import df

# Ensure datetime format

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%D %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%D %H:%M:%S")

# Create figure

cds=ColumnDataSource(df)

f = figure(width=500, height=250, x_axis_type="datetime", title="Motion Graph")
f.xaxis.minor_tick_line_color = None
f.yaxis.ticker = FixedTicker(ticks=[1])

#hover functionality

hover =HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)

# Plot motion intervals as green bars

f.quad(top=1, bottom=0, left="Start", right="End", color="green",source=cds)

output_file("MOTION_DETECTION_GRAPH.html")
show(f)
