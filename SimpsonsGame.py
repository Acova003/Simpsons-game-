
open_file = open("SimpsonsQ_A.txt")
read_file = open_file.read()

print "Welcome to the Simpson's Trivia Game"
print "type "quit" to exit game"

def question_generator():
    question_list = question_answers.keys
    rand_question = question_list.shuffle()

question_generator()

def user_guess():
    user_answer = raw_input(rand_question).upper()
    correct_guesses = 0
    num_of_questions = 0

    while num_of_questions <=15:

    if user_answer == question_answers[question_list]:
        print "Woo Hoo! You're correct!"
        correct_guesses += 1
        num_of_questions += 1

    elif user_answer == "quit"
        break

    else:
        print "Do'oh!"
        num_of_questions +=1

user_guess()


if num_of_questions == 15:
    "You're a bonified Simpsons expert! You've answered all of the questions correctly. Great Job!"

else:
    "You've answered %i out of 15 questions correctly" % (correct_guesses)


        









