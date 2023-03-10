import pandas as pd
from sqlalchemy import create_engine
from apicall import inr_rate


connection_string = 'mysql+mysqlconnector://root:1234@localhost:3306/gdp'
engine = create_engine(connection_string)


gdp_df = pd.read_sql("""
            SELECT *
            FROM gdp.gdp
            """, con=engine)

gdp_df['gdp'] = gdp_df['gdp'].astype(float)
gdp_df['gdp_inr'] = gdp_df['gdp'].apply(lambda x: x * inr_rate)
gdp_df['gdp_inr'] = gdp_df['gdp_inr'].round(3)

