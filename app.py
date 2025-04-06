import gradio as gr
   import ollama

   def chat(message):
       response = ollama.generate(model="mistral", prompt=f"Tu es Asra. {message}")
       return response["text"]

   gr.Interface(chat, inputs="textbox", outputs="textbox").launch(server_name="0.0.0.0")
