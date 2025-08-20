print('''                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. 
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  |
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#///
          ':|    "--'(#///)                 ?
                     (#///)                ?
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.|
                      (##///)        ||oMAZ||
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::"""        :: :     ""--.._
                  __..-'""           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....---- 
''')

print('''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
print("Welcome to Treasure Island!")
answer_1 = input('''You have decided to set sail towards a small undiscovered island to find treasure of Jack Sparrow!\nThe problem is that the island is undiscovered hence you don't know which direction to go in\nWhat do you do?\n1. Type "map" - to look at the map\n2. Type "go" - to set sail to the north\n-> ''').lower()
direction = ''
if answer_1 == 'map':
    input('It is an old exquisite piece of paper. \n[Press Enter to look closely and locate yourself]')
    input('The dock you are standing on is at the bottom \n[Press Enter to look where you should go]')
    input('You see three drawings on the map \n[Press Enter to examine the drawings]')
    input('''You examine the drawings and you see\nFire symbol in the north\nA dolphin's drawing in the east\nAnd a drawing of a ship wreckage in the west''')
    direction = input('''Where do you go?\nType "north" - to set sail north towards the fire symbol\nType "east"- set sail east towards the dolphin symbol\nType "west" - set sail towards west wrecked ship symbol\n-> ''').lower()
elif answer_1 == 'north' or answer_1 == 'go':
    print('''Who cares about map? Let's go!''')
    direction = 'north'
else:
    print('Game Over: You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
    exit(0)
input(f'''You sailed straight towards the {direction}! \n[Press Enter to keep sailing]''')
input('You go to sleep and wake up next day.\nIt is an unremarkable day\nYou catch some fish, cook some food, look at the sunset\nAnd then you go to sleep.\nThis goes on for 2 days.\n[Press Enter to go back to sleep]')

if direction == 'north':
    input('You fell asleep dreaming of beautiful mermaids\n[Press Enter to continue sleeping]')
    input('While you were asleep, you suddenly hear a BOOOOM! \n[Press Enter to WAKEEE UP!!!]')
    input("You rush out to see what has happened! \n[Press Enter to look through your scope]").lower()
    input("You look towards the horizon to find a vol--A---WHAT??\nA VOLCANO HAS JUST ERUPTED AND YOU ARE TRAVELLING DIRECTLY TOWARDS ITTTT!!!!!\n[Press Enter to RUSH TOWARDS THE HELM!!!]")
    input("You promptly rush towards the helm \n[Press Enter to start steering away from the volcano]")
    turn_0 = input('''A volcano has erupted on the horizon!\nType "right" - to sail right and go east\nType "left" - to sail left and go west\n-> ''').lower()
    if turn_0 == 'right' or 'east':
        direction = 'east'
    elif turn_0 == 'left' or 'west':
        direction = 'west'
    else:
        print('You chose to continue straight, and slowly disappeared into the ashes...\n(You chose an invalid response or pressed enter, retry from start)\nThe End: You did not find the treasure but you are alive')
        exit(0)

    print('PHEW! You turn right just in time\nYou avoid the suffocating smoke, ash and the tsunami')
    input(f'You set the sails to go towards {direction} \n[Press Enter to continue]')
elif direction == 'east' or direction == 'west':
    print(f'2 more days and nights have passed as you continue towards {direction}')

if direction == 'east':
    turn_1 = input('''You are asleep and you hear a gentle voice, it sounds like a lullaby your mother used to sing \nType "out" - to go out on the deck and check who's there\nType "hide" - to lock the door and hide!\n-> ''').lower()
    if turn_1 == 'out':
        turn_1 = input('''You go out to find a mermaid waiting for you what do you do?\nType "go" - to go to the mermaid\nType "hide" - to go back and hide!\n-> ''').lower()
    if turn_1 == 'go':
        input('You continue to walk towards the mermaid \n[Press Enter to continue walking]')
        print('Mermaid tells you go away! But you do not listen \n[Press Enter to start running!]')
        input('You spook the mermaid, the mermaid jumps down from the deck into the water \n[Press Enter to Stop!]')
        input('Running towards the deck where mermaid was you try to stop\nBut mermaid had brought water on the floor, you slip and fall down from the deck into the water! \n[Keep Pressing Enter to try to swim back to the ship!]')
        input('Hyahh! *Swim*')
        input('Huahh *Swim*')
        input('Ugh! *Swim*')
        input('Hyahh! *Swim* You start getting tired')
        print('Next morning a boat finds you floating over water holding on to a plank.\nThey rescue you and take you back to your home')
        print('Game Over: You did not find the treasure but you returned home alive...')
        exit(0)
    else:
        input('You hide, your grandma has told you far too many stories\nof pirates chasing mermaids and falling into the water.\nSo you hide \n[Press Enter to continue hiding]')
        input('The voice keeps becoming sweeter and louder \n[Press Enter to continue hiding]')
        input('The voice becomes even more sweeter and louder \n[Press Enter to keep hiding]')
        input('The voice suddenly stops \n[Press Enter to go close to the door and listen]')
        input('The voice is gone now \n[Press Enter to open the door]')
        input('You open the door, the mermaid is nowhere to be seen.\nA sweet fragrance is lurking in the air\n[Press Enter to look around]')
        input('You look around but the mermaid is nowhere to be seen.\nYou look down to find an arrow pointing backwards.\nYou think you should follow the direction.\n[Press Enter to turn around]')
        direction = 'west'
        input('Your slowly spin the wheel towards the west. \n[Press Enter to set your sails]')
        print('You have set your sails to go west')
if direction == 'west':
    input("Your sails towards the west.")
    turn_2 = input('''You look towards the horizon and you see another ship.\nAs you continue sailing in that direction you realize it's not wrecked like the one in the map\nYou look through your scope and see a black flag\nType "wait" - to wait and see what happens\nType "attack" - to attack the ship\n-> ''').lower()
    if turn_2 == 'wait':
        print('''BOOM!! You hear a sound, 4 secs later "WRAAACK---CREEEK CREEEEK BAAAAAMM\nThe enemy ship attacks you and your ship is wrecked"''')
        input('They attack you before you attack them, you can not turn back now! \n[Press enter to prepare your attack!]')
        print('BOOM! they fire another shot which lands on your deck, making a big hole and water starts to come in')
        input('It is Loaded! \n[Press Enter to Fire your Cannon!]')
        print('BOOM! You fire a shot but the pressure gets the worse of you and you miss the mast of their ship')
        print('Game Over - You did not find the treasure and the pirates have imprisoned you')
        exit(0)
    elif turn_2 == 'attack' or 'attack!':
        t2_action = input('''You load your canon, light it up! BOOOOOM!!! You fire at the enemy!\nEnemy raises their white flag and pivots to the east\nIt happens so that they were blocking your view, you have a clear sight of the treasure island and the wrecked ship!\nType "wreck" - to go towards the wrecked ship\nType "follow" - to follow the enemy ship\n-> ''').lower()
        if t2_action == 'wreck':
            input('You light your Cigar and sail towards the wreckage \n[Press Enter to Continue]')
            input('Wha! What? The wrecked ship is empty!! The enemies already had the treasure!\nYou look behind and see the enemy ship crossing the horizon\n[Press Enter to Continue]')
            print('Game Over - You found the treasure island! But you did not find the treasure. But you return home alive')
        elif t2_action == 'follow':
            input('You are not one to be deceived!\nWhy would a pirate just surrender after being so close to the treasure\n[Press Enter to aim your canon]')
            input('It is a bit windy so your aim might not be that accurate\nBut you have element of surprise so a missed shot is not a big deal\n[Press Enter to load your canon]')
            input('3..2..1..\n[Press Enter to fire your canon!]')
            input('Oof! You miss by a little \n[Press Enter to adjust your canon]')
            input('Carefully you re-adjust your canon.\nThe enemy did not expect you to fire and is still busy preparing their defence\n[Press Enter to load your canon]')
            input('PRESS ENTER TO FIREEE!!!')
            input('BOOOOOOMMMMMMMM! You have hit the mast of their ship [Press Enter twice to fire two warning shots!]')
            input('BAAAM this warning shot lands to their right')
            print('BOOOM The warning shot lands to their left')
            print('Pirates understand that their ship is destroyed and they cannot fight you\nYou continue firing warning shots to make them abandon their ship')
            print('You see them fleeing their ship in boats\nYou do not see them carry any crates with them.')
            input('[Press Enter to approach the ship cautiously]')
            print('You board their ship and you find a big crate with shiny things inside!\n[Press Enter to open the crate]')
            input('You open the crate...It is full of...\n[Press Enter]')
            input('TREASURE!! CONGRATULATIONS YOU HAVE FOUND THE TREASURE! \n[Press Enter to go home]')
            print('YOU WIN: You return home with the treasure, you become the legend of the town.\nYou help the village grow and your family prospers.\nThe next generations will thank you forever for your bravery!')
            input('Press Enter to end the game')
            print('THE END')
            print('''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
            print(''' By - Maz Gunn
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-[U].-'MAZ o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            Maz'-._'-.|| |' `_.-'
                    '-.||_/.-'

       ''')
            exit(0)
        else:
            print(
                'You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
            exit(0)
    else:
        print(
            'You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
        exit(0)
else:
    print('You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
    exit(0)
