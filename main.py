import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import json

# Fonction pour charger une image à partir d'une URL
def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Fonction pour obtenir l'adresse IP publique via un service tiers
def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json().get("ip", "IP inconnue")
    except requests.RequestException:
        return "Erreur lors de la récupération de l'IP"

# Fonction pour enregistrer les messages dans un fichier texte
def save_to_txt(name, email, message, ip):
    with open("contacts.txt", "a") as file:
        file.write(f"Nom: {name}\nEmail: {email}\nMessage: {message}\nIP: {ip}\n\n")

# Fonction pour afficher les messages enregistrés
def display_messages():
    try:
        with open("contacts.txt", "r") as file:
            messages = file.read()
        st.text_area("Messages enregistrés", messages, height=300)
    except FileNotFoundError:
        st.write("Aucun message trouvé.")

# Chargement des images
logo = load_image_from_url("https://g.top4top.io/p_3152gg9qo0.jpg")
header_image = load_image_from_url("https://j.top4top.io/p_3152e1dds3.jpeg")
image_secure = load_image_from_url("https://i.top4top.io/p_3152ce61q2.png")
image_optimize = load_image_from_url("https://k.top4top.io/p_3152sec7c4.jpeg")
image_legal = load_image_from_url("https://h.top4top.io/p_3152nmkk21.jpeg")

# Configuration de la page
st.set_page_config(page_title="Organisation de Réseaux de Vente de Hashish premium", 
                   page_icon="https://g.top4top.io/p_3152gg9qo0.jpg", 
                   layout="centered")

# Ajout des meta tags pour SEO et réseaux sociaux
st.markdown("""
    <meta name="description" content="Service complet pour organiser et sécuriser votre réseau de distribution de hashish premium.">
    <meta name="keywords" content="hashish, CBD, réseau de vente, distribution, sécurité, optimisation logistique">
    <meta property="og:title" content="Organisation de Réseaux de Vente de Hashish premium">
    <meta property="og:description" content="Nous offrons un service complet pour organiser et sécuriser votre réseau de distribution de hashish.">
    <meta property="og:image" content="https://g.top4top.io/p_3152gg9qo0.jpg">
    <meta property="og:url" content="https://orgaweedze.onrender.com/">
    <meta name="twitter:card" content="summary_large_image">
    <meta property="twitter:image" content="https://g.top4top.io/p_3152gg9qo0.jpg">
    <meta property="twitter:title" content="Organisation de Réseaux de Vente de Hashish premium">
    <meta property="twitter:description" content="Service complet pour organiser et sécuriser votre réseau de distribution de hashish.">
""", unsafe_allow_html=True)

# Ajout de CSS personnalisé pour le style
st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    .header {
        font-size: 36px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
    }
    .subheader {
        font-size: 22px;
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
        color: #ff0000;
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

# Page principale
def main_page():
    # Affichage du logo et de l'en-tête
    st.image(logo, use_column_width=True, width=150)
    st.markdown('<h1 class="header">Organisation et Sécurisation des Réseaux de Vente de Hashish premium</h1>', unsafe_allow_html=True)
    st.image(header_image, use_column_width=True)

    # Description du service
    st.markdown("""
    <p class="description">
    Nous offrons un service complet pour organiser et sécuriser votre réseau de distribution de hashish.
    Que vous soyez un nouveau venu ou un acteur établi sur le marché, nous vous aidons à structurer vos opérations,
    à optimiser vos routes de livraison, et à garantir une sécurité optimale au niveau des risques judiciaires..
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
                # Ajouter JavaScript pour obtenir l'IP du client
                st.markdown("""
                <script>
                async function sendIP() {
                    const response = await fetch('https://api.ipify.org?format=json');
                    const data = await response.json();
                    const ip = data.ip;
                    const form = document.querySelector('form');
                    const ipInput = document.createElement('input');
                    ipInput.type = 'hidden';
                    ipInput.name = 'ip';
                    ipInput.value = ip;
                    form.appendChild(ipInput);
                    form.submit();
                }
                sendIP();
                </script>
                """, unsafe_allow_html=True)
                st.experimental_rerun()  # Recharger la page après l'exécution du script
            else:
                st.error("Veuillez remplir tous les champs.")

    # Pied de page
    st.markdown("""
    <p class="footer">
    © 2024 - Organisation des Réseaux de Vente de Hashish premium. Tous droits réservés.
    </p>
    """, unsafe_allow_html=True)

# Page protégée pour consulter les messages
def admin_page():
    password = st.text_input("Mot de passe", type="password")
    if password == "trkntrkn":
        st.title("Messages enregistrés")
        display_messages()
    else:
        st.warning("Mot de passe incorrect.")

# Sélection de la page à afficher
PAGES = {
    "Page principale": main_page,
    "Administration": admin_page
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
