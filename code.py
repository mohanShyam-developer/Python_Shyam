####import random
####
####number = random.randint(1, 10)
####attempts = 5
####
####print("🎮 Guess the Number (1 to 10)")
####print("You have 3 attempts.\n")
####
####for i in range(attempts):
####    guess = int(input("Enter your guess: "))
####
####    if guess == number:
####        print("🎉 Correct! You win!")
####        break
####
####    elif guess > number:
####        print("📉 Too High!")
####
####    else:
####        print("📈 Too Low!")
####
####    print("Attempts left:", attempts - i - 1)
####
####else:
####    print("💀 Game Over!")
####    print("Correct number was:", number)
##
##import pyttsx3
##
##engine = pyttsx3.init()
##engine.runAndWait()
##def matalu_text(text):
##    engine.say(text)
##    while True:
##        user_input = input("you:").lower()
##        if user_input=="hello":
##            print(matalu_text("Bot:Hello there!"))
##        elif user_input=="hi":        
##            print(matalu_text("Bot:Hi,How are you?"))
##        elif user_input=="How are you":
##            print(matalu_text("Bot:iam great,how ur doing?"))
##        elif user_input=="Im absolutely fine!":
##            print(matalu_text("Bot:Awesome..buddy"))
##        elif user_input=="your name":
##            print(matalu_text("Bot:Iam a ChatBot"))
##        elif user_input=="my name is shyam":
##            print(matalu_text("Bot:nice name shyam"))
##        else:
##          print(matalu_text("Bot: sorry ,I dont understand that."))
##engine.runAndWait()
     
##
##       
##
##
##import pyttsx3
##
##engine = pyttsx3.init()
##
##def matalu_text(text):
##    engine.say(text)
##    engine.runAndWait()       
##matalu_text("hello boss, im you jarvis assistant")
##
##
##
##
####print("Hello, Im your chatbot")
####print("type bye to exit \n")
####
####while True:
####     user_input = input("you:").lower()
####
####     if user_input=="hello":
####         print("Bot:Hello there!")
####     elif user_input=="Hi":        
####         print("Bot:Hi,How are you?")
####     elif user_input=="How are you":
####         print("Bot:iam great,how ur doing?")
####     elif user_input=="Im absolutely fine!":
####         print("Bot:Awesome..buddy")
####     elif user_input=="your name":
####         print("Bot:Iam a ChatBot")
####     elif user_input=="my name is shyam":
####         print("Bot:nice name shyam")
####     else:
####         print("Bot: sorry ,I dont understand that.")
##import pyttsx3
##
##def matalu_text(text):
##    engine = pyttsx3.init()   
##    engine.say(text)
##    engine.runAndWait()
##    engine.stop()
##
##while True:
##    user_input = input("You: ").lower()
##
##    if user_input == "hello":
##        print("Bot: Hello there!")
##        matalu_text("Hello there!")
##
##    elif user_input == "hi":
##        print("Bot: Hi, how are you?")
##        matalu_text("Hi, how are you?")
##
##    elif user_input == "how are you":
##        print("Bot: I am great, how are you doing?")
##        matalu_text("I am great, how are you doing?")
##
##    elif user_input == "im absolutely fine":
##        print("Bot: Awesome buddy!")
##        matalu_text("Awesome buddy!")
##
##    elif user_input == "your name":
##        print("Bot: I am a ChatBot.")
##        matalu_text("I am a ChatBot.")
##
##    elif user_input == "bye":
##        print("Bot: Goodbye!")
##        matalu_text("Goodbye!")
##        break
##
##    else:
##        print("Bot: Sorry, I don't understand that.")
##        matalu_text("Sorry, I don't understand that.")
import pyttsx3

def matalu_text(text):
    engine = pyttsx3.init()   
    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        matalu_text("Hello there!")

    elif user_input == "hi":
        matalu_text("Hi, how are you?")

    elif user_input == "how are you":
        matalu_text("I am great, how are you doing?")

    elif user_input == "im absolutely fine":
        matalu_text("Awesome buddy!")

    elif user_input == "your name":
        matalu_text("I am a ChatBot.")

    elif user_input == "bye":
        matalu_text("Goodbye!")
        break

    else:
        matalu_text("Sorry, I don't understand that.")
