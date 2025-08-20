import streamlit as st

st.set_page_config(page_title="Treasure Island Adventure", layout="centered")

# ASCII art always on top
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

show_ascii_art()

st.title("Welcome to Treasure Island! 🏴‍☠️")

# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = "start"
if "direction" not in st.session_state:
    st.session_state.direction = ""

def reset_game():
    st.session_state.step = "start"
    st.session_state.direction = ""

def proceed(step):
    st.session_state.step = step

# --- START STEP ---
if st.session_state.step == "start":
    st.markdown("""
    You have decided to set sail towards a small undiscovered island to find the treasure of Jack Sparrow!

    The problem is that the island is undiscovered, hence you don't know which direction to go in.

    What do you do?
    """)
    if st.button("Look at the map 🗺️"):
        proceed("map")
    if st.button("Go North 🚢"):
        st.session_state.direction = "north"
        proceed("sailing")
    if st.button("Turn back 🏠"):
        proceed("game_over_turn_back")

# --- MAP STEP ---
if st.session_state.step == "map":
    st.markdown("""
    It is an old exquisite piece of paper.

    The dock you are standing on is at the bottom.

    You see three drawings on the map:
    - Fire symbol in the north 🔥
    - A dolphin's drawing in the east 🐬
    - A drawing of a ship wreckage in the west 🚢

    Where do you go?
    """)
    if st.button("Go North 🔥"):
        st.session_state.direction = "north"
        proceed("sailing")
    if st.button("Go East 🐬"):
        st.session_state.direction = "east"
        proceed("sailing")
    if st.button("Go West 🚢"):
        st.session_state.direction = "west"
        proceed("sailing")

# --- SAILING STEP ---
if st.session_state.step == "sailing":
    st.markdown(f"You sailed straight towards the **{st.session_state.direction}**! ⛵️")
    st.markdown("""
    You go to sleep and wake up the next day.  
    It is an unremarkable day.  
    You catch some fish, cook some food, look at the sunset, and then you go to sleep.  
    This goes on for 2 days.
    """)
    if st.button("Continue Sailing"):
        if st.session_state.direction == "north":
            proceed("volcano")
        elif st.session_state.direction == "east":
            proceed("east_mermaid")
        else:
            proceed("west_ship")

# --- NORTH VOLCANO STEP ---
if st.session_state.step == "volcano":
    st.markdown("""
    You fell asleep dreaming of beautiful mermaids.  

    Suddenly, you hear a **BOOOM!**  

    You rush out and see a volcano erupting right ahead!  

    You must steer away quickly!
    """)
    if st.button("Turn Right (East)"):
        st.session_state.direction = "east"
        proceed("sailing_after_volcano")
    if st.button("Turn Left (West)"):
        st.session_state.direction = "west"
        proceed("sailing_after_volcano")

# --- AFTER VOLCANO SAILING ---
if st.session_state.step == "sailing_after_volcano":
    st.markdown(f"PHEW! You turned towards the **{st.session_state.direction}** just in time and avoided the volcano ash and tsunami.")
    if st.button("Continue Sailing"):
        if st.session_state.direction == "east":
            proceed("east_mermaid")
        else:
            proceed("west_ship")

# --- EAST MERMAID STEP ---
if st.session_state.step == "east_mermaid":
    st.markdown("""
    You are asleep and you hear a gentle voice, a lullaby your mother used to sing.
    """)
    if st.button("Go out on deck to check who's there"):
        proceed("mermaid_encounter")
    if st.button("Hide and lock the door"):
        proceed("mermaid_hide")

# --- MERMAID ENCOUNTER ---
if st.session_state.step == "mermaid_encounter":
    st.markdown("You find a mermaid waiting for you. What do you do?")
    if st.button("Go to the mermaid"):
        st.markdown("""
        You approach the mermaid, but she tells you to go away!  
        You start running, slip on wet floor, and fall into the water!  
        You struggle to swim back but are exhausted.
        """)
        st.markdown("The next morning, a boat rescues you and takes you back home.")
        st.markdown("**Game Over:** You did not find the treasure but you returned home alive.")
        if st.button("Play Again"):
            reset_game()
    if st.button("Hide and go back inside"):
        proceed("mermaid_hide")

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
        proceed("west_ship")

# --- WEST SHIP STEP ---
if st.session_state.step == "west_ship":
    st.markdown("""
    Sailing west, you see another ship on the horizon flying a black flag.  

    It doesn't look wrecked.
    """)
    if st.button("Wait and see"):
        st.markdown("""
        BOOM! The enemy ship fires first and attacks your ship.  

        Your ship is wrecked and you are captured.
        """)
        st.markdown("**Game Over:** You did not find the treasure and the pirates have imprisoned you.")
        if st.button("Play Again"):
            reset_game()
    if st.button("Attack the ship"):
        proceed("attack_follow")

# --- ATTACK OR FOLLOW STEP ---
if st.session_state.step == "attack_follow":
    st.markdown("""
    Enemy ship surrenders and moves east, revealing the treasure island and wrecked ship.

    What do you do?
    """)
    if st.button("Go to the wrecked ship"):
        st.markdown("""
        You sail to the wrecked ship but it's empty!  

        The enemies have already taken the treasure.
        """)
        st.markdown("**Game Over:** You found the treasure island but no treasure. You return home alive.")
        if st.button("Play Again"):
            reset_game()
    if st.button("Follow the enemy ship"):
        proceed("final_battle")

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

# --- GAME OVER TURN BACK ---
if st.session_state.step == "game_over_turn_back":
    st.markdown("""
    You chose to turn back and go home, "adventures are for fools" you said.

    The End: You did not find the treasure but you are alive.
    """)
    if st.button("Play Again"):
        reset_game()
