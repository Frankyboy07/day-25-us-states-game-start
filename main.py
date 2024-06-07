import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
correct = 0
answer_turtle = turtle.Turtle()
answer_turtle.penup()
answer_turtle.hideturtle()
correct_guesses = []
while correct < 50:
    answer_state = screen.textinput(title=f'{correct}/50 correct', prompt="What's another state's name?").title()

    if data['state'].str.contains(answer_state).any():
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            print(correct_guesses)
            x = data[data['state'] == answer_state]['x'].item()
            y = data[data['state'] == answer_state]['y'].item()
            answer_turtle.setpos(x, y)
            answer_turtle.write(answer_state, align='left', font=('Arial',8,'normal'))
            correct += 1

turtle.mainloop()
