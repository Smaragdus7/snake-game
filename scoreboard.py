from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()
