import turtle
import pandas
import random
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:/Users/USER/PycharmProjects/DAY 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/USER/PycharmProjects/DAY 25/us-states-game-start/50_states.csv")
states_list = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt="What's another state?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        tinny = turtle.Turtle()
        tinny.penup()
        tinny.hideturtle()
        tinny.goto(int(state_data.x), int(state_data.y))
        tinny.write(answer_state)


turtle.mainloop()





