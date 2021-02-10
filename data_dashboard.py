#pandas_datareader.data function extract data from various Internet sources into a pandas DataFrame
from pandas_datareader import data
import datetime

start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,1,15)

df = data.DataReader(name='AAPL',data_source='yahoo',start=start,end=end)
print(df)
