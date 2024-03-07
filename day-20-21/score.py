from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"score: {self.score}", align= "center", font= ("Arial", 24, "normal"))
        self.hideturtle()
    def add_score(self):
        self.score += 1
        
   
        
      
        