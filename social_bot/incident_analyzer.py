"""Hate Incident Analyzer"""


from os import urandom
from operator import itemgetter


class HateIncidentAnalyzer:
    """Hate Incident Analyzer"""

    def __init__(self, topics, discount_factor=0.9):
        """Initializes the class"""
        print('Initializing HateIncidentAnalyzer')
        self.topics = topics
        self.discount_factor = discount_factor

    def analyze_incident(self, tweet):
        """Analyzes a tweet for hate incidents, returns a vector of violations"""
        print('Analyzing tweet: {}'.format(tweet))
        # build some random vector of violations
        violations = [0] * len(self.topics)
        for i in range(len(self.topics)):
            if self.topics[i] in tweet:
                violations[i] = urandom.randint(0, 1)
        return violations

    def time_weighted_analysis(self, violations):
        """Given a list of violations for a particular user:
                returns time weighted analysis of hate incidents"""
        print('Time Weighted Analysis')
        # violations made of a list of user, timestamp, and violations
        # use most recent violation as baseline (maximum timestamp)
        baseline = max(violations, key=itemgetter(1))[0]

        # for each violation, calculate weight and multiply by violation
        weighted_violations = [0] * len(self.topics)
        for violation in violations:
            delta_t = baseline - violation[1]
            weighted_violations = weighted_violations + \
                [violation * (self.discount_factor ** delta_t)]
        # return sum of weights
        return weighted_violations
