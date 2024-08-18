import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from streamlit_js_eval import streamlit_js_eval

# Fonction pour charger une image à partir d'une URL
def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Fonction pour enregistrer les messages dans un fichier texte (Secret File)
def save_to_txt(name, email, message, ip):
    try:
        with open("/etc/secrets/contacts.txt", "a") as file:
            file.write(f"Nom: {name}\nEmail: {email}\nMessage: {message}\nIP: {ip}\n\n")
    except Exception as e:
        st.error("Erreur lors de l'enregistrement du message. Veuillez vérifier les permissions ou la configuration.")

# Fonction pour afficher les messages enregistrés (Secret File)
def display_messages():
    try:
        with open("/etc/secrets/contacts.txt", "r") as file:
            messages = file.read()
        st.text_area("Messages enregistrés", messages, height=300)
    except FileNotFoundError:
        st.write("Aucun message trouvé.")
    except Exception as e:
        st.error("Erreur lors de la lecture du fichier. Veuillez vérifier les permissions ou la configuration.")

# Charger les images
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
        margin-bottom: 20px;
        border: 3px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        transition: transform 0.3s;
    }
    .header:hover {
        transform: scale(1.05);
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #333333;
        line-height: 1.6;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 50px;
    }
    .subheader {
        font-size: 22px;
        color: #666666;
        text-align: center;
        margin-bottom: 50px;
    }
    .service-section {
        text-align: center;
        padding: 20px;
        margin: 20px 0;
        border-radius: 15px;
        background-color: #ffffff;
        transition: box-shadow 0.3s, transform 0.3s;
    }
    .service-section:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        transform: scale(1.02);
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
        transition: background-color 0.3s;
    }
    .btn:hover {
        background-color: #45a049;
    }
    .contact-form {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 50px;
        transition: box-shadow 0.3s;
    }
    .contact-form:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
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
    à optimiser vos routes de livraison, et à garantir une sécurité optimale au niveau des risques judiciaires.
    </p>
    """, unsafe_allow_html=True)

    # Sections des services
    st.subheader("Nos Services")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="service-section">', unsafe_allow_html=True)
        st.image(image_secure, use_column_width=True)
        st.markdown("### Sécurisation des transactions")
        st.write("Nous assurons la sécurité de toutes vos transactions de hashish grâce à des protocoles avancés.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="service-section">', unsafe_allow_html=True)
        st.image(image_optimize, use_column_width=True)
        st.markdown("### Optimisation logistique")
        st.write("Nous optimisons vos routes de livraison pour garantir une efficacité maximale.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="service-section">', unsafe_allow_html=True)
        st.image(image_legal, use_column_width=True)
        st.markdown("### Évitement des soucis judiciaires")
        st.write("Nous vous aidons à respecter les réglementations en vigueur sur la vente de hashish.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Section contact
    st.subheader("Contactez-nous")

    # Utilisation de streamlit_js_eval pour obtenir l'IP du client
    ip_address = streamlit_js_eval(js_expressions="fetch('https://api.ipify.org?format=json').then(res => res.json()).then(data => data.ip);")

    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    with st.form(key="contact_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Envoyer")

        if submit_button:
            if name and email and message:
                save_to_txt(name, email, message, ip_address)
                st.success(f"Merci {name}, votre message a bien été enregistré. Nous vous contacterons sous peu.")
            else:
                st.error("Veuillez remplir tous les champs.")
    st.markdown('</div>', unsafe_allow_html=True)

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

def sidebar_about():
    st.sidebar.markdown("## À propos")
    st.sidebar.markdown("""
        **Nom :** Trhacknon  
        **Application :** Organisation de Réseaux de Vente de Hashish premium  
        **Version :** 1.0  
    """)

def main():
    st.sidebar.title("Navigation")
    sidebar_about()  # Appeler la fonction pour afficher l'info "À propos"
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
