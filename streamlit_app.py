import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

# Display ASCII art in an expandable container
with st.expander("Treasure Island ASCII Art"):
    st.text('''                  __..-----')
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

st.markdown("### 🏴‍☠️ Welcome to Treasure Island! 🏝️")

# Use session_state to keep track of state in Streamlit
if 'step' not in st.session_state:
    st.session_state.step = 'start'
    st.session_state.direction = ''
    st.session_state.turn_0 = ''
    st.session_state.turn_1 = ''
    st.session_state.turn_2 = ''
    st.session_state.t2_action = ''

def restart():
    st.session_state.step = 'start'
    st.session_state.direction = ''
    st.session_state.turn_0 = ''
    st.session_state.turn_1 = ''
    st.session_state.turn_2 = ''
    st.session_state.t2_action = ''
    st.experimental_rerun()

if st.session_state.step == 'start':
    answer_1 = st.radio(
        "You have decided to set sail towards a small undiscovered island to find the treasure of Jack Sparrow! 🏴‍☠️\n"
        "The island is undiscovered; you don't know which direction to go in.\nWhat do you do?",
        ('Look at the map 🗺️', 'Set sail north 🚢', 'Give up and go home')
    )
    if st.button("Choose"):
        if answer_1 == 'Look at the map 🗺️':
            st.session_state.step = 'map'
        elif answer_1 == 'Set sail north 🚢':
            st.session_state.direction = 'north'
            st.session_state.step = 'sailing'
        else:
            st.error('Game Over 💀: You chose to turn back and go home. Adventures are for fools. The End: You did not find the treasure but you are alive 🫡')
            if st.button("Restart"):
                restart()

elif st.session_state.step == 'map':
    st.write("It is an old exquisite piece of paper. 📜")
    st.write("The dock you are standing on is at the bottom 🛳️")
    st.write("You see three drawings on the map 🖼️:")
    st.write("🔥 Fire symbol in the north")
    st.write("🐬 A dolphin's drawing in the east")
    st.write("💀 A drawing of a shipwreck in the west")
    direction = st.radio("Where do you go?", ('north 🧭', 'east 🐬', 'west ☠️'))
    if st.button("Set Sail"):
        if 'north' in direction:
            st.session_state.direction = 'north'
        elif 'east' in direction:
            st.session_state.direction = 'east'
        elif 'west' in direction:
            st.session_state.direction = 'west'
        else:
            st.error("Invalid direction, please try again.")
            st.stop()
        st.session_state.step = 'sailing'
        st.experimental_rerun()

elif st.session_state.step == 'sailing':
    st.write(f"You sailed straight towards the {st.session_state.direction}! ⛵")
    st.write("You go to sleep and wake up next day. 🌅")
    st.write("It is an unremarkable day.\nYou catch some fish 🐟, cook some food 🍲, look at the sunset 🌇 and then go back to sleep. 😴\nThis goes on for 2 days.")
    if st.button("Continue"):
        if st.session_state.direction == 'north':
            st.session_state.step = 'volcano'
        elif st.session_state.direction == 'east':
            st.session_state.step = 'mermaid'
        elif st.session_state.direction == 'west':
            st.session_state.step = 'pirates'
        else:
            st.error('Unexpected direction. Restarting.')
            restart()

elif st.session_state.step == 'volcano':
    st.write("You fell asleep dreaming of beautiful mermaids 🧜‍♀️")
    st.write("Suddenly you hear a BOOOOM! 💥")
    st.write("You rush out and see a VOLCANO erupting! 🌋 You are sailing directly towards it!")
    turn_0 = st.radio("What do you do?", ('Turn right ➡️ (east)', 'Turn left ⬅️ (west)', 'Keep going straight'))
    if st.button("Make decision"):
        if turn_0 == 'Turn right ➡️ (east)':
            st.session_state.direction = 'east'
            st.session_state.step = 'sailing_after_volcano'
        elif turn_0 == 'Turn left ⬅️ (west)':
            st.session_state.direction = 'west'
            st.session_state.step = 'sailing_after_volcano'
        else:
            st.error("You chose to continue straight and got caught in the volcano ashes... 💨 Game Over!")
            if st.button("Restart"):
                restart()

elif st.session_state.step == 'sailing_after_volcano':
    st.write(f"Phew! You turned safely towards the {st.session_state.direction} and avoided the volcano.")
    if st.button("Continue sailing"):
        if st.session_state.direction == 'east':
            st.session_state.step = 'mermaid'
        elif st.session_state.direction == 'west':
            st.session_state.step = 'pirates'
        else:
            st.error("Invalid direction after volcano. Restarting.")
            restart()

elif st.session_state.step == 'mermaid':
    st.write("You hear a gentle lullaby singing...")
    choice = st.radio("What do you do?", ('Go out on deck to check 🚪', 'Hide inside 🛏️'))
    if st.button("Decide"):
        if choice == 'Go out on deck to check 🚪':
            st.session_state.step = 'meet_mermaid'
        else:
            st.session_state.step = 'hide_mermaid'

elif st.session_state.step == 'meet_mermaid':
    st.write("You find a mermaid waiting for you 🧜‍♀️")
    action = st.radio("What do you do?", ('Go to the mermaid 🏃‍♂️', 'Hide again 🛏️'))
    if st.button("Act"):
        if action == 'Go to the mermaid 🏃‍♂️':
            st.error("You spooked the mermaid and slipped into the water! You got rescued next morning but no treasure found.\nGame Over.")
            if st.button("Restart"):
                restart()
        else:
            st.session_state.step = 'hide_mermaid'

elif st.session_state.step == 'hide_mermaid':
    st.write("You hide and the voice becomes louder, then suddenly stops.")
    st.write("You open the door and see the mermaid is gone, but there is an arrow pointing backwards.")
    if st.button("Follow arrow and turn around"):
        st.session_state.direction = 'west'
        st.session_state.step = 'pirates'

elif st.session_state.step == 'pirates':
    st.write("You sail west and spot another ship with a black flag 🏴‍☠️")
    action = st.radio("What do you do?", ('Wait ⏳', 'Attack ⚔️'))
    if st.button("Decide"):
        if action == 'Wait ⏳':
            st.error("The enemy ship attacks first and wrecks your ship! Game Over.")
            if st.button("Restart"):
                restart()
        else:
            st.session_state.step = 'attack_pirates'

elif st.session_state.step == 'attack_pirates':
    st.write("You fire your cannon and the enemy ship surrenders and flees east.")
    action = st.radio("Now what?", ('Go towards the wrecked ship 🛳️', 'Follow enemy ship 🏃‍♂️'))
    if st.button("Choose"):
        if action == 'Go towards the wrecked ship 🛳️':
            st.error("The wrecked ship is empty. Enemies escaped with the treasure.\nGame Over.")
            if st.button("Restart"):
                restart()
        else:
            st.session_state.step = 'find_treasure'

elif st.session_state.step == 'find_treasure':
    st.write("You carefully approach the fleeing enemy ship and fire warning shots!")
    st.write("The pirates abandon their ship, leaving behind a crate of treasure! 💰")
    st.success("🎉 CONGRATULATIONS! YOU FOUND THE TREASURE! 🎉")
    st.write("You return home a hero and legend! 🏆")
    if st.button("Play Again"):
        restart()
