import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mon projet")

fichier = st.file_uploader("Sélectionner un fihcier au format CSV", type="csv")

if fichier is not None :
    df = pd.read_csv(fichier)

    st.subheader("Prévisualisation des datas")
    st.write(df.head())
    #st.dataframe(df)
    #st.dataframe(df.style.highlight_max(axis=0))
    #st.dataframe(df.style.highlight_min(axis=0))

    st.subheader("Résumé des statistiques")
    st.write(df.describe)

    st.subheader("Filter les données")
    colonnes = df.columns.tolist()
    selected_colonnes = st.selectbox("Sélectionner une colonne à filtrer", colonnes)

    valeurs_uniques = df[selected_colonnes].unique() #permet de supprimer les doublons
    selected_valeurs = st.selectbox("Sélectionner une valeur à filtrer", valeurs_uniques)

    st.subheader("données filtrées")
    df_filtre = df[df[selected_colonnes] == selected_valeurs]
    st.write(df_filtre)

    st.subheader("Graphique")
    x_col = st.selectbox("Selectionner votre axe X", colonnes)
    y_col = st.selectbox("Selectionner votre axe Y", colonnes)

    if st.button("Générer le graphique"): 
        st.line_chart(df_filtre.set_index(x_col)[y_col])

else:
    st.write("en attente de fichier")