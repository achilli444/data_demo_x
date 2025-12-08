import pandas as pd
import numpy as np

# Load both datasets using existing patterns
flights_path = "/mnt/data/airlines_flights_data_demo.csv"
tweets_path = "/mnt/data/airlines_tweets_data_demo.csv"

flights_df = pd.read_csv(flights_path)
tweets_df = pd.read_csv(tweets_path)

# Flight metrics by airline (following flights_summary.py pattern)
flight_metrics = flights_df.groupby('airline').agg({
    'price': ['mean', 'median'],
    'duration': 'mean',
    'airline': 'size'
}).round(2)
flight_metrics.columns = ['avg_price', 'median_price', 'avg_duration', 'flight_count']

# Twitter sentiment metrics (following tweets_sentiment_summary.py pattern)
sentiment_metrics = tweets_df.groupby('airline')['airline_sentiment'].value_counts().unstack(fill_value=0)
sentiment_metrics['total_tweets'] = sentiment_metrics.sum(axis=1)
sentiment_metrics['%positive'] = (sentiment_metrics.get('positive', 0) / sentiment_metrics['total_tweets'] * 100).round(2)
sentiment_metrics['%negative'] = (sentiment_metrics.get('negative', 0) / sentiment_metrics['total_tweets'] * 100).round(2)

# Merge datasets for correlation analysis
correlated_data = flight_metrics.join(sentiment_metrics, how='inner').dropna()

# Calculate correlations
print("=== Correlation Analysis ===")
print(f"Price vs % Positive Sentiment: {correlated_data['avg_price'].corr(correlated_data['%positive']):.4f}")
print(f"Flight Count vs Total Tweets: {correlated_data['flight_count'].corr(correlated_data['total_tweets']):.4f}")
print(f"Duration vs % Negative Sentiment: {correlated_data['avg_duration'].corr(correlated_data['%negative']):.4f}")

# Detailed comparison
print("\n=== Airline Performance vs Sentiment ===")
comparison = correlated_data[['avg_price', 'flight_count', '%positive', '%negative']].sort_values('%positive', ascending=False)
print(comparison.round(2))

# Save correlated results (following existing output pattern)
output_path = "/mnt/data/airline_performance_sentiment_correlation.csv"
comparison.to_csv(output_path)
print(f"\nSaved correlation results to: {output_path}")
