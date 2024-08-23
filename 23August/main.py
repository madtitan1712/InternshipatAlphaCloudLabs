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
