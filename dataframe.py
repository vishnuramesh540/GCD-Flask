import pandas as pd
from apicall import inr_rate
import numpy as np



gdp_df = pd.read_excel('gdp.xlsx')
gdp_df.replace(np.nan, 0000)
columns = list(gdp_df.columns)
year_column = columns[0]

gdp_df['gdp'] = gdp_df['gdp'].astype(float)
gdp_df['gdp_inr'] = gdp_df['gdp'].apply(lambda x: x * inr_rate)
gdp_df['gdp_inr'] = gdp_df['gdp_inr'].round(3)

