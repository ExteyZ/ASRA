import gradio as gr
import ollama
import json
from datetime import datetime

# ----------------------------
# PARTIE 1 : OPTIMISATION VITESSE
# ----------------------------
MODÈLE_RAPIDE = "tinyllama"  # Modèle léger (1GB)
CONFIG_RAPIDITÉ = {
    "num_predict": 100,  # Réponses courtes
    "temperature": 0.7   # Équilibre créativité/cohérence
}

# ----------------------------
# PARTIE 2 : MÉMOIRE DES CONVERSATIONS
# ----------------------------
def charger_mémoire():
    try:
        with open("asra_memory.json", "r") as f:
            return json.load(f)
    except:
        return []

def sauvegarder_mémoire(mémoire):
    with open("asra_memory.json", "w") as f:
        json.dump(mémoire, f)

# ----------------------------
# PARTIE 3 : PERSONNALISATION
# ----------------------------
def créer_prompt(message, mémoire):
    # Personnalisez CI-DESSOUS selon votre style :
    return f"""
    [TON PROFIL]
    - Prénom : Pierre
    - Style : "Détendu tech avec des 'frr' et des refs jeux vidéo"
    - Tics de langage : "tu captes ?", "je te jure"
    - Centres d'intérêt : Python, One Piece, musculation
    - Exemple de phrase : "C'est comme quand Goku..."

    [HISTORIQUE] (3 derniers messages) :
    {mémoire[-3:]}

    [MESSAGE ACTUEL]
    {message}

    [CONSIGNES]
    - Réponds EXACTEMENT comme moi
    - Sois concis (max 2 phrases)
    """

# ----------------------------
# FONCTION PRINCIPALE
# ----------------------------
def chat(message):
    # Charge la mémoire
    mémoire = charger_mémoire()
    
    # Génère le prompt personnalisé
    prompt = créer_prompt(message, mémoire)
    
    # Appel à Ollama (optimisé pour la vitesse)
    response = ollama.generate(
        model=MODÈLE_RAPIDE,
        prompt=prompt,
        options=CONFIG_RAPIDITÉ
    )
    
    # Sauvegarde la conversation
    mémoire.append({
        "date": str(datetime.now()),
        "user": message,
        "asra": response["text"]
    })
    sauvegarder_mémoire(mémoire)
    
    return response["text"]

# ----------------------------
# INTERFACE
# ----------------------------
interface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="Parle à Asra", placeholder="Dis quelque chose..."),
    outputs=gr.Textbox(label="Asra"),
    title="Asra - Mon Double IA",
    theme="soft",
    allow_flagging="never"
)

interface.launch(server_port=7860, server_name="0.0.0.0")
