#import streamlit as st 
#import random
#datei = open ("sprueche.txt")
#sprueche = datei.readlines ()

#st.write(sprueche[0].strip())

#spruch = random.choice(sprueche)

#st.write(spruch.strip())

import random
import streamlit as st

st.title("💬 Gerd-Ahr-Spruch-Generator")

# Sprüche laden (jede Zeile ein Spruch)
with open("sprueche.txt", "r", encoding="utf-8") as f:
    sprueche = [zeile.strip() for zeile in f if zeile.strip()]

neuer_spruch = st.text_input("Neuen Spruch hinzufügen")

if st.button("➕ Spruch speichern"):
    text = neuer_spruch.strip()
    if text:
        with open("sprueche.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        st.success("Gespeichert ✅ (Seite neu laden oder 'Nächster Spruch')")
    else:
        st.warning("Bitte erst einen Spruch eingeben 🙂")


if not sprueche:
    st.error("sprueche.txt ist leer oder nicht gefunden.")
    st.stop()

# aktuellen Spruch merken (damit er beim Klick wechselt)
if "spruch" not in st.session_state:
    st.session_state.spruch = random.choice(sprueche)

#st.write(st.session_state.spruch)

#st.markdown(
    #f"<h2 style='text-align: center; font-weight: bold;'>{st.session_state.spruch}</h2>",
    #unsafe_allow_html=True
#)

st.markdown(
    f"""
    <div style="
        font-size:34px;
        font-weight:600;
        text-align:center;
        padding:40px;
        border-radius:20px;
        background-color:#1e1e1e;
        color:white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    ">
        “{st.session_state.spruch}”
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("➡️ Nächster Spruch"):
    neuer = random.choice(sprueche)

    # optional: nicht zweimal hintereinander derselbe
    if len(sprueche) > 1:
        while neuer == st.session_state.spruch:
            neuer = random.choice(sprueche)

    st.session_state.spruch = neuer
    st.rerun()
