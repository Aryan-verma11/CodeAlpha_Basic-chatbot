#  basic chatbot say bye to exit

def chatbot():
    print("Hii! i am simple chat bot ")
 

    while True:
        user_input=input("you:" ).lower()

        #it breaks the loop
        if "bye" in user_input:
            print("chatbot: good bye have a nice day ")
            break

        #chatbot response
        elif "hii" in user_input or "hello" in user_input:
            print("ChatBot: Hi there How can I help you?")

        elif "how are you" in user_input:
            print("ChatBot: I'm just a bot, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("ChatBot: I'm a simple rule-based chatbot")

        elif "time" in user_input:
            from datetime import datetime
            now=datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: the current time is {now}")

        elif "date" in user_input:
            from datetime import date
            today=date.today()
            print(f"Chatbot:todays date is {today}")

        else:
            print("Chatbot: sorry i dont understand that")

chatbot()