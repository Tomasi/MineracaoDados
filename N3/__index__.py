import pandas as pd
from textblob import TextBlob
import json

with open('Arts_Crafts_and_Sewing_5.json', 'r') as file:
    data = [json.loads(line) for line in file]

df = pd.DataFrame(data)
df = df.dropna(subset=['reviewText'])

def analyze_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity

df['sentiment'] = df['reviewText'].apply(analyze_sentiment)

menor_que_0 = df[df['sentiment'] < 0][['reviewText', 'sentiment']]
igual_a_0 = df[df['sentiment'] == 0][['reviewText', 'sentiment']]
entre_0_e_1 = df[(df['sentiment'] > 0) & (df['sentiment'] < 1)][['reviewText', 'sentiment']]

menor_que_0.to_excel('menor_que_0.xlsx', index=False)
igual_a_0.to_excel('igual_a_0.xlsx', index=False)
entre_0_e_1.to_excel('entre_0_e_1.xlsx', index=False)