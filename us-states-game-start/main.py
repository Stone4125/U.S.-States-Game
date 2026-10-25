from turtle import Turtle, Screen
import pandas as pd

### Create a screen
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle_screen = Turtle()
turtle_text = Turtle()
turtle_screen.shape(image)

### Management of the data
data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
new_list = []

score = 0

### Body of the Game
game_is_over = False
while not game_is_over:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state's name?").title()
    if answer_state == "Exit":
        miss_states = []
        for state in state_list:
            if state not in new_list:
                miss_states.append(state)
        miss_state_data = pd.DataFrame({"state": miss_states})
        miss_state_data.to_csv("miss_states.csv")

        break

    if answer_state in state_list :
        if answer_state in new_list :
            pass
        else :
            new_list.append(answer_state)
            city_name = data[data["state"] == answer_state]
            cord = city_name["x"].to_list() + city_name["y"].to_list()

            turtle_text.teleport(cord[0], cord[1])
            turtle_text.up()
            turtle_text.hideturtle()
            turtle_text.write(city_name["state"].to_list()[0])

            score = score + 1
    if score > 50 :
        turtle_text.write("Congratulations, you guessed all the state it! You scored " + str(score) + "/ 50",
                          align="center", font=("Arial", 30, "bold"))
        game_is_over = True


