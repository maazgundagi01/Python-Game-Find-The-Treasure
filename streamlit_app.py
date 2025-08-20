import streamlit as st

st.set_page_config(page_title="Treasure Island Adventure", layout="centered")

# ✨ Emojis outside ASCII only
st.write("🌊⚓🏴‍☠️🧜‍♀️🌋💣")

# ASCII art must remain EXACT
st.code('''                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--'""'-. 
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

st.write('''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')

st.title("Welcome to Treasure Island!")

# --- State ---
if "stage" not in st.session_state:
    st.session_state.stage = "start"
    st.session_state.direction = ""
    st.session_state.temp = {}

# Helper to make a continue button with exact prompt text
def cont(label, key):
    return st.button(label, key=key)

# ---------------- Start ----------------
if st.session_state.stage == "start":
    st.write("You have decided to set sail towards a small undiscovered island to find treasure of Jack Sparrow!")
    st.write("The problem is that the island is undiscovered hence you don't know which direction to go in")
    answer_1 = st.text_input('''What do you do?\n1. Type "map" - to look at the map\n2. Type "go" - to set sail to the north\n-> ''', key="answer_1").lower()
    if st.button("Submit Choice", key="submit_start"):
        if answer_1 == 'map':
            st.session_state.stage = "map_1"
        elif answer_1 == 'north' or answer_1 == 'go':
            st.write("""Who cares about map? Let's go!""")
            st.session_state.direction = 'north'
            st.session_state.stage = "sail_intro"
        else:
            st.error('Game Over: You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
            st.stop()

# ---------------- Map flow ----------------
elif st.session_state.stage == "map_1":
    if cont('It is an old exquisite piece of paper. \n[Press Enter to look closely and locate yourself]', "m1"):
        st.session_state.stage = "map_2"
elif st.session_state.stage == "map_2":
    if cont('The dock you are standing on is at the bottom \n[Press Enter to look where you should go]', "m2"):
        st.session_state.stage = "map_3"
elif st.session_state.stage == "map_3":
    if cont('You see three drawings on the map \n[Press Enter to examine the drawings]', "m3"):
        st.session_state.stage = "map_4"
elif st.session_state.stage == "map_4":
    if cont('''You examine the drawings and you see\nFire symbol in the north\nA dolphin's drawing in the east\nAnd a drawing of a ship wreckage in the west''', "m4"):
        st.session_state.stage = "map_choose"
elif st.session_state.stage == "map_choose":
    direction = st.text_input('''Where do you go?\nType "north" - to set sail north towards the fire symbol\nType "east"- set sail east towards the dolphin symbol\nType "west" - set sail towards west wrecked ship symbol\n-> ''', key="map_dir").lower()
    if st.button("Sail!", key="map_sail"):
        if direction in ['north','east','west']:
            st.session_state.direction = direction
            st.session_state.stage = "sail_intro"
        else:
            st.error('Game Over: You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
            st.stop()

# ---------------- Common sailing intro ----------------
elif st.session_state.stage == "sail_intro":
    if cont(f'''You sailed straight towards the {st.session_state.direction}! \n[Press Enter to keep sailing]''', "s1"):
        st.session_state.stage = "sail_sleep"
elif st.session_state.stage == "sail_sleep":
    if cont('You go to sleep and wake up next day.\nIt is an unremarkable day\nYou catch some fish, cook some food, look at the sunset\nAnd then you go to sleep.\nThis goes on for 2 days.\n[Press Enter to go back to sleep]', "s2"):
        # Branch
        if st.session_state.direction == 'north':
            st.session_state.stage = "north_1"
        elif st.session_state.direction == 'east':
            st.session_state.stage = "east_ask"
        elif st.session_state.direction == 'west':
            st.session_state.stage = "west_intro"

# ---------------- North branch ----------------
elif st.session_state.stage == "north_1":
    if cont('You fell asleep dreaming of beautiful mermaids\n[Press Enter to continue sleeping]', "n1"):
        st.session_state.stage = "north_2"
elif st.session_state.stage == "north_2":
    if cont('While you were asleep, you suddenly hear a BOOOOM! \n[Press Enter to WAKEEE UP!!!]', "n2"):
        st.session_state.stage = "north_3"
elif st.session_state.stage == "north_3":
    if cont("You rush out to see what has happened! \n[Press Enter to look through your scope]", "n3"):
        st.session_state.stage = "north_4"
elif st.session_state.stage == "north_4":
    if cont("You look towards the horizon to find a vol--A---WHAT??\nA VOLCANO HAS JUST ERUPTED AND YOU ARE TRAVELLING DIRECTLY TOWARDS ITTTT!!!!!\n[Press Enter to RUSH TOWARDS THE HELM!!!]", "n4"):
        st.session_state.stage = "north_5"
elif st.session_state.stage == "north_5":
    if cont("You promptly rush towards the helm \n[Press Enter to start steering away from the volcano]", "n5"):
        st.session_state.stage = "north_turn"
elif st.session_state.stage == "north_turn":
    turn_0 = st.text_input('''A volcano has erupted on the horizon!\nType "right" - to sail right and go east\nType "left" - to sail left and go west\n-> ''', key="turn0").lower()
    if st.button("Steer!", key="n_turn_btn"):
        # Preserve original logic literally (note: this makes condition always True like the console version)
        if turn_0 == 'right' or 'east':
            st.session_state.direction = 'east'
        elif turn_0 == 'left' or 'west':
            st.session_state.direction = 'west'
        else:
            st.error('You chose to continue straight, and slowly disappeared into the ashes...\n(You chose an invalid response or pressed enter, retry from start)\nThe End: You did not find the treasure but you are alive')
            st.stop()
        st.write('PHEW! You turn right just in time\nYou avoid the suffocating smoke, ash and the tsunami')
        if cont(f'You set the sails to go towards {st.session_state.direction} \n[Press Enter to continue]', "n_after_turn"):
            if st.session_state.direction == 'east':
                st.session_state.stage = "east_ask"
            else:
                st.session_state.stage = "west_intro"

# ---------------- East branch ----------------
elif st.session_state.stage == "east_ask":
    turn_1 = st.text_input('''You are asleep and you hear a gentle voice, it sounds like a lullaby your mother used to sing \nType "out" - to go out on the deck and check who's there\nType "hide" - to lock the door and hide!\n-> ''', key="turn1").lower()
    if st.button("Decide", key="e_decide1"):
        if turn_1 == 'out':
            st.session_state.stage = "east_out"
        else:
            st.session_state.stage = "east_hide_1"
elif st.session_state.stage == "east_out":
    turn_1b = st.text_input('''You go out to find a mermaid waiting for you what do you do?\nType "go" - to go to the mermaid\nType "hide" - to go back and hide!\n-> ''', key="turn1b").lower()
    if st.button("Decide", key="e_decide2"):
        if turn_1b == 'go':
            st.session_state.stage = "east_go_seq1"
        else:
            st.session_state.stage = "east_hide_1"
elif st.session_state.stage == "east_go_seq1":
    if cont('You continue to walk towards the mermaid \n[Press Enter to continue walking]', "e_go1"):
        st.write('Mermaid tells you go away! But you do not listen \n[Press Enter to start running!]')
        if cont('You spook the mermaid, the mermaid jumps down from the deck into the water \n[Press Enter to Stop!]', "e_go2"):
            if cont('Running towards the deck where mermaid was you try to stop\nBut mermaid had brought water on the floor, you slip and fall down from the deck into the water! \n[Keep Pressing Enter to try to swim back to the ship!]', "e_go3"):
                if cont('Hyahh! *Swim*', "e_sw1") and cont('Huahh *Swim*', "e_sw2") and cont('Ugh! *Swim*', "e_sw3") and cont('Hyahh! *Swim* You start getting tired', "e_sw4"):
                    st.write('Next morning a boat finds you floating over water holding on to a plank.\nThey rescue you and take you back to your home')
                    st.error('Game Over: You did not find the treasure but you returned home alive...')
                    st.stop()
elif st.session_state.stage == "east_hide_1":
    if cont('You hide, your grandma has told you far too many stories\nof pirates chasing mermaids and falling into the water.\nSo you hide \n[Press Enter to continue hiding]', "e_h1"):
        if cont('The voice keeps becoming sweeter and louder \n[Press Enter to continue hiding]', "e_h2"):
            if cont('The voice becomes even more sweeter and louder \n[Press Enter to keep hiding]', "e_h3"):
                if cont('The voice suddenly stops \n[Press Enter to go close to the door and listen]', "e_h4"):
                    if cont('The voice is gone now \n[Press Enter to open the door]', "e_h5"):
                        if cont('You open the door, the mermaid is nowhere to be seen.\nA sweet fragrance is lurking in the air\n[Press Enter to look around]', "e_h6"):
                            if cont('You look around but the mermaid is nowhere to be seen.\nYou look down to find an arrow pointing backwards.\nYou think you should follow the direction.\n[Press Enter to turn around]', "e_h7"):
                                st.session_state.direction = 'west'
                                if cont('Your slowly spin the wheel towards the west. \n[Press Enter to set your sails]', "e_h8"):
                                    st.write('You have set your sails to go west')
                                    st.session_state.stage = "west_intro"

# ---------------- West branch ----------------
elif st.session_state.stage == "west_intro":
    if cont("Your sails towards the west.", "w0"):
        st.session_state.stage = "west_ask"
elif st.session_state.stage == "west_ask":
    turn_2 = st.text_input('''You look towards the horizon and you see another ship.\nAs you continue sailing in that direction you realize it's not wrecked like the one in the map\nYou look through your scope and see a black flag\nType "wait" - to wait and see what happens\nType "attack" - to attack the ship\n-> ''', key="turn2").lower()
    if st.button("Decide", key="w_decide1"):
        if turn_2 == 'wait':
            st.write('''BOOM!! You hear a sound, 4 secs later "WRAAACK---CREEEK CREEEEK BAAAAAMM\nThe enemy ship attacks you and your ship is wrecked"''')
            if cont('They attack you before you attack them, you can not turn back now! \n[Press enter to prepare your attack!]', "w_wait1"):
                st.write('BOOM! they fire another shot which lands on your deck, making a big hole and water starts to come in')
                if cont('It is Loaded! \n[Press Enter to Fire your Cannon!]', "w_wait2"):
                    st.write('BOOM! You fire a shot but the pressure gets the worse of you and you miss the mast of their ship')
                    st.error('Game Over - You did not find the treasure and the pirates have imprisoned you')
                    st.stop()
        elif turn_2 == 'attack' or 'attack!':
            t2_action = st.text_input('''You load your canon, light it up! BOOOOOM!!! You fire at the enemy!\nEnemy raises their white flag and pivots to the east\nIt happens so that they were blocking your view, you have a clear sight of the treasure island and the wrecked ship!\nType "wreck" - to go towards the wrecked ship\nType "follow" - to follow the enemy ship\n-> ''', key="t2act").lower()
            if st.button("Choose", key="w_choose"):
                if t2_action == 'wreck':
                    if cont('You light your Cigar and sail towards the wreckage \n[Press Enter to Continue]', "w_wr1"):
                        if cont('Wha! What? The wrecked ship is empty!! The enemies already had the treasure!\nYou look behind and see the enemy ship crossing the horizon\n[Press Enter to Continue]', "w_wr2"):
                            st.error('Game Over - You found the treasure island! But you did not find the treasure. But you return home alive')
                            st.stop()
                elif t2_action == 'follow':
                    if cont('You are not one to be deceived!\nWhy would a pirate just surrender after being so close to the treasure\n[Press Enter to aim your canon]', "w_f1"):
                        if cont('It is a bit windy so your aim might not be that accurate\nBut you have element of surprise so a missed shot is not a big deal\n[Press Enter to load your canon]', "w_f2"):
                            if cont('3..2..1..\n[Press Enter to fire your canon!]', "w_f3"):
                                if cont('Oof! You miss by a little \n[Press Enter to adjust your canon]', "w_f4"):
                                    if cont('Carefully you re-adjust your canon.\nThe enemy did not expect you to fire and is still busy preparing their defence\n[Press Enter to load your canon]', "w_f5"):
                                        if cont('PRESS ENTER TO FIREEE!!!', "w_f6"):
                                            if cont('BOOOOOOMMMMMMMM! You have hit the mast of their ship [Press Enter twice to fire two warning shots!]', "w_f7"):
                                                st.write('BAAAM this warning shot lands to their right')
                                                st.write('BOOOM The warning shot lands to their left')
                                                st.write('Pirates understand that their ship is destroyed and they cannot fight you\nYou continue firing warning shots to make them abandon their ship')
                                                st.write('You see them fleeing their ship in boats\nYou do not see them carry any crates with them.')
                                                if cont('[Press Enter to approach the ship cautiously]', "w_f8"):
                                                    st.write('You board their ship and you find a big crate with shiny things inside!\n[Press Enter to open the crate]')
                                                    if cont('You open the crate...It is full of...\n[Press Enter]', "w_f9"):
                                                        if cont('TREASURE!! CONGRATULATIONS YOU HAVE FOUND THE TREASURE! \n[Press Enter to go home]', "w_f10"):
                                                            st.write('YOU WIN: You return home with the treasure, you become the legend of the town.\nYou help the village grow and your family prospers.\nThe next generations will thank you forever for your bravery!')
                                                            if cont('Press Enter to end the game', "w_f11"):
                                                                st.write('THE END')
                                                                st.write('''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')
                                                                st.code(''' By - Maz Gunn
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
                                                                st.stop()
                else:
                    st.error('You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
                    st.stop()
        else:
            st.error('You chose to turn back and go home, "adventures are for fools" you said. (You chose an invalid response, retry from start)\nThe End: You did not find the treasure but you are alive')
            st.stop()

# Footer emojis again (outside story copy)
st.write("🗺️🐬🔥🚢💥🎣🍲🌅💤🏆")
