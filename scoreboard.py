from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'bold')
FONT2 = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_score_up(self):
        self.l_score += 1
        self.write_score()

    def r_score_up(self):
        self.r_score += 1
        self.write_score()

    def win(self):
        self.goto(0, 0)
        winner = "LEFT" if self.l_score == 2 else "RIGHT"
        self.write(f"AND THE WINNER IS \nPLAYER ON THE {winner}", align=ALIGNMENT, font=FONT2)
