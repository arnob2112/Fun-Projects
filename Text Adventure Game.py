def text_advanture_game():
    import random

    answer = input("Do you want to play? (yes / no)").lower().strip()
    if answer == "yes":
        print("Welcome to the Text Advanture Game!")
        start = True
        inventory = []
        if start:
            print("Stranger: Hello traveler, I see you are new to this world.")
            print("Stranger: This is world Pulaski, Chicago. You will find no other city in the world more aquint with providing top of the line hospitality.")
            print("Stranger: Right now we have to keep you alive, it seems you only have 20. Well do not fear, I will help you in the journey.")

            choice = input("Do you need my help? (yes / no)")
            if choice.lower() == "yes":
                choiceY1 = True
                print("Great to hear kid.")
                print("###--- You have been given brass knuckles ---###")
                print("All right then, lets make sure you know the streets.")
                inventory.append("Brass Knuckles")
            else:
                choiceY1 = False
                print("cool man, I have ya. Here have this map of the city so if you ever get lost you have something to guide you atleast.")
                print("###--- You have been given a map ---###")
                inventory.append("Map")

            if not choiceY1 and "Map" in inventory:
                print("Your map tells you to take left.")
                decide = input("Do you take left or right?")
                if decide.lower() == "right":
                    print("You got into a car accident now you are dead.")
                    print("Game over.")
                elif decide.lower() == "left":
                    approach1 = input("You are at a park and someone wants to fight with you, do you approach him? (yes / no)")
                    if approach1 == "no":
                        print("You are a coward.")
                        print("Game over.")
                    if approach1 == "yes":
                        print("***--- You are in a fight what will you do? Will you: ---***")
                        print("***--- ---***")
                        print("***--- A: Punch him? Success: 85% ---***")
                        print("***--- B: Kick him? Success: 33% ---***")
                        print("***--- C: Use brass kunckles? Success: 95% ---***")
                        decision = input("What will be your decision: A, B, C?")

                        minpoint = 1
                        maxpoint = 100

                        chA = (random.randint(minpoint, maxpoint)) * .85
                        chB = (random.randint(minpoint, maxpoint)) * .33
                        chC = (random.randint(minpoint, maxpoint)) * .95

                        if decision.upper() == "A" and chA > 25:
                            print("You decided to punch him.")
                            print("He is knocked out cold.")
                        elif decision.upper() == "B" and chB > 25:
                            print("You decided to kick him.")
                            print("He is knocked out cold.")
                        elif decision.upper() == "C" and chC > 25 and "Brass Kunckles" in inventory:
                            print("You use your brass kunckles.")
                            print("You beat him pretty bad.")
                        else:
                            print("That did not work and you are knocked out cold.")
                            print("Game over.")


            elif choiceY1:
                print("Cmon man, follow me to the park there is something important there to show you - it will help you on your journey.")
                print("Oh hold up, that there is danger dan, he likes to fight people with his mind you should fight him.")
                approach = input("Do you approach to individual? (yes / no)") #get start here step 10 done
                if approach.lower() == "no":
                    print("You are a coward.")
                    print("Game over.")
                if approach.lower() == "yes":
                    print("***--- You are in a fight what will you do? Will you: ---***")
                    print("***--- ---***")
                    print("***--- A: Punch him? Success: 85% ---***")
                    print("***--- B: Kick him? Success: 33% ---***")
                    print("***--- C: Use brass kunckles? Success: 95% ---***")
                    decision = input("What will be your decision: A, B, C?")

                    minpoint = 1
                    maxpoint = 100

                    chA = (random.randint(minpoint, maxpoint)) * .85
                    chB = (random.randint(minpoint, maxpoint)) * .33
                    chC = (random.randint(minpoint, maxpoint)) * .95

                if decision.upper() == "A" and chA > 25:
                    print("You decided to punch him.")
                    print("He is knocked out cold.")
                elif decision.upper() == "B" and chB > 25:
                    print("You decided to kick him.")
                    print("He is knocked out cold.")
                elif decision.upper() == "C" and chC > 25 and "Brass Kunckles" in inventory:
                    print("You use your brass kunckles.")
                    print("You beat him pretty bad.")
                else:
                    print("That did not work and you are knocked out cold.")
                    print("Game over.")

    else:
        print("Okay, some other time.")
    return

text_advanture_game()