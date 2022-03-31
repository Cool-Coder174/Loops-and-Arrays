# Isaias Hernandez

NumOfQuiz = int(input(" ENTER THE NUMBER OF QUIZ'S: "))

total = 0
QuizCount = 1

for QuizNum in range(0, NumOfQuiz):
    score = input("ENTER THE SCORE FOR QUIZ " + str(QuizCount) + ": " )
    total = int(total) + int(score)
Avg = int(total)/int(NumOfQuiz)
print("The Quiz Average is: ", float(Avg))

# Activity F/B

print("WELCOME TO ANNOYING KID SIMULATOR 2020")
AgeIn = int(input("What age do you wanna simulate?: "))

if AgeIn >= 18:
    print("...I can drive if you are tired")
elif AgeIn < 18:
    for Counter in range(AgeIn, 0, -1):
        print("Are we there yet?")