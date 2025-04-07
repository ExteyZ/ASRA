import gradio as gr
   import ollama  # Importe la bibliothèque Ollama

   def chat(message):
       # Personnalisez ce prompt pour qu'Asra vous ressemble
       prompt = f"""
       Tu es Asra, le double IA de [Votre Prénom]. 
       Ton style : [décrivez comment vous parlez, ex: "direct et sarcastique"].
       Exemple de réponse typique : "[une phrase que vous dites souvent]".
       Message à traiter : "{message}"
       """
       
       # Envoie la requête à Ollama
       response = ollama.generate(
           model="mistral",  # Nom du modèle Ollama
           prompt=prompt
       )
       return response["text"]

   # Crée l'interface web
   gr.Interface(fn=chat, inputs="text", outputs="text").launch()
