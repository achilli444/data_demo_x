import pandas as pd
p="/mnt/data/airlines_tweets_data_demo.csv"
df=pd.read_csv(p)
print(f"rows={len(df):,}, cols={len(df.columns)}")
print("Overall sentiment counts:")
print(df['airline_sentiment'].value_counts(dropna=False))
tot=df.groupby('airline')['airline_sentiment'].value_counts().unstack(fill_value=0)
tot['total']=tot.sum(1); tot['%positive']=(tot.get('positive',0)/tot['total']*100)
print("\nPer-airline sentiment (sorted by %positive):")
print(tot.sort_values('%positive',ascending=False).round(2))
by_hour=(pd.to_datetime(df['tweet_created'],errors='coerce')
           .dt.floor('H').value_counts().sort_index())
print("\nTweets per hour (first 10 points):")
print(by_hour.head(10))
