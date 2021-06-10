#!/usr/bin/env python3
import random

#~40 lines of code is a good benchamrk
#Return unique answers based on the input provided... multiple results should be possible.
#Control for user errors (suggested: methods, try/except, while loop)
#Use at least one while loop.
#Make all code "your own."
#ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative.

#while loop running through every question

questions_asked = []
morality = 0

questions = [
    {"question":"1: You’ve fallen in love with someone who belongs to a competing tribe. Your tribal elders do not approve of this union, and demand that you end all contact with your beloved. How do you respond?",
    "answer1":"1.1: Begrudgingly accept, knowing that their years of wisdom trump your emotionally clouded judgment.",
    "answer2": "1.2: Question their authority, and present a compelling case for why your union will benefit both tribes.",
    "answer3":"1.3: Sneak off with your beloved to start a new life away from either tribe.",
    "lvalue": "2",
    "2value": "3",
    "3value": "1"
    },
    {"question":"2: Alas, you’ve lived a full, long life, and will soon join your forefathers in the great beyond. What should be inscribed on the monument dedicated to your life?",
    "answer1":'2.1: "Feared by enemies, even in death."',
    "answer2": '2.2: “A gentle soul who changed the world."',
    "answer3":'2.3: “Rest in peace."',
    "lvalue": "1",
    "2value": "3",
    "3value": "2"
    },
    {"question":"3: You witness what appears to be a wealthy man shouting at and kicking a beggar. Satisfied with the damage he’s inflicted, the wealthy man walks away from the beggar. What do you do?",
    "answer1":"3.1: Nothing. It’s not your problem.",
    "answer2": "3.2: Run to the beggar to make sure he’s not seriously injured.",
    "answer3":"3.3: Tackle the wealthy man and beat him without mercy.",
    "lvalue": "1",
    "2value": "3",
    "3value": "2"
    },
    {"question":"4: The beggar seems fine and thanks you for your assistance. After walking away, you discover that your coin purse is missing, and the beggar has fled. What do you do now?",
    "answer1":"4.1: Attempt to track the thief down, and beat him until he returns what’s yours.",
    "answer2": '4.2: Report the "beggar" to the authorities.',
    "answer3":"4.3: Catch up with the wealthy man and ask for more information about the thief.",
    "lvalue": "1",
    "2value": "3",
    "3value": "2"
    },
    {"question":"5: You lent a friend a considerable amount of money shortly before they left on a months-long adventure. They’ve now returned, and discovered a small fortune while away. How do you approach the topic of the debt?",
    "answer1":"5.1: No need. A legally binding contract was written up with repayment details.",
    "answer2": "5.2: Insist on prompt repayment while they’re still flush with loot.",
    "answer3":"5.3: Wait until they’ve had a chance to recover from their trip before bringing it up.",
    "lvalue": "3",
    "2value": "1",
    "3value": "2"
    },
    {"question":"6: You’ve been tossed in prison for a crime you didn’t commit. What would you do next?",
    "answer1":"6.1: Wait for the system to discover the error and free you.",
    "answer2": "6.2: Talk your way out using your wits and charisma.",
    "answer3":"6.3: Fight your way out, killing anyone you need to in order to escape.",
    "lvalue": "3",
    "2value": "2",
    "3value": "1"
    },
    {"question":"7: After your release, you discover another man has been convicted in your place. You know that without him, his impoverished family will starve. What do you do?",
    "answer1":"7.1: Attempt to prove the man’s innocence, even if it means you may be convicted in his place.",
    "answer2": "7.2: Thank your maker that you avoided the punishment.",
    "answer3":"7.3: Falsify evidence to make sure only he is ever convicted for this crime.",
    "lvalue": "3",
    "2value": "2",
    "3value": "1"
    },
    {"question":"8: You witness a brutal brawl, and one of the fighters dies and is carted away. His coin purse was left behind in the commotion, and nobody but you seems to have noticed. What do you do?",
    "answer1":"8.1: Attempt to find the man’s family and return the gold to them.",
    "answer2": "8.2: Pocket the coins. He won’t need them.",
    "answer3":"8.3: Leave the purse. It’s not yours.",
    "lvalue": "3",
    "2value": "1",
    "3value": "2"
    },
    {"question":"9: You come across a scroll that allows you to cast a spell of invisibility on yourself for one hour. What would you do with it?",
    "answer1":"9.1: Use your newfound stealth to sneak into the keep and make off with all the gold you can carry.",
    "answer2": "9.2: Use it to pull some choice pranks on your friends.",
    "answer3":"9.3: Burn the scroll. Magic is too dangerous.",
    "lvalue": "1",
    "2value": "2",
    "3value": "3"
    },
    {"question":"10: A wizard presents you with a small box. He claims that he’ll make you extremely wealthy if you press a button on the box, but that someone somewhere in the world will instantly die. Do you hit the button?",
    "answer1":"10.1: Sure. You probably won’t know the person who dies.",
    "answer2": "10.2: Yes, but donate a portion of your new wealth to charity to clear your conscience.",
    "answer3":"10.3: Not only will you not push the button, but you vow to apprehend the wizard and destroy the box.",
    "lvalue": "1",
    "2value": "2",
    "3value": "3"
    },
]

# intro text
input('''
======================================================================================
                Welcome to the "Find Your Moral Alignment" Quiz! There are 
                ten questions that will be asked randomly. 
                How you choose to act in each scenario determines your inner morality!
                Would you like to get started?
                (press any key to continue) :\n''')


while len(questions_asked) <= 10:
    #get random question. make sure it is not equal to any previous question.
    
    if len(questions_asked) == 10:
        if morality <= 10:
            print('\n Test completed. \n')
            print('''You Got: Neutral Evil 
You see others as a means to an end. You only make friends and allies temporarily, and will turn on someone in a second if you can see a way to gain from it. You don’t really go out of your way to cause harm to others, but you don\'t really go out of your way to prevent it either. 
Popular neutral evil characters:
Voldemort from Harry Potter
Gaston from Beauty and the Beast
Littlefinger from Game of Thrones''')
        elif morality <= 20:
            print('Test completed. \n')
            print('''You Got: True Neutral
You don’t feel strongly about much of anything. Frankly, you can take or leave a lot of things in your life. You’re mostly guided by instinct, rather than conscious decision.
Popular true neutral characters:
Hawkeye from The Avengers
Hodor from Game of Thrones
Doctor Manhattan from Watchmen''')
        else :
            print('Test completed. \n')
            print('''You Got: Neutral Good
You are guided by your conscience, rather than any formal laws or traditions. You may occasionally break the rules, but it’s generally in service of the greater good.
Popular neutral good characters:
Jake the Dog from Adventure Time
Albus Dumbledore from Harry Potter
Glenn from The Walking Dead''')
        break

    #try except for input validation
    try:
        random_index = random.randint(0, 9)
        while questions[random_index] in questions_asked:
            random_index = random.randint(0, 9)

        #print question. get input
        print(questions[random_index]["question"])
        print(questions[random_index]["answer1"] + "\n")
        print(questions[random_index]['answer2'] + "\n")
        print(questions[random_index]['answer3'] + "\n")

    
        user_select = int(input("Choose 1, 2, or 3:"))
    
        if user_select < 1 or user_select > 3:
            raise ValueError('Your input should be 1, 2, or 3.') 
        questions_asked.append(questions[random_index])
        if user_select == 1:
            morality += int(questions[random_index]['1value'])
        elif user_select == 2:
            morality += int(questions[random_index]['2value'])
        else:
            morality += int(questions[random_index]['3value'])


    except:
        print("You must enter a whole number between 1 and 3.")
    
    
    print(f'Questions Asked: {len(questions_asked)}')
