# Simple ETL Pipeline with Pandas

## Project Overview

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline using Python and Pandas. The pipeline extracts data from a CSV file, performs basic data cleaning and transformation, and loads the processed data into multiple destinations.

---

## ETL Process

### 1. Extract

The dataset is loaded from a CSV file using the Pandas library.

```python
import pandas as pd

df = pd.read_csv("udemy.csv")
```

---

### 2. Transform

The transformation phase includes data exploration and cleaning.

#### Data Exploration

* Inspect data types using `df.info()`
* Detect missing values using `df.isnull()`
* Identify duplicate records using `df.duplicated()`

#### Data Cleaning

* Convert columns to appropriate data types (e.g., dates)
* Remove duplicate records
* Handle or remove missing values based on business requirements

> **Note:** In real-world ETL pipelines, missing values should be handled carefully. Not every null value should be removed; decisions should be based on the importance of each column and the business context.

---

### 3. Load

#### Load to CSV

Save the cleaned dataset as a new CSV file.

```python
df.to_csv("udemy_cleaned.csv", index=False)
```

#### Load to SQLite

Store the processed data in a SQLite database.

```python
import sqlite3

conn = sqlite3.connect("udemy.db")
df.to_sql("customers", conn, if_exists="replace", index=False)
```

#### Load to Microsoft SQL Server

Use SQLAlchemy to connect to SQL Server and load the processed data.

```python
from sqlalchemy import create_engine

engine = create_engine(connection_string)
df.to_sql("udemy", engine, if_exists="replace", index=False)
```

---

## Technologies Used

* Python
* Pandas
* SQLite
* Microsoft SQL Server
* SQLAlchemy

---

## Project Outcome

After running the pipeline, the cleaned dataset is successfully stored in:

* A CSV file
* A SQLite database
* A Microsoft SQL Server database

This makes the data ready for further analysis, reporting, or integration with downstream systems.
