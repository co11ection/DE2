import pandas as pd
import psycopg2
# Настройки подключения к локальной бд
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": 'mashina_kg',
    "user": "macbook",
    "password": '1',
    "client_encoding": "UTF8"
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price_usd INTEGER,
    year INTEGER,
    millage_km FLOAT,
    city TEXT,
    age INTEGER,
    url TEXT
)
"""

INSERT_SQL = """
INSERT INTO cars(title, price_usd, year, millage_km, city, age, url)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

def main():
    df = pd.read_csv("cars_clean.csv")
    
    # NaN -> None
    df = df.astype(object).where(pd.notnull(df), None)
    
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    cur.execute(CREATE_TABLE_SQL)
    
    for _, row in df.iterrows():
        cur.execute(
            INSERT_SQL, (
                row['title'],
                row['price_usd'],
                row["year"], 
                row["millage_km"],
                row["city"],
                row["age"],
                row["url"]
            )
        )
        
    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    main()