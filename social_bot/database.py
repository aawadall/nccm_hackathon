"""Mock in memory database simulating actual db"""


class Database:
    # fields
    # tuple of (user, timestamp, tweet)
    tweets = []
    violations = []

    def __init__(self):
        """Constructor"""
        self.tweets = []
        self.violations = []

    # methods
    def store_tweet(self, user, timestamp, tweet):
        """Saves a tweet to tweets"""
        self.tweets.append((user, timestamp, tweet))

    def get_tweets(self, user=None):
        """Returns all tweets for a user if provided, otherwise all"""
        if user is None:
            return self.tweets
        else:
            return [tweet for tweet in self.tweets if tweet[0] == user]

    def store_violation(self, user, timestamp, violation):
        """Saves a violation to violations"""
        self.violations.append((user, timestamp, violation))

    def get_violations(self, user=None):
        """Returns all violations for a user if provided, otherwise all"""
        if user is None:
            return self.violations
        else:
            return [violation for violation in self.violations if violation[0] == user]
