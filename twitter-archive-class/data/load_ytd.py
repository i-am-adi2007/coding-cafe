import json
import pandas as pd

def load_ytd(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    if content.startswith('{') or content.startswith('['):
        return json.loads(content)
    
    eq_idx = content.find('=')
    if eq_idx == -1:
        raise ValueError(f"Could not parse file structure in {path}")
    
    json_str = content[eq_idx + 1:].strip()
    if json_str.endswith(';'):
        json_str = json_str[:-1].strip()
        
    return json.loads(json_str)

# 1. Load your tweets file (update path if your folder name is different)
tweets_data = load_ytd('twitter-archive-class/data/tweets.js')

# 2. Extract the inner 'tweet' dictionary into a DataFrame
df = pd.DataFrame([t['tweet'] for t in tweets_data])

# 3. Convert created_at to datetime (handling UTC)
df['created_at'] = pd.to_datetime(df['created_at'], format='mixed')

# 4. Filter for January 2020
jan_2020_tweets = df[(df['created_at'].dt.year == 2020) & (df['created_at'].dt.month == 1)].copy()

# Part a: How many tweets were posted in this month?
num_tweets = len(jan_2020_tweets)
print(f"a. Total tweets in Jan 2020: {num_tweets}")

# Part b: How many of them are retweets (full_text starts with 'RT @')?
num_retweets = jan_2020_tweets['full_text'].str.startswith('RT @').sum()
print(f"b. Total retweets: {num_retweets}")

# Part c: On which day of the month (1-31) were the most tweets posted?
jan_2020_tweets['day'] = jan_2020_tweets['created_at'].dt.day
busiest_day = jan_2020_tweets['day'].value_counts().idxmax()
print(f"c. Busiest day of the month: {busiest_day}")