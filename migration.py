from pandas.io.stata import read_stata
import pandas as pd


class Ted(object):
    def __init__(self):
        pass

    def dta_to_csv(self):
        tr = read_stata("Treatment.dta")
        mh = read_stata("migration_history_4_22.dta")
        merged = mh.merge(tr)
        merged = merged.drop(['country_fill', 'admbound_fill', 'village_fill',
                              'programbase_', 'origin_location', 'origin_gps'],
                              axis=1)
        merged = merged.dropna()
        merged.columns = ['id', 'dt', 'lat', 'long', 'treatment']
        merged = merged[merged['dt']=='2013-08-01']
        merged.to_csv("migration.csv", index=False)

if __name__ == '__main__':
    t = Ted()
    t.dta_to_csv()
