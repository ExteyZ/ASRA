import gradio as gr

   def chat(message):
       return f"Asra répond : '{message}' (mode test)"

   gr.Interface(chat, inputs="text", outputs="text").launch()
