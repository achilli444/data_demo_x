import pandas as pd, numpy as np
p="/mnt/data/airlines_flights_data_demo.csv"
df=pd.read_csv(p)
df=df.dropna(subset=['price','days_left'])
print("Overall corr(price, days_left):", round(df['price'].corr(df['days_left']),4))
corr=(df.groupby('airline')
        .apply(lambda x: x['price'].corr(x['days_left']))
        .dropna().sort_values())
print("\nBy-airline correlation (price vs days_left):")
print(corr.round(4).head(20)); print(corr.round(4).tail(20))
bins=pd.cut(df['days_left'],bins=[-1,0,1,3,7,14,30,60,90,180,1e9],
            labels=["0","1","2-3","4-7","8-14","15-30","31-60","61-90","91-180","180+"])
bp=(df.assign(days_bucket=bins).groupby('days_bucket')['price']
      .agg(['count','mean','median']).reset_index())
out="/mnt/data/flights_price_by_daysleft.csv"; bp.to_csv(out,index=False)
print("\nSaved bucketed price stats to:", out)
print(bp.head(10).round(2))
