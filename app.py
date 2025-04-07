import gradio as gr
import ollama  # Importe la bibliothèque Ollama

def chat(message):
    # Personnalisez ce prompt pour qu'Asra vous ressemble
    prompt = 

    # Envoie la requête à Ollama
    response = ollama.generate(
        model="mistral",  # Nom du modèle Ollama
        prompt=prompt
    )

    return response["response"]  # Correction ici aussi pour le bon champ

# Crée l'interface web
gr.Interface(fn=chat, inputs="text", outputs="text").launch()
