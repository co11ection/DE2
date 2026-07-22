import pandas as pd

CURRENT_YEAR = 2026

def load_row(path='cars.csv'):
    df = pd.read_csv(path)
    return df

def clean(df):
    before = len(df)
    # Убираем строки если нету названия цены или годв выпуска
    df = df.dropna(subset=["title", "price_usd", "year"])
    # Убираем повторяющиеся обьявление смотри по url
    df = df.drop_duplicates(subset='url')
    
    df['age'] = CURRENT_YEAR - df["year"]
    
    after = len(df)
    print("before: ", before, "after: ", after, 'убранно строк: ', before-after)
    df = df.reset_index(drop=True)
    return df


def save_clean(df, path='cars_clean.csv'):
    df.to_csv(path, index=False)
    print("Сохранено")
    

if __name__ == "__main__":
    df = load_row()
    clean_df = clean(df)
    save_clean(clean_df)
    
    print(clean_df.groupby('city')['price_usd'].mean().round(0))