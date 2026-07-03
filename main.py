import pandas as pd

### ETL Process

### Extract

df = pd.read_csv('udemy.csv')

# print(df.head(5))
# print(df.tail(5))
# print(df.sample(5))

## Transform

## check the data types of the columns
#print(df.info())


df["published_date"] = pd.to_datetime(df["published_date"])

# print(df.info())

## func to check the nulls and duplicates then drop them

### not this action is taken for only tranining in the fact we need to check the data and define which need to cleaning and which not. For example, if the data is missing for a column that is not important then we can keep it as it is. But if the data is missing for a column that is important then we need to clean it.
def cleaning_data(df):
    print(df.shape)
    ## before cleaning
    print("Before Cleaning")
    print("Null Values: ", df.isnull().sum().sum())
    print("Duplicate Values: ", df.duplicated().sum())
    ## After cleaning
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    print("After Cleaning")
    print("Null Values: ", df.isnull().sum().sum())
    print("Duplicate Values: ", df.duplicated().sum())

    return df

cleaning_data(df)

### load 

df.to_csv('udemy_cleaned.csv', index=False)


### load to database

import sqlite3

def load_to_db(df, table_name, db_name):
    conn = sqlite3.connect(db_name)

    try:
        df.to_sql(
            table_name,
            conn,
            if_exists='replace',
            index=False
        )
        print("Data Loaded Successfully")
    except Exception as e:
        print("The error becuase: ", e)

    finally:
        conn.close()
    

load_to_db(df, 'Udemy', 'udemy.db')


### load to database using sqlalchemy

from sqlalchemy import create_engine
import urllib

def load_to_sqldb(df, table_name):

    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-LNUIJ9T;"
        "DATABASE=ETL_Test;"
        "Trusted_Connection=yes;"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    try:
        df.to_sql(
            table_name,
            engine,
            if_exists='replace',
            index=False
        )
        print("The table Created Successfully")

    except Exception as e:
        print("The error is becuase", e)


load_to_sqldb(df, 'Udemy')



