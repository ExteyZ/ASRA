import gradio as gr
   import ollama  # Cette ligne importe la bibliothèque Ollama

   def chat(message):
       # Personnalisez ce prompt pour qu'Asra vous ressemble
       prompt = f"""
       Tu es Asra, mon double IA. 
       Ton style : [ajoutez ici comment vous parlez, ex: "direct et amical"].
       Réponds à ce message comme je le ferais : "{message}"
       """
       
       # Envoie la requête à Ollama
       response = ollama.generate(
           model="mistral",  # Nom du modèle Ollama
           prompt=prompt
       )
       return response["text"]

   # Crée l'interface web
   gr.Interface(fn=chat, inputs="text", outputs="text").launch()
