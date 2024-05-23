"""U.S. States Guessing Game"""
import turtle
import pandas

data = pandas.read_csv("50_states.csv")
print(data)
states_list = data.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
IMAGE = "blank_states_img.gif"
screen.bgpic(IMAGE)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the name of a state'?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Pull out row where row is the answer state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Use Pandas series to only pull name of state
        t.write(state_data.state.item())

screen.exitonclick()
