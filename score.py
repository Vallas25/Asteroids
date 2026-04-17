from constants import *

class Score():
    def __init__(self):
        self.score = START_SCORE
    
    def add_to_score(self):
        self.score += 1
        print(f"score : {self.score}")