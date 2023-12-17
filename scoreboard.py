from turtle import Turtle

ALIGNMENT = "center"
FONT = ("JetBrains Mono", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("lime")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL {self.level}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        self.level = 0
        self.goto(-200, 250)

    def restart_game(self):
        self.clear()
        self.level = 1
        self.write(f"LEVEL {self.level}", False, ALIGNMENT, FONT)
