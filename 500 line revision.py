name = input
import time,sys
def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.028)
  value = print()
  return value

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.028)
  value = input()
  return value
  
def end_damage_escaped():
      ascii_game_over()
      answer = typingInput("You managed to escape, however you failed to take the right tools for the job and damaged the painting. All the gear and no idea! YOU LOSE! If you would like to try again please hit enter:  ").lower().strip()
      if answer == ("aada"):
         end_damage_escaped()
      else: start_game()

def start_game():
    global name
    name = typingInput("What is your name?: ").capitalize().strip()
    answer = typingInput(f"Hello {name} are you ready to play? \nYes or No?: ").lower().strip()
    if answer == "yes":
        question_1()
    else: answer == "no"
    start_game()

def question_1():
    typingprint (f"It is a beautiful sunny day so you decide to say yes to a message to go for a drink with your friend, Freddie, nick named Five-finger Freddie, in a pub close to a local art gallery, where he is working as a cleaner. Upon meeting him, he starts telling you about a painting that was just delivered at his work, which is supposed to be worth £100 million. He asked if you wanted to go with him. What do you choose {name}?")
    option_1()

def option_1():
    global name
    answer = typingInput("Yes or No: ").lower().strip()
    if answer == "yes":
        typingprint(" Awesome, let's go!")
        option_2()
    elif answer == ("no"):
         pushy_no()
    else:
        start_game()

def pushy_no():
    answer = typingInput ("You listened and decided that it wasn't worth it for you, so you refuse your friend's proposal. Five-finger Freddie offers you extra money to get involved. Did he manage to convince you? \n Yes or No: ").lower().strip()
    if answer == ("no"):
            ascii_game_over()
            typingprint("Five-finger Freddie, gets concerned that you might have turned over a new leaf and will report him to the authorities. He creeps up behind you after dropping you off and knocks you out in a dark alley, leaving you unconscious in the boot of a stolen car. Try again")
            start_game()
    else: option_2()

def option_2():
   global name
   answer = typingInput("You leave with your friend to a secure location and together you start planning hostile reconnaissance. Do you: \n A - Go and check security out at the gallery,\n B - Try and recruit someone else that could help or \n C - Go in guns blazing?: ").lower().strip()
   if answer == ("a"):
     security_1() 
   elif answer == ("b"):
      recruit_1()
   elif answer == ("c"):
       ascii_art_gallery()
       ascii_guns()
       ascii_game_over()
       typingprint("You chose to go in guns blazing; that was a rash decision; you and Five-finger Freddie rushed into the Art Gallery with weapons pointed at the security guard but before you even saw it, he managed to hit the panic button under his desk, which set the silent alarms of. The police managed to get there just as you and your friend were trying to find the room in which the painting was held.You were both caught and are now in Police Custody. GAME OVER!")
       answer = typingInput("Ready to start again? Hit enter!").lower().strip()
       if answer == (""):
            start_game()
   else:     
        option_2()

def gallery_plan_withcode():
      ascii_art_gallery()
      ascii_game_over()
      answer = typingInput("You arrive at the gallery, but have no tools to enter. If only you had keys or some sort of tool to force the door open. You failed to plan correctly. To start again hit enter: ").lower().strip()
      if answer == (""):
           start_game()
      else: gallery_plan_withcode()

def gallery_plan_withcrow():
      ascii_art_gallery()
      ascii_painting()
      answer = typingInput("You arrive at the gallery and use the crowbar to force entry into the building, setting off alarms in the process. You then locate the target using the floor plan. As you approach the painting you notice its secured with a code lock. you have to use the crowbar in order to break the code lock off. Woops! You damaged the painting! Are you ready to leave? \n Yes or No?:  ").lower().strip()
      if answer == ("yes"):
            end_damage_escaped()
      elif answer == ("no"):
            ascii_game_over()
            answer = typingInput("Well that wasnt a good call. You took too long and now the police have arrived and arrested you! GAME OVER. If you would like to start again, press enter:  ").lower().strip()
            if answer == (""):
              start_game()
      else: gallery_plan_withcrow

def gallery_keysplan_withcrow():
      ascii_art_gallery()
      ascii_painting()
      answer = typingInput("You arrive at the gallery and use the key you obtained to enter the building. You then locate the target using the floor plan. As you approach the painting you notice its secured with a code lock. You have to use the crowbar in order to break the code lock off. Woops! You damaged the painting! Are you ready to leave? \n Yes or No?:  ").lower().strip()
      if answer == "yes":
            end_damage_escaped()
      elif answer == ("no"):
            ascii_game_over()
            answer = typingInput("Well that wasnt a good call. You took too long and now the police have arrived and arrested you! GAME OVER. If you would like to start again, press enter:  ").lower().strip()
            if answer == (""):
              start_game()
      else: gallery_keysplan_withcrow

def gallery_keysplan_withcode():
      ascii_art_gallery()
      ascii_painting()
      answer = typingInput("You arrive at the gallery and use the key you obtained to enter the building. You then locate the target using the floor plan. As you approach the painting you notice its secured with a code lock. Good job we have the code generator!You crack the code and safely get the painting. Do you want to flee now? \n Yes or No?:  ").lower().strip()
      if answer == ("yes"):
           answer = typingInput("Great job! You stole the painting, kept it one piece and got away before the police arrived! 'Winner winner chicken dinner!' excitedly says Five-finger Freddie. If you would like to play again and see where else the adventure lead hit enter:  ").lower().strip()
           if answer == (""):
                 start_game()
      elif answer == ("no"):
            ascii_game_over()
            answer = typingInput("You're clearly out of your depth with that decision, you got it all right but your decision to stay allowed time for the police to arrive! You're nicked! GAME OVER. If you want to try again hit enter").lower().strip()
            if answer == (""):
                 start_game
      else: gallery_keysplan_withcode

def gallery_keys_withcrow():
      ascii_art_gallery()
      answer = typingInput("You arrive at the gallery and use the keys to enter the building. However, without a floor plan its difficult to locate the target painting. Do you want to keep looking? \n Yes or No?: ").lower().strip()
      if answer == ("yes"):
            ascii_painting()
            answer = typingInput("You eventualy locate the painting but notice its secured with a code lock. You use the crowbar to force it free. Woops, you damaged the painting. Are you ready to flee? \n Yes or No?: ").lower().strip()
            if answer == ("yes"):
                 end_damage_escaped()
      elif answer == ("no"):
            ascii_game_over()
            answer = typingInput("The Police arrive before you had a chance to leave. GAME OVER. If you want to try again press enter: ")
            if answer == (""):
                 start_game()
      else: gallery_keys_withcrow()

def gallery_keys_withcode():
      ascii_art_gallery()
      answer = typingInput("You arrive at the gallery and use the keys to enter the building. However, without a floor plan its difficult to locate the target painting. Do you want to keep looking? \n Yes or No?: ").lower().strip()
      if answer == ("yes"):
            ascii_painting()
            answer = typingInput("You finally locate the painting. You notice it is secured with a code lock. Good job you chose the code generator. You manage to crack the code lock and remove the painting intact! Nice!.............. OH NO! You took too long to find the painting and the police have arrived. GAME OVER. To start again hit enter").lower().strip()
            if answer == (""):
                 start_game()
      elif answer == ("no"):
            ascii_game_over()
            answer = typingInput("You failed in your mission and left empty handed! GAME OVER! To restart the game hit enter:  ").lower().strip()
            if answer == (""):
                 start_game()
      else: gallery_keys_withcode()

def gallery_no_code():
      ascii_art_gallery()
      ascii_game_over()
      answer = typingInput("You arrive at the gallery, but have no tools to enter, Five-finger Freddie looks as if you slapped his mum. If only you had keys or some sort of tool to force the door open. You failed to plan correctly. To start again hit enter: ").lower().strip()
      if answer == (""):
         start_game()
      else: start_game()

def gallery_no_withcrow():
      ascii_art_gallery()
      answer = typingInput("You arrive at the gallery and use the crowbar to break in, however you are struggling to find the painting because you dont have a floor plan. Do you want to: \n A - Leave or \n B- Keep looking?: ").lower().strip()
      if answer == ("a"):
            ascii_game_over()
            answer = typingInput("You were unable to find the painting so left before the Police arrived. GAME OVER. To start again hit enter: ").lower().strip()
            if answer == (""):
                 start_game()
      elif answer == ("b"):
          ascii_painting()
          answer = typingInput("You finally found the painting but it has a code lock securing it to the wall. You use the crowbar to to break the lock and damage the painting in the process. Do you want get out now? \n Yes or No: ").lower().strip()
          if answer == ("yes"):
              end_damage_escaped()
          elif answer == ("no"):
                ascii_game_over()
                answer == typingInput("The Police arrive before you had a chance to leave. GAME OVER. If you want to try again press enter: ").lower().strip()
                if answer == (""):
                     start_game
      else: gallery_no_withcrow

def storage_keysplan():
    answer = typingInput("You arrive at the storage unit and have a look in the tool cupboard. You can only carry one of the following 3 options: \n A - Code generator, \n B - Crow bar or \n C - Some pretty tasty looking snacks!: ").lower().strip()
    if answer == ("a"):
        typingprint("Excellent choice! Lets go to the gallery and get things moving!")
        gallery_keysplan_withcode()
    elif answer == ("b"): 
      ascii_crowbar()
      typingprint("That seems a good choice, off to the gallery we go!")
      gallery_keysplan_withcrow()
    elif answer == ("c"):
        ascii_snacks()
        ascii_game_over()
        answer = typingInput ("'SNACKS!' exclaims Five-finger Freddie 'Are you serious?!'. Five-finger Freddie loses faith in you and calls the whole thing off. Do you want to play again? Hit enter to restart!")
        if answer == (""):
             start_game()
    else: storage_keysplan() 

def storage_plan():
    answer = typingInput("You arrive at the storage unit and have a look in the tool cupboard. You can only carry one of the following 3 options: \n A - Code generator, \n B - Crow bar or \n C - Some pretty tasty looking snacks!: ").lower().strip()
    if answer == ("a"):
        typingprint("Excellent choice! Lets go to the gallery and get things moving!")
        gallery_plan_withcode() 
    elif answer == ("b"): 
        ascii_crowbar()
        typingprint("That seems a good choice, off to the gallery we go!")
        gallery_plan_withcrow()
    elif answer == ("c"):
        ascii_snacks()
        ascii_game_over()
        answer = typingInput("'SNACKS!' exclaims Five-finger Freddie 'Are you serious?!'. Five-finger Freddie loses faith in you and calls the whole thing off. Do you want to play again? Hit enter to restart!")
        if answer == (""):
             start_game()
    else: storage_plan()

def storage_keys():
    answer = typingInput("You arrive at the storage unit and have a look in the tool cupboard. You can only carry one of the following 3 options: \n A - Code generator, \n B - Crow bar or \n C - Some pretty tasty looking snacks!: ").lower().strip()
    if answer == ("a"):
        typingprint("Excellent choice! Lets go to the gallery and get things moving!")
        gallery_keys_withcode()
    elif answer == ("b"): 
        ascii_crowbar()
        typingprint("That seems a good choice, off to the gallery we go!")
        gallery_keys_withcrow()
    elif answer == ("c"):
        ascii_snacks()
        ascii_game_over()
        answer = typingInput("'SNACKS!' exclaims Five-finger Freddie 'Are you serious?!'. Five-finger Freddie loses faith in you and calls the whole thing off. Do you want to play again? Hit enter to restart!")
        if answer == (""):
             start_game()
    else: storage_keys()

def storage_no():
    answer = typingInput("You arrive at the storage unit and have a look in the tool cupboard. You can only carry one of the following 3 options: \n A - Code generator, \n B - Crow bar or \n C - Some pretty tasty looking snacks!: ").lower().strip()
    if answer == ("a"):
        typingprint("Excellent choice! Lets go to the gallery and get things moving!")
        gallery_no_code()
    elif answer == ("b"): 
      ascii_crowbar()
      typingprint("That seems a good choice, off to the gallery we go!")
      gallery_no_withcrow()
    elif answer == ("c"):
       ascii_snacks()
       ascii_game_over()
       answer = typingInput("'SNACKS!' exclaims Five-finger Freddie 'Are you serious?!'. Five-finger Freddie loses faith in you and calls the whole thing off. Do you want to play again? Hit enter to restart!")
       if answer == (""):
             start_game()
    else: storage_no()

def pub_keysplan():
    ascii_plans()
    ascii_key()
    answer = typingInput("You arrive back to the pub with the keys and the floor plan to the gallery, which you picked up from the office. Five-finger Freddie suggests going to his lock up at a nearby storage unit to do some further planning. Do you: \n A - Go to the lock up or \n B - Have a few drinks and go later?: ").lower().strip()
    if answer == ("a"):
            typingprint("Lets get this show on the road!")
            storage_keysplan()
    elif answer == ("b"):
        ascii_game_over()
        answer = typingInput("One turned into two and two to ten. You got so drunk that you befriended a police officer and made a drunken confession about your plan. Press enter to start again!")
        if answer == (""):
             start_game()
    else: pub_keysplan()

def pub_plan():
    ascii_plans()
    answer = typingInput("You arrive back to the pub with the floor plan to the gallery, Five-finger Freddie suggests going to his lock up at a nearby storage unit to do some further planning. Do you: \n A - Go to the lock up or \n B - Have a few drinks and go later?: ").lower().strip()
    if answer == ("a"):
        typingprint("Lets get this show on the road!")
        storage_plan()
    elif answer == ("b"):
        ascii_game_over()
        answer = typingInput("One turned into two and two to ten. You got so drunk that you befriended a police officer and made a drunken confession about your plan. Press enter to start again!")
        if answer == (""):
         start_game()
    else: pub_plan()

def pub_keys():
    ascii_key()
    answer = typingInput("You arrive back to the pub with the keys to the gallery, your friend suggests going to his lock up at a nearby storage unit to do some further planning. Do you: \n A - Go to the lock up or \n B - Have a few drinks and go later?: ").lower().strip()
    if answer == ("a"):
        typingprint("Lets get this show on the road!")
        storage_keys()
    elif answer == ("b"):
        ascii_game_over()
        answer = typingInput("One turned into two and two to ten. You got so drunk that you befriended a police officer and made a drunken confession about your plan. Press enter to start again!")
        if answer == (""):
          start_game()
    else: pub_keys()

def pub_no():
    answer = typingInput("You arrive back to the pub with nothing that can help, Five-finger Freddie suggests going to his lock up at a nearby storage unit to do some further planning. Do you: \n A - Go to the lock up or \n B - Have a few drinks and go later?: ").lower().strip()
    if answer == ("a"):
       typingprint("Lets get this show on the road!")
       storage_no()
    elif answer == ("b"):
        ascii_game_over()
        answer = typingInput("One turned into two and two to ten. You got so drunk that you befriended a police officer and made a drunken confession about your plan. Press enter to start again!")
        if answer == (""):
          start_game()
    else: pub_no()

def friend_1():
    answer = typingInput("You managed to recruit Mikhael, your friend, who is actually working at the Art Gallery. He's offered you the keys to the gallery. Do you want them? \n Yes or No?:  ").lower().strip()
    if answer == ("yes"):
            typingprint("Lets's go back to the pub")
            pub_keys()
    if answer == ("no"):
            typingprint("We better have a drink after that decision.")
            pub_no()
    else: friend_1()

def gangster_1():
    ascii_game_over()
    answer = typingInput("That was a terrible decision, the gangster took all your information and has double crossed you. Ready to start again? Hit enter!").lower().strip()
    if answer == (""):
         start_game()

def recruit_1():
    answer = typingInput("Who do you want to recruit: \n A - Mikhael, your friend, who works in security or \n B - The local gangster? A or B?: ").lower().strip()
    if answer == ("a"):
        typingprint("I think thats a great choice")
        friend_1()
    elif answer == ("b"): 
        gangster_1()
    else: recruit_1()

def security_1():
    ascii_art_gallery()
    answer = typingInput("You arrive at the Gallery to check out the security. Do you: \n A - Attempt to befriend the guard, \n B - Follow the security guard or \n C - Attack the guard?: ").lower().strip()
    if answer == ("a"):
     befriend_1()
    elif answer == ("b"):
     follow_1()
    elif answer == ("c"):
        ascii_game_over()
        answer = typingInput("That was silly, the guard noticed you creeping up behind him and before you even got a chance to react he tasered you to the ground. The police have arrived and arrested you. GAME OVER! Ready to start again? Hit enter!").lower().strip()
        if answer == (""):
         start_game()
    else: security_1
    
def befriend_1(): 
    answer = typingInput("You have chosen to befriend the security guard, you talk for a short time and build rapport, what do you ask him about? \n A- Security cameras, \n B- General information or \n C- Monet painting?").lower().strip()
    if answer == ("a"):
        ascii_game_over()
        answer = typingInput("You ask the guard about the security cameras. The guard's suspicions were raised. He stopped for a second and looked at you while taking his taser out. He tasered you to the ground and waited until the police arrived to arrested you, responding to the silent alarm, triggered by the guard under his desk. Are you ready to start again? Hit enter! Hit enter!").lower().strip()
        if answer == (""):
         start_game
    elif answer == ("b"):
        typingprint("You ask the guard generally about the Gallery, no useful information is gained so you decide to head back to the pub and meet up with your friend")
        pub_no()
    elif answer == ("c"):
        ascii_painting()
        typingprint("You ask the guard about the 'Haystacks' painting by Monet and he provides a tour guide map showing where in the Art Gallery it is, with this new information you head back to the pub to meet with your friend.")
        pub_plan()
    else: befriend_1()
    
def follow_1():
    answer = typingInput("You begin following the guard on their route, suddenly they hear a noise and rush off to investigate, dropping their keys in the process. Do you: \n A- Take the keys and run back to the pub, \n B- Pick up the keys and check out the office or \n C - Keep following the guard?:  ").lower().strip()
    if answer == ("a"):
        pub_keys()
    elif answer == ("b"):
        pub_keysplan()
    elif answer == ("c"):
        ascii_game_over()
        answer = typingInput("You follow the guard into a restricted area, he notices you creeping up on him, turns around and tasers you to the ground. Ready to start again? Hit enter!").lower().strip()
        if answer == (""):
         start_game()
    else: follow_1()

def ascii_snacks():
    print("""
        _.-.
       ,'/ //
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  
""")

def ascii_plans():
    print("""
        _________   _________
   ____/      452\ /     453 \____
 /| ------------- |  ------------ |
||| ------------- | ------------- |||
||| ------------- | ------------- |||
||| ------- ----- | ------------- |||
||| ------------- | ------------- |||
||| ------------- | ------------- |||
|||  ------------ | ----------    |||
||| ------------- |  ------------ |||
||| ------------- | ------------- |||
||| ------------- | ------ -----  |||
||| ------------  | ------------- |||
|||_____________  |  _____________|||
L/_____/--------\\_//W-------\_____\J
""")

def ascii_crowbar():
    print(""""
 ______
|_,.,--|
   ||
   ||
   ##
   ##
""")

def ascii_key():
    print("""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
                                
""")

def ascii_start_game():
    print("""
      _______.___________.    ___      .______     .___________.     _______      ___      .___  ___.  _______ 
    /       |           |   /   \     |   _  \    |           |    /  _____|    /   \     |   \/   | |   ____|
   |   (----`---|  |----`  /  ^  \    |  |_)  |   `---|  |----`   |  |  __     /  ^  \    |  \  /  | |  |__   
    \   \       |  |      /  /_\  \   |      /        |  |        |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
.----)   |      |  |     /  _____  \  |  |\  \----.   |  |        |  |__| |  /  _____  \  |  |  |  | |  |____ 
|_______/       |__|    /__/     \__\ | _| `._____|   |__|         \______| /__/     \__\ |__|  |__| |_______|
                                                                                                              
   .___  ___.   ______   .__   __.  _______ .___________.    __    __   _______  __       _______.___________.
   |   \/   |  /  __  \  |  \ |  | |   ____||           |   |  |  |  | |   ____||  |     /       |           |
   |  \  /  | |  |  |  | |   \|  | |  |__   `---|  |----`   |  |__|  | |  |__   |  |    |   (----`---|  |----`
   |  |\/|  | |  |  |  | |  . `  | |   __|      |  |        |   __   | |   __|  |  |     \   \       |  |     
   |  |  |  | |  `--'  | |  |\   | |  |____     |  |        |  |  |  | |  |____ |  | .----)   |      |  |     
   |__|  |__|  \______/  |__| \__| |_______|    |__|        |__|  |__| |_______||__| |_______/       |__|     
                                                                                                                                                      
""")
def ascii_game_over():
    print(""" 
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
 """)

def ascii_guns():
    print("""
  +--^----------,--------,-----,--------^-,
  | |||||||||   `--------'     |          O
  `+---------------------------^----------|
    `\_,---------,---------,--------------'
      / XXXXXX /'|       /'
     / XXXXXX /  `\    /'
    / XXXXXX /`-------'
   / XXXXXX /
  / XXXXXX /
 (________(                
  `------' 
     """)
def ascii_painting():
    print("""
 ________________________
|.----------------------.|
||                      ||
||                      ||
||     .-"````"-.       ||
||    /  _.._    `\     ||
||   / /`    `-.   ; . .||
||   | |__  __  \   |   ||
||.-.| | e`/e`  |   |   ||
||   | |  |     |   |'--||
||   | |  '-    |   |   ||
||   |  \ --'  /|   |   ||
||   |   `;---'\|   |   ||
||   |    |     |   |   ||
||   |  .-'     |   |   ||
||'--|/`        |   |--.||
||   ;    .     ;  _.\  ||
||    `-.;_    /.-'     ||
||         ````         ||
|| ___________________||
'------------------------' """)
def ascii_art_gallery():
    print("""
 ____||____
 ///////////
///////////  
|    _    |  |
|[] | | []|[]|
|   | |   |  |
""")
ascii_start_game()
start_game()