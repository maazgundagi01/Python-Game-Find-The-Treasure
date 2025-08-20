import streamlit as st

st.set_page_config(page_title="Treasure Island Adventure", layout="centered")

# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = "start"
if "direction" not in st.session_state:
    st.session_state.direction = ""
if "turn_0" not in st.session_state:
    st.session_state.turn_0 = ""
if "turn_1" not in st.session_state:
    st.session_state.turn_1 = ""
if "turn_2" not in st.session_state:
    st.session_state.turn_2 = ""
if "t2_action" not in st.session_state:
    st.session_state.t2_action = ""

def reset_game():
    st.session_state.step = "start"
    st.session_state.direction = ""
    st.session_state.turn_0 = ""
    st.session_state.turn_1 = ""
    st.session_state.turn_2 = ""
    st.session_state.t2_action = ""

def show_ascii_art():
    st.code('''                  __..-----')
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

st.markdown("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
st.title("Welcome to Treasure Island! 🏴‍☠️")

# --- START STEP ---
if st.session_state.step == "start":
    choice = st.radio(
        "You have decided to set sail towards a small undiscovered island to find treasure of Jack Sparrow!\n"
        "The problem is that the island is undiscovered hence you don't know which direction to go in.\n"
        "What do you do?",
        ("Look at the map 🗺️", "Go North 🚢", "Turn back 🏠")
    )
    if st.button("Choose"):
        if choice == "Look at the map 🗺️":
            st.session_state.step = "map"
        elif choice == "Go North 🚢":
            st.session_state.direction = "north"
            st.session_state.step = "sailing"
        else:
            st.session_state.step = "game_over"
            st.session_state.game_over_reason = (
                'You chose to turn back and go home, "adventures are for fools" you said. '
                '(You chose an invalid response, retry from start)\n'
                'The End: You did not find the treasure but you are alive.'
            )
    st.stop()

# --- MAP STEP ---
if st.session_state.step == "map":
    st.markdown("""
    It is an old exquisite piece of paper.

    The dock you are standing on is at the bottom.

    You see three drawings on the map:
    - Fire symbol in the north 🔥
    - A dolphin's drawing in the east 🐬
    - A drawing of a ship wreckage in the west 🚢
    """)
    direction_choice = st.radio(
        "Where do you go?",
        ("North 🔥", "East 🐬", "West 🚢")
    )
    if st.button("Set Sail"):
        st.session_state.direction = direction_choice.split()[0].lower()
        st.session_state.step = "sailing"
    st.stop()

# --- SAILING STEP ---
if st.session_state.step == "sailing":
    st.markdown(f"You sailed straight towards the **{st.session_state.direction}**! ⛵️")
    st.markdown("""
    You go to sleep and wake up the next day.  
    It is an unremarkable day.  
    You catch some fish, cook some food, look at the sunset, and then you go to sleep.  
    This goes on for 2 days.
    """)
    if st.button("Continue"):
        if st.session_state.direction == "north":
            st.session_state.step = "volcano"
        elif st.session_state.direction in ["east", "west"]:
            # skip to corresponding step
            if st.session_state.direction == "east":
                st.session_state.step = "east_mermaid"
            else:
                st.session_state.step = "west_ship"
    st.stop()

# --- NORTH VOLCANO STEP ---
if st.session_state.step == "volcano":
    st.markdown("""
    You fell asleep dreaming of beautiful mermaids.  
    Suddenly, you hear a **BOOOM!**  
    You rush out and see a volcano erupting right ahead!  
    You must steer away quickly!
    """)
    turn = st.radio(
        "Which way do you turn to avoid the volcano?",
        ("Right (East)", "Left (West)")
    )
    if st.button("Turn"):
        if turn.startswith("Right"):
            st.session_state.direction = "east"
            st.session_state.step = "sailing_after_volcano"
        else:
            st.session_state.direction = "west"
            st.session_state.step = "sailing_after_volcano"
    st.stop()

# --- AFTER VOLCANO SAILING ---
if st.session_state.step == "sailing_after_volcano":
    st.markdown(f"PHEW! You turned towards the **{st.session_state.direction}** just in time and avoided the volcano ash and tsunami.")
    if st.button("Continue Sailing"):
        if st.session_state.direction == "east":
            st.session_state.step = "east_mermaid"
        else:
            st.session_state.step = "west_ship"
    st.stop()

# --- EAST MERMAID STEP ---
if st.session_state.step == "east_mermaid":
    st.markdown("""
    You are asleep and you hear a gentle voice, a lullaby your mother used to sing.
    """)
    choice = st.radio(
        "What do you do?",
        ("Go out on deck to check who's there", "Hide and lock the door")
    )
    if st.button("Choose"):
        if choice == "Go out on deck to check who's there":
            st.session_state.step = "mermaid_encounter"
        else:
            st.session_state.step = "mermaid_hide"
    st.stop()

# --- MERMAID ENCOUNTER ---
if st.session_state.step == "mermaid_encounter":
    choice = st.radio(
        "You find a mermaid waiting for you. What do you do?",
        ("Go to the mermaid", "Hide and go back inside")
    )
    if st.button("Choose"):
        if choice == "Go to the mermaid":
            st.markdown("""
            You approach the mermaid, but she tells you to go away!  
            You start running, slip on wet floor, and fall into the water!  
            You struggle to swim back but are exhausted.
            """)
            st.markdown("The next morning, a boat rescues you and takes you back home.")
            st.markdown("**Game Over:** You did not find the treasure but you returned home alive.")
            if st.button("Play Again"):
                reset_game()
            st.stop()
        else:
            st.session_state.step = "mermaid_hide"
    st.stop()

# --- MERMAID HIDING ---
if st.session_state.step == "mermaid_hide":
    st.markdown("""
    You hide as the lullaby voice becomes louder and sweeter.  
    Suddenly, the voice stops.  
    You open the door to find the mermaid gone and a mysterious arrow pointing backwards.  
    You decide to follow the arrow and sail west.
    """)
    if st.button("Set sail West"):
        st.session_state.direction = "west"
        st.session_state.step = "west_ship"
    st.stop()

# --- WEST SHIP STEP ---
if st.session_state.step == "west_ship":
    st.markdown("""
    Sailing west, you see another ship on the horizon flying a black flag.  
    It doesn't look wrecked.
    """)
    choice = st.radio(
        "What do you do?",
        ("Wait and see", "Attack the ship")
    )
    if st.button("Choose"):
        if choice == "Wait and see":
            st.markdown("""
            BOOM! The enemy ship fires first and attacks your ship.  
            Your ship is wrecked and you are captured.
            """)
            st.markdown("**Game Over:** You did not find the treasure and the pirates have imprisoned you.")
            if st.button("Play Again"):
                reset_game()
            st.stop()
        else:
            st.session_state.step = "attack_follow"
    st.stop()

# --- ATTACK OR FOLLOW STEP ---
if st.session_state.step == "attack_follow":
    choice = st.radio(
        "Enemy ship surrenders and moves east, revealing the treasure island and wrecked ship.\nWhat do you do?",
        ("Go to the wrecked ship", "Follow the enemy ship")
    )
    if st.button("Choose"):
        if choice == "Go to the wrecked ship":
            st.markdown("""
            You sail to the wrecked ship but it's empty!  
            The enemies have already taken the treasure.
            """)
            st.markdown("**Game Over:** You found the treasure island but no treasure. You return home alive.")
            if st.button("Play Again"):
                reset_game()
            st.stop()
        else:
            st.session_state.step = "final_battle"
    st.stop()

# --- FINAL BATTLE & TREASURE ---
if st.session_state.step == "final_battle":
    st.markdown("""
    You prepare your cannon and fire warning shots.  
    The enemy pirates flee their ship abandoning the treasure!
    """)
    if st.button("Board the ship"):
        st.markdown("""
        You board the enemy ship and open a crate filled with treasure!  
        **CONGRATULATIONS! YOU HAVE FOUND THE TREASURE!** 🎉🏆
        """)
        st.markdown("""
        You return home a legend, your family prospers and generations thank you for your bravery!  
        **THE END**
        """)
        if st.button("Play Again"):
            reset_game()
        st.stop()

# --- GAME OVER ---
if st.session_state.step == "game_over":
    st.markdown(st.session_state.game_over_reason)
    if st.button("Play Again"):
        reset_game()
    st.stop()
