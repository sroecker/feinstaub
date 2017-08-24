from __future__ import print_function

import pandas as pd

col_names = ['date', 'hour', 'mean_temp', 'humidity', \
            'mean_wspeed', 'wdegree', 'pressure', 'rainfall', \
            'radiation', 'radiation_balance', 'uva', 'uvb', \
            'no', 'no2', 'ozone', 'PM10', 'PM2_5']

df = None

for i in range(12):
    df_tmp = pd.read_excel('raw/Halbstd-Werte-Stuttgart-Mitte-SZ_2016.xls', \
             sheetname=i, skiprows=8, skip_footer=8, na_values='--', \
             parse_cols='A:C, F:G, I:T', names=col_names, header=None, verbose=True)
    #df.to_csv('sz-halfhour-2016_'+str(i)+'.csv', index=False)
    if df is None:
        df = df_tmp.copy()
    else:
        df = df.append(df_tmp, ignore_index=True)
    print(df.tail())

df.date = df.date.astype(str)
df.date = pd.to_datetime(df.date.str.split(' ', expand=True)[0] + ' ' + df.hour.astype(str))
df.drop('hour', axis=1, inplace=True)
df.to_csv('data/sz-halfhourly-2016.csv', index=False)
