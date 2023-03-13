import mysql.connector as mysql
import pandas as pd
from apicall import inr_rate
from sqlalchemy import create_engine
import numpy as np


connection = mysql.connect(host="localhost",
                           database='gdp',
                           user="root",
                           password="1234")

cursor = connection.cursor()

connection_string = 'mysql+mysqlconnector://root:1234@localhost:3306/gdp'
engine = create_engine(connection_string)

gdp_df = pd.read_sql("""
            SELECT *
            FROM gdp.gdp
            """, con=engine)


gdp_df['gdp'] = gdp_df['gdp'].astype(float)
gdp_df['gdp_inr'] = gdp_df['gdp'].apply(lambda x: x * inr_rate)
gdp_df['gdp_inr'] = gdp_df['gdp_inr'].round(3)

gdp_df.replace(np.nan, 0000)
columns = list(gdp_df.columns)
year_column = columns[0]


for index, row in gdp_df.iterrows():
    try:
        insert_query = f"INSERT INTO gdp ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        cursor.execute(insert_query, tuple(row))
        connection.commit()

    except mysql.errors.IntegrityError as e:
        if "Duplicate entry" in str(e):
            duplicate_value = row[year_column]
