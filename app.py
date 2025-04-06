import ollama  # Ajoutez en haut du fichier

   def chat(message):
       response = ollama.generate(
           model="mistral",
           prompt=f"Tu es Asra. Parle comme [Votre Prénom]. Réponds à : {message}"
       )
       return response["text"]
