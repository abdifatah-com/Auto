name: X Bot

on:
  schedule:
    - cron: "0 * * * *"  # Runs every hour
  workflow_dispatch:     # Allow manual run

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: pip install tweepy

    - name: Run bot script
      env:
        API_KEY: ${{ secrets.API_KEY }}
        API_SECRET: ${{ secrets.API_SECRET }}
        ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
        ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}
      run: python bot.py

