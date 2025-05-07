import streamlit as st
import random

st.set_page_config(page_title="Bliepie Robot", page_icon="🤖")

# Custom CSS
st.markdown("""
    <style>
    body { background-color: #f3f0ff; }
    .stApp { background-color: #f3f0ff; }
    .zoeki {
        background-color: #e0d9ff;
        padding: 1em;
        border-radius: 10px;
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Avatar centreren binnen de middelste kolom
    inner_col1, inner_col2, inner_col3 = st.columns([1, 2, 1])
    with inner_col2:
        st.image("images/avatar_bliepie.png", width=150)

    st.markdown("<h2 style='text-align: center;'>🤖 Bliepie Robot</h2>", unsafe_allow_html=True)
    st.markdown('<div class="zoeki" style="text-align: center;"><strong>Bliep bliep! Ik zoek een leuke serie voor jou uit:</strong></div>', unsafe_allow_html=True)
    
    knop = st.button("Laat mij een serie kiezen!")

    if knop:
        keuze = random.choice([
            {"titel": "Het Huis Anubis", "beschrijving": "Tieners ontdekken geheimen in een oud internaat. Spannend en mysterieus!", "platform": "Videoland"},
            {"titel": "The Worst Witch", "beschrijving": "Een gewoon meisje leert magie op een heksenschool. Vol humor en toverspreuken!", "platform": "Netflix"},
            {"titel": "The Bureau of Magical Things", "beschrijving": "Een meisje krijgt magische krachten en ontdekt een verborgen wereld.", "platform": "Netflix / Viaplay"},
            {"titel": "Carmen Sandiego", "beschrijving": "Slimme dief reist de wereld rond en steelt van slechteriken. Spannend en leerzaam!", "platform": "Netflix"},
            {"titel": "Het Klokhuis", "beschrijving": "Elke dag een ander onderwerp uitgelegd op een grappige en leerzame manier.", "platform": "NPO Start"},
            {"titel": "Harry Potter", "beschrijving": "Magie, avontuur en vriendschap op Zweinstein.", "platform": "HBO Max"},
            {"titel": "The Thundermans", "beschrijving": "Een familie vol superhelden met puberproblemen.", "platform": "Netflix"},
            {"titel": "Henry Danger", "beschrijving": "Een jongen wordt de sidekick van een superheld.", "platform": "Netflix"},
            {"titel": "Meisje Jamilla", "beschrijving": "YouTuber die spannende avonturen beleeft.", "platform": "Videoland"},
            {"titel": "Juf Braaksel", "beschrijving": "Een strenge juf met een geheimzinnig verleden.", "platform": "Zapp / NPO Start"},
            {"titel": "Spangas", "beschrijving": "Het dagelijks leven van scholieren met veel drama en humor.", "platform": "NPO Start"},
            {"titel": "Checkpoint", "beschrijving": "Stoere experimenten en testen: wat werkt en wat niet?", "platform": "NPO Zapp"},
            {"titel": "Zapp Detective", "beschrijving": "Interactief raadselprogramma waarin je zelf de dader zoekt.", "platform": "NPO Zapp"},
            {"titel": "W.I.T.C.H.", "beschrijving": "Vijf meisjes ontdekken dat ze magische krachten hebben en moeten een andere wereld beschermen.", "platform": "Disney+"},
            {"titel": "Winx Club", "beschrijving": "Magische meiden op een sprookjesschool beleven avonturen en gevechten.", "platform": "Netflix"},
        ])
        st.markdown(f"""
            <div style="background-color: #d4edda; color: #155724; padding: 1em; border-radius: 10px; text-align: center;">
                <strong>{keuze['titel']}</strong> – {keuze['beschrijving']}<br><br>📺 Te zien op: {keuze['platform']}
            </div>
        """, unsafe_allow_html=True)
