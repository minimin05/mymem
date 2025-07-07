score1 = int(input(" Enter your score1: "))
score2 = int(input(" Enter your score2: "))
score3 = int(input(" Enter your score3: "))

average = (score1 + score2 + score3) / 3
print("Your average score is:", format(average, '.1f'))
if average > 95:
    print("Congratulation!")