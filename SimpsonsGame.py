import random

def question_generator():

    #opens SimpsonsQ_A.txt file
    open_file = open("SimpsonsQ_A.txt")

    #creates an empty dictionary to store and organize txt file data
    empty_dictionary = {}

    #creates an empty list to keep track of questions given
    questions_given = []
    
    #iterates through each line to organize and split questions and answers
    for line in open_file:
        clean_line = line.strip(',\n' )
        split_line = clean_line.split(':')
        empty_dictionary[split_line[0]] = split_line[-1]

        #creates list of keys (questions)
        question_list = empty_dictionary.keys()

        #picks a random item from the list of questions
        random_question = random.choice(question_list)

    #adds new question asked to the questions_given list
    if random_question not in questions_given:
        questions_given.append(random_question)
        print random_question

def user_guess():

    #user_answer = raw_input(question_generator()).upper()
    user_answer = raw_input().upper()
#     correct_guesses = 0
#     num_of_questions = 0

#     while num_of_questions <=15:

#         if user_answer == question_answers[question_list]:
#             print "Woo Hoo! You're correct!"
#             correct_guesses += 1
#             num_of_questions += 1

#         elif user_answer == "quit":
#             break

#         else:
#             print "Do'oh!"
#             num_of_questions +=1

# print "Welcome to the Simpson's Trivia Game"
# print "type 'quit' to exit game"

user_guess()
question_generator()

# if num_of_questions == 15:
#     "You're a bonified Simpsons expert! You've answered all of the questions correctly. Great Job!"

# else:
#     "You've answered %i out of 15 questions correctly" % (correct_guesses)


        









