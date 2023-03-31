import pandas as pd
import numpy as np

FILE_PATH = "stats_full_stack_dev.csv"

def fillData():
    data = pd.read_csv(FILE_PATH) 
    data = preprocess(data)
    data.to_csv(FILE_PATH)

def preprocess(df):
    #Adding random datetimes for 'time_stamp' column for past 1 hr
    last1 = pd.datetime.now().replace(microsecond=0) - pd.Timedelta('1H')

    dates = pd.date_range(last1, periods = 30 * 60 * 60, freq='S')
    
    N = len(df)
    df['time_stamp'] = np.random.choice(dates, size=N)
    
    return df

fillData()