print "Welcome to the Simpsons trivia game"

name = raw_input('What is your name?')

print "Alright %s, let's play!" % (name)

num_correct = 0

question_1 = raw_input("Question 1: Who created the Simpson's theme song? ").upper()

if question_1 == "DANNY ELFMAN":
    print "You're correct!"
    num_correct += 1

else:
    print "Ay, caramba! Wrong answer"

question_2 = raw_input("Question 2: What is the Simpsons' dog's name? ").upper()

if question_2 == "SANTA'S LITTLE HELPER":
    print "That's right!"
    num_correct += 1

else:
    print "DO'H!"

question_3 = raw_input(" Question 3: What musical instrument does Lisa Simpson usually play? ").upper()

if question_3 =="THE SAXOPHONE":
    print "Yay! Correcto"
    num_correct += 1

else:
    print "Come on. That was an easy one"

question_4 = raw_input("What is Krusty the Clown's monkey's name? ").upper()

if question_4 == "MR. TEENY":
    print "Good job!"
    num_correct += 1

else:
    print "Nope!"

question_5 = raw_input("Ok, last question. What Simpson's character has a full set of five fingers? ").upper()

if question_5 == "GOD":
    print "Correct!"
    num_correct += 1

else:
    "Wrong answer!"

if num_correct == 5:
    print "You're a certified Simpson's trivia God. You've gotten a perfect score. Good job!"

else:
    print "You've gotten %i out of 5 questions right. Don't have a cow man. Keep watching" % (num_correct)



