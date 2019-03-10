def big5():
    print('Welcome to the Big Five Personality Test. You will answer 50 questions '
          'which will determine your level of Extraversion, Agreeableness, '
          'Conscientiousness, Neuroticism, and Openness.')
    while True:
        ready = input('Are you ready to begin? Enter "Yes" to proceed. ')
        if ready.lower() != 'yes':
            print ('I will wait until you are ready to begin.')
            continue
        else:
            break
    print("Let's get started.")
    print("For each question, input a number, 1 through 5, where 1 = disagree and 5 = agree.")
    while True:
        q1 = input("1. I am the life of the party. ")
        if (q1.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q1) > 5 or int(q1) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q2 = input("2. I feel little concern for others. ")
        if (q2.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q2) > 5 or int(q2) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q3 = input("3. I am always prepared. ")
        if (q3.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q3) > 5 or int(q3) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q4 = input("4. I get stressed out easily. ")
        if (q4.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q4) > 5 or int(q4) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q5 = input("5. I have a rich vocabulary. ")
        if (q5.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q5) > 5 or int(q5) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q6 = input("6. I don't talk a lot. ")
        if (q6.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q6) > 5 or int(q6) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q7 = input("7. I am interested in people. ")
        if (q7.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q7) > 5 or int(q7) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q8 = input("8. I leave my belongings around. ")
        if (q8.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q8) > 5 or int(q8) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q9 = input("9. I am the life of the party. ")
        if (q9.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q9) > 5 or int(q9) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    while True:
        q10 = input("10. I have difficulty understanding abstract ideas. ")
        if (q10.isalpha() == True): 
            print('Input a number, not text.')
            continue
        elif int(q10) > 5 or int(q10) < 1:
            print('Input a number between 1 and 5.')
            continue
        else:
            break
    oScore = 8 + int(q5) - int(q10)
    cScore = 14 + int(q3) - int(q8)
    eScore = 20 + int(q1) - int(q5)
    aScore = 14 - int(q2) + int(q7)
    nScore = 38 - int(q4) + int(q9)
    print (oScore, cScore, eScore, aScore, nScore)
    
    
