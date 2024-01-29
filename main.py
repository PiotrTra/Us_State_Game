import turtle 
import pandas

#Read a csv file using pandas
data = pandas.read_csv("50_states.csv")

#Set up screen with Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")    
image = "blank_states_img.gif"
screen.addshape(image)

#Change a turtle to image 
turtle.shape(image)


guessed_states = []  

#Putting all states to list form 50_states.csv
list_of_states = data.state.to_list()


while len(guessed_states) < 50:
    #Creating a bar to put the user's answer and guess the state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state name?").title() 
    #title()  makes that if we put answer which starts with a small letter the title() change a  small letter to big letter

    #Write Exit to leave game and write missing states you have to learn
    if answer_state == "Exit":
        #Using List Comprehension creating list of missing states
        missing_states = [state for state in list_of_states if state not in guessed_states]
        #Creating DataFrame with pandas
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #If answer_state is one of the state in all the states of the 50_states.csv
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        #Creating turtle to write correct answer on the correct state
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #Getting x and y of guessing state 
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        #Putting an answer to the correct coordinates
        t.write(answer_state)

    

