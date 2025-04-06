import gradio as gr

   def chat(message):
       message = message.lower()
       if "salut" in message:
           return "Yo ! Comment tu vas ?"
       elif "ça va" in message:
           return "Tranquille, et toi ?"
       elif "aide" in message:
           return "Je peux te conseiller sur : projets, tech, vie perso. Demande !"
       elif "merci" in message:
           return "Avec plaisir bro !"
       else:
           return "Je suis Asra, ton double IA. Pose-moi une question précise."

   gr.Interface(fn=chat, inputs="text", outputs="text").launch()
