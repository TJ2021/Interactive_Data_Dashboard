#pandas_datareader.data function extract data from various Internet sources into a pandas DataFrame
from pandas_datareader import data
import datetime
#bokeh is a plotting package that makes it simple to create complex plots from data in a dataframe
from bokeh.plotting import figure,show,output_file

def inc_dec(c,o):
    if c > o:
        value = 'Increase'
    elif o >c:
        value = 'Decrease'
    else:
        value = 'Equal'

    return value

start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,1,15)
df = data.DataReader(name='AAPL',data_source='yahoo',start=start,end=end)
df["Status"] = [inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df['Middle'] = (df.Close+df.Open)/2
df["Height"] = abs(df.Close-df.Open)
hour_12 = 12*60*60*1000

#create a new figure for plotting
p = figure(x_axis_type = 'datetime',width = 1000, height = 800,x_axis_label='date',y_axis_label='stock value')
p.title.text ='Candlestick Chart'
p.grid.grid_line_alpha = 0.4

#segment(x-cordinates of the starting point, y-coordinates of the starting point,x-cordinates of the ending point, y-coordinates of the ending point)
p.segment(df.index,df.High,df.index,df.Low,color = 'black') 
#configure and add rect glyphs to the figure
#rect(x-coordinates,y-cordinates,width,height)
p.rect(df.index[df.Status =="Increase"],df.Middle[df.Status == 'Increase'],hour_12,df.Height[df.Status == 'Increase'],fill_color='#90EE90',line_color='black')
p.rect(df.index[df.Status == "Decrease"],df.Middle[df.Status == 'Decrease'],hour_12,df.Height[df.Status == 'Decrease'],fill_color='#87CEFA',line_color='black')
output_file("CS.html")
show(p)


