from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def level_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.screen.update_car_speed()
