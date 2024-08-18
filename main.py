import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Fonction pour charger une image à partir d'une URL
def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Chargement des images à partir des URLs
logo = load_image_from_url("https://g.top4top.io/p_3152gg9qo0.jpg")
header_image = load_image_from_url("https://j.top4top.io/p_3152e1dds3.jpeg")
image_secure = load_image_from_url("https://i.top4top.io/p_3152ce61q2.png")
image_optimize = load_image_from_url("https://k.top4top.io/p_3152sec7c4.jpeg")
image_legal = load_image_from_url("https://h.top4top.io/p_3152nmkk21.jpeg")

# Configuration de la page
st.set_page_config(page_title="Organisation de Réseaux de Vente de CBD", page_icon="🌿", layout="centered")

# Ajout de CSS personnalisé pour le style
st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    .header {
        font-size: 48px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
    }
    .subheader {
        font-size: 24px;
        color: #666666;
        text-align: center;
        margin-bottom: 50px;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #4CAF50;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #888888;
        margin-top: 50px;
    }
    .btn {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Affichage du logo et de l'en-tête
st.image(logo, width=150)
st.markdown('<h1 class="header">Organisation et Sécurisation des Réseaux de Vente de Hashish premium</h1>', unsafe_allow_html=True)
st.image(header_image, use_column_width=True)

# Description du service
st.markdown("""
<p class="description">
Nous offrons un service complet pour organiser et sécuriser votre réseau de distribution de hashish.
Que vous soyez un nouveau venu ou un acteur établi sur le marché, nous vous aidons à structurer vos opérations,
à optimiser vos routes de livraison, et à garantir une conformité légale optimale.
</p>
""", unsafe_allow_html=True)

# Sections des services
st.subheader("Nos Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_secure, use_column_width=True)
    st.markdown("### Sécurisation des transactions")
    st.write("Nous assurons la sécurité de toutes vos transactions de hashish grâce à des protocoles avancés.")

with col2:
    st.image(image_optimize, use_column_width=True)
    st.markdown("### Optimisation logistique")
    st.write("Nous optimisons vos routes de livraison pour garantir une efficacité maximale.")

with col3:
    st.image(image_legal, use_column_width=True)
    st.markdown("### Évitement des soucis judiciaires")
    st.write("Nous vous aidons à respecter les réglementations en vigueur sur la vente de hashish.")

# Section contact
st.subheader("Contactez-nous")

with st.form(key="contact_form"):
    name = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit_button = st.form_submit_button(label="Envoyer")

    if submit_button:
        if name and email and message:
            st.success(f"Merci {name}, votre message a bien été envoyé. Nous vous contacterons sous peu.")
        else:
            st.error("Veuillez remplir tous les champs.")

# Pied de page
st.markdown("""
<p class="footer">
© 2024 - Organisation des Réseaux de Vente de Hashish premium. Tous droits réservés.
</p>
""", unsafe_allow_html=True)
