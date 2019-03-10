def intro():
    print('''Welcome to the Big Five Personality Test. You will answer 10 questions 
    which will determine your level of Extraversion, Agreeableness, 
    Conscientiousness, Neuroticism, and Openness.''')
    while True:
        ready = input('Are you ready to begin? Enter "Yes" to proceed. ')
        if ready.lower() != 'yes':
            print ('I will wait until you are ready to begin. \n')
            continue
        else:
            break
    print("\n Let's get started. \n" );

def answers():
    total = 10
    answers = [0]*total
    for i in range(total):
        print ("For question " + str(i))
        answers[i] = int(input('Input number between 1 and 5: '))
        if int(answers[i]) > 5 or int(answers[i]) < 1:
            print('Input a valid number, between 1 and 5.')
            answers.pop(i)
            answers[i] = int(input('Input number between 1 and 5: '))
            answers.append('')
            continue
    oScore = answers[4] + answers[9]
    cScore = answers[2] + answers[7]
    eScore = answers[0] + answers[5]
    aScore = answers[1] + answers[6]
    nScore = answers[3] + answers[8]
    if oScore <= 3:
        print("You are LOW on openness!")
    elif oScore >= 4 and oScore <=6:
        print("You are MEDIUM on openness!")
    else:
        print("You are HIGH on openness!")
    if cScore <= 3:
        print("You are LOW on conscientiousness!")
    elif cScore >= 4 and cScore <=6:
        print("You are MEDIUM on conscientiousness!")
    else:
        print("You are HIGH on conscientiousness!")
    if eScore <= 3:
        print("You are LOW on extraversion!")
    elif eScore >= 4 and eScore <=6:
        print("You are MEDIUM on extraversion!")
    else:
        print("You are HIGH on extraversion!")
    if aScore <= 3:
        print("You are LOW on agreeableness!")
    elif aScore >= 4 and aScore <=6:
        print("You are MEDIUM on agreeableness!")
    else:
        print("You are HIGH on agreeableness!")
    if nScore <= 3:
        print("You are LOW on neuroticism!")
    elif nScore >= 4 and aScore <=6:
        print("You are MEDIUM on neuroticism!")
    else:
        print("You are HIGH on neuroticism!")


def big5():
    intro();
    print("For each question, input a number, 1 through 5, where 1 = disagree and 5 = agree.")
    print("I see myself as someone who ... \n")
    quiz = open("big5.txt", "r")
    line = quiz.readline()
    while line:
        for i in range(10):
            print (line)
            line = quiz.readline()
        answers();
    quiz.close()    
