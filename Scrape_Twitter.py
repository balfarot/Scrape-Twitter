# Scrape Twitter using Python 1 #
# Youtube Video: https://www.youtube.com/watch?v=P2NsIYZMPSk&t=1s #

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "covid"
limit = 100
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount])

df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet", "LikeCount"])
print(df)

df.to_csv('tweet100.csv')
