import tweepy
import time
import random
import os

# Load API keys from environment variables (set in GitHub Secrets)
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Tweets to post (add or edit as you want)
tweets_to_post = [
    "Change starts with a single voice 📢 #Somaliland #ClimateAction",
    "The future of diplomacy is built today 🤝 #ForeignPolicy",
    "Youth are the heartbeat of progress 💡 #Somaliland",
    "Every step toward justice matters 🌍 #InternationalRelations"
]

# Post interval in hours
post_interval_hours = 6
last_post_time = 0

print("🚀 Starting GitHub Actions Twitter Bot...")

while True:
    now = time.time()

    if now - last_post_time >= post_interval_hours * 3600:
        tweet = random.choice(tweets_to_post)
        try:
            api.update_status(tweet)
            print(f"📢 Posted tweet: {tweet}")
            last_post_time = now
        except tweepy.TweepError as e:
            print(f"⚠️ Error posting tweet: {e.reason}")

    # Sleep 5 minutes before next check
    time.sleep(300)
