# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
result_score = 0
data_states = pandas.read_csv('50_states.csv')
all_states = data_states.state.to_list()
guessed_states = []
while result_score <= 50:
    answer_state = screen.textinput(title=f"Guess the State {result_score}/50", prompt="What\'s another state\'s name?").title()
    result = data_states[data_states['state'] == answer_state]

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if not result.empty:
        guessed_states.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x = result.x.to_list()[0]
        y = result.y.to_list()[0]
        state.goto(x,y)
        state.write(f"{answer_state}")
        result_score += 1

