from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.color("white")
        self.penup()
        self.goto(60, 260)
        self.heading()
        self.hideturtle()
        self.board_update1()
        self.goto(-120, 260)
        self.score2 = 0
        self.board_update2()
    
        
    
    def board_update1(self):
        self.goto(60, 260)
        self.write(f"score: {self.score1}", align= "center", font= ("Arial", 24, "normal"))
        self.goto(60, 260)
    def board_update2(self):
        self.goto(-120, 260)
        self.write(f"score: {self.score2}", align= "center", font= ("Arial", 24, "normal"))    
        self.goto(-120, 260)
    
    def add_score1(self):
        self.score1 += 1
        self.clear()
        self.board_update1()
        self.board_update2() 
    
    def add_score2(self):
        self.score2 += 1
        self.clear()
        self.board_update2()
        self.board_update1()    

    
            
                