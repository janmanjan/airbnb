import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import OneSidedSelection

def u_samp(method, size, df):
    if method == 'random':
        end = pd.DataFrame()
        for each in list(set(df['country_destination'])):
            if df['country_destination'].value_counts().loc[each]>=size:
                sample = df[df['country_destination']==each].sample(n=size, random_state=24)
                end = pd.concat([end, sample], axis=0)
            else:
                og = df[df['country_destination']==each]
                end = pd.concat([end, og], axis=0)
    return end