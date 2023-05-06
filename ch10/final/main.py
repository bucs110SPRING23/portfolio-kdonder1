from proxyinspo import inspirationAPI
from proxyhumor import humorAPI


def quiz(happy, sad):
    '''
    This goal initializes the quiz game that the user plays. It sets the quiz questions, and keeps track of the users responses.
    args: (happy, sad). This function keeps track of the users answer so that the user can get a personalized resopnse from the
    program
    return: returns the happy and sad args
    '''
    print("☼☼☼  A small dose of sunshine: A quiz game to brighten your day  ☼☼☼")
    init = input("Enter b to begin: ").lower()
    if init == "b":
        print("Lets get started!")
        print("Answer each question to the best of your ability.")
        print("                      ~☼~☼~☼~☼~☼~")

        question1 = "t or f: Today I'm feeling happy"
        question2 = "t or f: I am hopeful for the future"
        question3 = "t or f: I got enough sleep last night"
        question4 = "t or f: The weather is nice today"
        question5 = "t or f: I'm staying hydrated"
        questionlist = (question1, question2, question3, question4, question5)

        for question in questionlist:
            print(question)
            choice = input("input your answer here: ").lower()
            if choice == "t":
                happy += 1
            if choice == "f":
                sad += 1
            print("-")
    else:
        print("Maybe next time :)")

    print("                  ~☼~☼~☼~☼~☼~☼~☼~☼~☼~☼~")
    return(happy, sad)


def main():
    '''
    From the users responses in the previous method, this method gives the user a personalized response. It calls the proxy
    classes, which is part of the personalized response.
    args: no args in this function- it's the main.py
    return: None.
    '''
    happy = 0
    sad = 0
    newhap, newsad = quiz(happy, sad)
    if newhap >= 3:
        print("I like your vibes! Here's a funny joke to keep you smiling:")
        humor = humorAPI(joke="")
        print(humor.get())
    if newsad >= 3:
        print("It's going to be ok! Here's an inspirational quote to brighten your day:")
        inspo = inspirationAPI(quote="", author="")
        print(inspo)

main()