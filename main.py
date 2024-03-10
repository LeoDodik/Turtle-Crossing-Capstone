import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create instances
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player(screen)
player.go_up()

# Set up key bindings
screen.onkey(player.go_up, "w")
screen.listen()

# Game loop
game_is_on = True



# Call update_car_speed to start increasing car speed


while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create new cars randomly
    if random.randint(1, 6) == 1:
        car_manager.create_car()

    # Move cars
    car_manager.move_cars()

    # Check collision with player
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player finished a level
    if player.level_finished():
        scoreboard.increase_level()

# Exit the game when clicking on the screen
screen.exitonclick()
w