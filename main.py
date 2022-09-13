import turtle
import pandas

font = ("Arial", 7, "bold")
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
game_image = "blank_states_img.gif"

screen.addshape(game_image)
turtle.shape(game_image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
states_listed = data["state"].to_list()
states_x = data["x"].to_list()
states_y = data["y"].to_list()
correct_states = 0
guess_states = []
remaining_states = []

while correct_states != 50:
    user_answer = screen.textinput(title=f"{correct_states}/50 States Identified", prompt="Name a state that belong "
                                                                                          "to this map").title()
    if user_answer == "Exit":
        for missed_states in states_listed:
            if missed_states not in guess_states:
                remaining_states.append(missed_states)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_answer in states_listed:
        states_number = states_listed.index(user_answer)
        turtle.penup()
        x_cor = states_x[states_number]
        y_cor = states_y[states_number]
        turtle.setpos(x_cor, y_cor)
        turtle.write(user_answer, False, align="center", font=font)
        del states_listed[states_number], states_x[states_number], states_y[states_number]
        correct_states += 1
        guess_states.append(user_answer)

screen.exitonclick()
