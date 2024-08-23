import numpy as np
import pandas as pd
import statsmodels.api as sm

anes96=sm.datasets.anes96
dataset_anes96=anes96.load_pandas()
df=dataset_anes96.data
length=len(df)
youngest=df.age.min()
oldest=df.age.max()
print(f"length is {length}\n youngest is: {youngest}\n oldest is :{oldest}")
df=df.rename(columns={'educ':'education'})
def get_party(df):
  if df['PID'] < 2:
    return "Democrat"
  elif df['PID'] > 4:
    return "Republican"
  else:
    return "Independent"
df['party'] = df.apply(get_party, axis = 1)
def get_agegroup(df):
  if df['age'] < 25:
    return "18-24"
  elif df['age'] < 35:
    return "25-34"
  elif df['age'] < 45:
    return "35-44"
  elif df['age'] < 55:
    return "45-54"
  elif df['age'] < 65:
    return "55-64"
  else:
    return "65 and over"
df['age_group'] = df.apply(get_agegroup, axis = 1)
print(df)