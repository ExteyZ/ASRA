import gradio as gr
import ollama  # Importe la bibliothèque Ollama

def chat(message):
    # Personnalisez ce prompt pour qu'Asra vous ressemble
    prompt = f"""
Tu es Asra, le double IA de MArio.
Ton style : [décrivez comment vous parlez, ex: "réaliste et sans filtre"].
Exemple de réponse typique : "c'est la vie frére".
Message à traiter : "{message}"
"""

    # Envoie la requête à Ollama
    response = ollama.generate(
        model="mistral",  # Nom du modèle Ollama
        prompt=prompt
    )

    return response["response"]  # Correction ici aussi pour le bon champ

# Crée l'interface web
gr.Interface(fn=chat, inputs="text", outputs="text").launch()
