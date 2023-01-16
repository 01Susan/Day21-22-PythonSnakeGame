from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.reading_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.writing_score(self.score)
        self.score = 0
        self.update_score()

    # Reading the High Score  from the data.txt file
    def reading_score(self):
        with open("data.txt", mode="r") as high_score_data:
            return high_score_data.read()

    # Writing the High score in data.txt

    def writing_score(self, high_score):
        with open("data.txt", mode='w') as updating_high_score:
            return updating_high_score.write(str(high_score))
