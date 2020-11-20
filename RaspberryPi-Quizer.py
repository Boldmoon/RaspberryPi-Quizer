import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
q1 = "1. Entomology is the science that studies"
option1 = [" a) Behavior of human beings", " b) Insects", " c) The formation of rocks"]
ans1 = "b) Insects"
q2 = "2. For which of the following disciplines is Nobel Prize awarded?"
option2 = [" a) Physics, Chemistry and Medicine", " b) Literature, Peace and Economics", " c) All of the above"]
ans2 = "c) All of the above"
q3 = "3. Hitler party which came into power in 1933 is known as"
option3 = [" a) Nazi Party", " b) Ku-Klux-Klan", " c) Democratic Party"]
ans3 = "a) Nazi Party"
q4 = "4. FFC stands for"
option4 = [" a) Federation of Football Council", " b) Film Finance Corporation", " c) Foreign Finance Corporation"]
ans4 = "b) Film Finance Corporation"
q5 = "5. Epsom (England) is the place associated wit"
option5 = [" a) Polo", " b) Snooker", " c) Horse racing"]
ans5 = "c) Horse racing"
q6 = "6. Galileo was an Italian astronomer who"
option6 = [" a) developed the telescope", " b) discovered four satellites of Jupiter", " c) All of the above"]
ans6 = "c) All of the above"
q7 = "7. Exposure to sunlight helps a person improve his health because"
option7 = [" a) the pigment cells in the skin get stimulated and produce Vitamin D",
           " b) the ultraviolet rays convert skin oil into Vitamin D",
           " c) the infrared light kills bacteria in the body"]
ans7 = "b) the ultraviolet rays convert skin oil into Vitamin D"
q8 = "8. For the Olympics and World Tournaments, the dimensions of basketball court are"
option8 = [" a) 27 m x 16 m", " b) 26 m x 14 m", " c) 28 m x 15 m"]
ans8 = "c) 28 m x 15 m"
q9 = "9. Film and TV institute of India is located at"
option9 = [" a) Rajkot (Gujarat)", " b) Pune (Maharashtra)", " c) Pimpri (Maharashtra)"]
ans9 = "b) Pune (Maharashtra)"
q10 = "10. The ozone layer restricts"
option10 = [" a) Infrared radiation", " b) X-rays and gamma rays", " c) Ultraviolet radiation"]
ans10 = "c) Ultraviolet radiation"
score = 0
inputv = "a"


def verify(ui, oa):
    global score
    if ui == oa[0]:
        score = score + 1
        print("Good Job!!! The answer is correct!!!")
    else:
        print("Wrong Answer :(")


def inputf():
    global inputv
    while True:
        if GPIO.input(16) == GPIO.HIGH:
            inputv = "a"
            break
        elif GPIO.input(10) == GPIO.HIGH:
            inputv = "b"
            break
        elif GPIO.input(18) == GPIO.HIGH:
            inputv = "c"
            break
        else:
            continue


def func():
    print("Hello, Welcome to RaspiQuiz")
    print("\n")
    print(q1)
    print(*option1, sep="\n")
    inputf()
    verify(inputv, ans1)
    time.sleep(2)
    print("\n")
    print(q2)
    print(*option2, sep="\n")
    inputf()
    verify(inputv, ans2)
    time.sleep(2)
    print("\n")
    print(q3)
    print(*option3, sep="\n")
    inputf()
    verify(inputv, ans3)
    time.sleep(2)
    print("\n")
    print(q4)
    print(*option4, sep="\n")
    inputf()
    verify(inputv, ans4)
    time.sleep(2)
    print("\n")
    print(q5)
    print(*option5, sep="\n")
    inputf()
    verify(inputv, ans5)
    time.sleep(2)
    print("\n")
    print(q6)
    print(*option6, sep="\n")
    inputf()
    verify(inputv, ans6)
    time.sleep(2)
    print("\n")
    print(q7)
    print(*option7, sep="\n")
    inputf()
    verify(inputv, ans7)
    time.sleep(2)
    print("\n")
    print(q8)
    print(*option8, sep="\n")
    inputf()
    verify(inputv, ans8)
    time.sleep(2)
    print("\n")
    print(q9)
    print(*option9, sep="\n")
    inputf()
    verify(inputv, ans9)
    time.sleep(2)
    print("\n")
    print(q10)
    print(*option10, sep="\n")
    inputf()
    verify(inputv, ans10)
    time.sleep(2)
    print("\n")
    print(f"Your total score is {score}")
    print("\nA project developed and maintained by Boldmoon.inc")
    print("\nFor more information visit www.boldmoon.in")
    print("\nThank you for playing RaspiQuiz© :)")
func()
