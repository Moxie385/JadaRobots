import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(page_title="Sompje – Tafeltovenaar", page_icon="✨")

# Custom CSS
st.markdown("""
    <style>
    body { background-color: #fff8ec; }
    .stApp { background-color: #fff8ec; }
    .magie {
        background-color: #ffeac2;
        padding: 1em;
        border-radius: 10px;
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    inner_col1, inner_col2, inner_col3 = st.columns([1, 2, 1])
    with inner_col2:
        st.image("images/avatar_sompje.png", width=150)

    st.markdown("<h2 style='text-align: center;'>✨ Sompje – Tafeltovenaar</h2>", unsafe_allow_html=True)
    st.markdown('<div class="magie" style="text-align: center;">Welkom bij Sompje! Kies een oefenmodus en tover met tafels!</div>', unsafe_allow_html=True)

    mode = st.radio("Kies een oefenmodus:", ["Zonder tijd", "Op tijd (5 min)"], horizontal=True)

    # Session state setup
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    if "start_clicked" not in st.session_state:
        st.session_state.start_clicked = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "log" not in st.session_state:
        st.session_state.log = []
    if "current" not in st.session_state:
        st.session_state.current = (random.randint(1,10), random.randint(1,10))
    if "input_key" not in st.session_state:
        st.session_state.input_key = random.randint(0, 1000000)

    def new_question():
        st.session_state.current = (random.randint(1,10), random.randint(1,10))
        st.session_state.input_key = random.randint(0, 1000000)

    a, b = st.session_state.current

    if mode == "Zonder tijd":
        antwoord = st.text_input(f"Wat is {a} x {b}?", key=st.session_state.input_key)

        if antwoord:
            try:
                antwoord_int = int(antwoord)
                if antwoord_int == a * b:
                    st.success("Goed gedaan, tovenaar! ✨")
                    st.session_state.score += 1
                    st.session_state.log.append((f"{a}x{b}", "✔"))
                    st.button("Nieuwe som", on_click=new_question)
                else:
                    st.error("Helaas, probeer het opnieuw!")
            except ValueError:
                st.warning("Typ een getal!")

        if len(st.session_state.log) > 0:
            df = pd.DataFrame(st.session_state.log, columns=["Som", "Resultaat"])
            st.write("Je voortgang:")
            st.dataframe(df)
            st.bar_chart(df["Resultaat"].value_counts())

    elif mode == "Op tijd (5 min)":
        if not st.session_state.start_clicked:
            if st.button("Start!"):
                st.session_state.start_time = time.time()
                st.session_state.start_clicked = True

        if st.session_state.start_clicked:
            elapsed = time.time() - st.session_state.start_time
            remaining = 300 - elapsed
            st.info(f"Tijd over: {int(remaining)} sec")

            antwoord = st.text_input(f"Wat is {a} x {b}?", key=st.session_state.input_key)

            if st.button("Volgende"):
                st.session_state.log.append((f"{a}x{b}", antwoord))
                new_question()

            if remaining <= 0:
                if len(st.session_state.log) == 0:
                    st.warning("Er zijn nog geen sommen gemaakt!")
                else:
                    st.warning("Tijd is op! Hier is je resultaat:")
                    resultaat_lijst = []
                    for som, gegeven in st.session_state.log:
                        correct = eval(som.replace("x", "*"))
                        try:
                            gegeven_int = int(gegeven)
                            goed = (gegeven_int == correct)
                        except:
                            goed = False
                        resultaat_lijst.append((som, gegeven, correct, "✔" if goed else "✘"))

                    df = pd.DataFrame(resultaat_lijst, columns=["Som", "Jouw antwoord", "Correct", "Resultaat"])
                    score = df["Resultaat"].value_counts().get("✔", 0)
                    st.success(f"Je had {score} goed van de {len(df)} sommen!")

                    st.dataframe(df)
                    st.bar_chart(df["Resultaat"].value_counts())
