import pandas as pd
p="/mnt/data/airlines_tweets_data_demo.csv"
df=pd.read_csv(p)
neg=df[df['airline_sentiment']=='negative']
print("Top negative reasons overall:")
print(neg['negativereason'].fillna('Unknown').value_counts().head(15))
print("\nTop negative reasons by airline (top 5 per airline):")
for a,g in neg.groupby('airline'):
    top=g['negativereason'].fillna('Unknown').value_counts().head(5)
    print(f"\n== {a} =="); print(top)
cols=['tweet_id','airline','retweet_count','text']
top_rt=(neg[cols].sort_values('retweet_count',ascending=False).head(5))
print("\nMost retweeted negative tweets:")
print(top_rt.to_string(index=False))
