import random

def get_rand_questions(num_questions, filename):
    #creates list of questions(keys)
    question_list = get_questions_from_file(filename).keys()

    #mixes questions at random
    random_question = random.shuffle(question_list)

    #returns the first five questions of list
    return question_list[:num_questions]

    print question_list

def get_questions_from_file(filename):
    #opens txt file
    questions_file = open(filename)

    #creates empty dictionary to store questions and answers
    questions = {}

    #iterates through each line of the txt file
    for line in questions_file:
        #cleans up the output of data
        clean_line = line.strip(',\n' )
        split_line = clean_line.split(':')
       
        #splits questions into keys and answers into values
        questions[split_line[0]] = split_line[-1].strip()   

    return questions

def user_guess(correct_count, question, answer_dict):
    #asks question and gets user input in a controlled format
    user_answer = raw_input(question).upper()
    
    #creates an instance for correct and incorrect user answers
    if user_answer == answer_dict[question]:
        print  "Woo Hoo! You're correct!"
        correct_count = correct_count + 1 

    else:
        print "Do'oh!"
        print "The answer is %s" % (answer_dict[question])
    return correct_count

print "Welcome to the Simpson's Trivia Game"

five_questions = get_rand_questions(5, "SimpsonsQ_A.txt")

answer_dict = get_questions_from_file("SimpsonsQ_A.txt")

#starts number of correct answers at zero
correct_count = 0

#creates a loop for each time question is answered, a count of correct answers is taken
for item in five_questions:
    correct_count = user_guess(correct_count, item, answer_dict)

if correct_count == 5:
    print  "           -----------------------------------------"
    print  "           | You're a bonified Simpsons expert!    |" 
    print  "|\/\/\/|   | You've answered all of the questions  |" 
    print  "|      |   | correctly. Great job!                 |"   
    print  "| (o)(o)   \_   ___________________________________/"   
    print  "c      _)    | /"                              
    print   "| '___|     <_/"
    print   "|   /"         
     

else:
   
    print  "           -----------------------------------------"
    print  "           | You've answered %d out of 5 questions  |" % (correct_count)
    print  "|\/\/\/|   |    correctly. Don't have a cow man.   |" 
    print  "|      |   |         You're still awesome!         |"   
    print  "| (o)(o)   \_   ___________________________________/"   
    print  "c      _)    | /"                              
    print   "| '___|     <_/"
    print   "|   /"         








