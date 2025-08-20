import streamlit as st

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
    st.session_state.direction = ''
    st.session_state.volcano_escaped = False
    st.session_state.met_mermaid = False
    st.session_state.treasure_found = False

st.markdown("## 🏴‍☠️ Welcome to Treasure Island!")

# ASCII Art
if st.session_state.stage == 'start':
    st.code(r'''
                  __..-----')
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

    st.markdown("You have decided to set sail towards a small undiscovered island to find the treasure of **Jack Sparrow**!")
    answer_1 = st.radio("What do you do?", ['Look at the map', 'Set sail north'])

    if answer_1 == 'Look at the map':
        st.session_state.stage = 'map_look'
    elif answer_1 == 'Set sail north':
        st.session_state.direction = 'north'
        st.session_state.stage = 'north_sail'

elif st.session_state.stage == 'map_look':
    st.markdown("🗺️ You unfold the old map...")
    st.markdown("- Fire symbol in the **north**\n- A dolphin symbol in the **east**\n- Shipwreck in the **west**")
    map_choice = st.radio("Where do you go?", ['North (fire)', 'East (dolphin)', 'West (wreck)'])

    if map_choice.startswith("North"):
        st.session_state.direction = 'north'
        st.session_state.stage = 'north_sail'
    elif map_choice.startswith("East"):
        st.session_state.direction = 'east'
        st.session_state.stage = 'east_sail'
    elif map_choice.startswith("West"):
        st.session_state.direction = 'west'
        st.session_state.stage = 'west_sail'

elif st.session_state.stage == 'north_sail':
    st.markdown("🌋 You wake up to a loud **BOOM**! A volcano has erupted ahead!")
    turn_0 = st.radio("Quick! What do you do?", ['Sail Right (East)', 'Sail Left (West)'])

    if 'Right' in turn_0:
        st.session_state.direction = 'east'
        st.session_state.stage = 'east_sail'
    elif 'Left' in turn_0:
        st.session_state.direction = 'west'
        st.session_state.stage = 'west_sail'

elif st.session_state.stage == 'east_sail':
    if not st.session_state.met_mermaid:
        turn_1 = st.radio("You hear a gentle lullaby...", ['Go out to check', 'Hide inside'])

        if turn_1 == 'Go out to check':
            decision = st.radio("A mermaid appears!", ['Approach her', 'Run back and hide'])
            if decision == 'Approach her':
                st.markdown("🏊‍♂️ You slip and fall into the sea!")
                st.markdown("🚨 You are rescued days later, but no treasure for you.")
                st.session_state.stage = 'end'
            else:
                st.session_state.met_mermaid = True
                st.session_state.direction = 'west'
                st.session_state.stage = 'west_sail'
        else:
            st.session_state.met_mermaid = True
            st.session_state.direction = 'west'
            st.session_state.stage = 'west_sail'

elif st.session_state.stage == 'west_sail':
    turn_2 = st.radio("You see a pirate ship flying a black flag.", ['Wait and watch', 'Attack first'])

    if turn_2 == 'Wait and watch':
        st.markdown("☠️ They attack you first! Your ship is wrecked and you are captured.")
        st.session_state.stage = 'end'
    else:
        t2_action = st.radio("Your attack is successful! You now see the treasure island.", ['Go to wrecked ship', 'Follow the pirates'])

        if t2_action == 'Go to wrecked ship':
            st.markdown("💥 The shipwreck is empty. Pirates took the treasure.")
            st.session_state.stage = 'end'
        else:
            st.markdown("💣 You sink their ship and board it.")
            st.markdown("🎉 You find the crate full of **TREASURE**!")
            st.session_state.treasure_found = True
            st.session_state.stage = 'end'

if st.session_state.stage == 'end':
    if st.session_state.treasure_found:
        st.success("🏆 YOU WIN: You found the treasure and became a legend!")
    else:
        st.warning("🪙 GAME OVER: You didn't find the treasure, but you survived.")

    if st.button("Restart Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
