import mysql.connector as mysql
import pandas as pd
import numpy as np

connection = mysql.connect(host="localhost",
                           database='gdp',
                           user="root",
                           password="1234")

cursor = connection.cursor()

data = pd.read_excel('D:/NCG-Assignment/gdp/src/resources/gdp.xlsx')
data.replace(np.nan, 0000)
columns = list(data.columns)
year_column = columns[0]

for index, row in data.iterrows():
    try:
        insert_query = f"INSERT INTO gdp ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        cursor.execute(insert_query, tuple(row))
        connection.commit()

    except mysql.errors.IntegrityError as e:
        if "Duplicate entry" in str(e):
            duplicate_value = row[year_column]
