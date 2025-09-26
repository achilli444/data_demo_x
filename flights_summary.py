import pandas as pd
p="/mnt/data/airlines_flights_data_demo.csv"
df=pd.read_csv(p)
print(f"rows={len(df):,}, cols={len(df.columns)}")
print("Columns:", ", ".join(df.columns))
print("\nTop airlines by flights:")
print(df['airline'].value_counts().head(10))
g=df.groupby('airline').agg(avg_price=('price','mean'),
                            avg_duration=('duration','mean'),
                            flights=('airline','size')).sort_values('flights',ascending=False)
print("\nPer-airline summary (top 10):")
print(g.head(10).round(2))
df['route']=df['source_city']+"→"+df['destination_city']
r=(df.groupby('route').agg(avg_price=('price','mean'),
                           flights=('route','size'))
      .query('flights>=50').sort_values('avg_price',ascending=False))
print("\nMost expensive routes (>=50 flights):")
print(r.head(10).round(2))
