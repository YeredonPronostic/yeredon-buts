import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Yèrèdon Média - Calculateur de Pronostics", page_icon="⚽", layout="centered")

st.title("⚽ Yèrèdon Média - Système Buts")
st.write("Bienvenue sur l'outil d'aide à la décision pour vos pronostics sportifs.")

st.markdown("---")

# Formulaire d'entrée des données
st.subheader("📊 Analyser un nouveau match")

col1, col2 = st.columns(2)
with col1:
    equipe_dom = st.text_input("Équipe Domicile", value="France")
    buts_dom = st.slider("Buts marqués Dom (%)", min_value=0, max_value=100, value=85, step=5)

with col2:
    equipe_ext = st.text_input("Équipe Extérieur", value="Maroc")
    buts_ext = st.slider("Buts encaissés Ext (%)", min_value=0, max_value=100, value=75, step=5)

st.markdown("---")

# Calcul de la moyenne et affichage du verdict
if equipe_dom and equipe_ext:
    moyenne = (buts_dom + buts_ext) / 2
    st.metric(label=f"Moyenne calculée pour {equipe_dom} vs {equipe_ext}", value=f"{moyenne} %")
    
    if moyenne >= 75:
        st.success("✅ TICKET VALIDÉ")
        st.balloons()
    elif moyenne >= 60:
        st.warning("⚠️ MISE MODÉRÉE")
    else:
        st.error("❌ MATCH REJETÉ")
