import gradio as gr
from together import Together

client = Together(api_key="aa93be1f6064e39a5f54a340184e6629be29edd7cc6497a86c83ec395b44b46c")

def chat_with_gpt(history, user_message):
    if history is None:
        history = []
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3-70b-chat-hf",
            messages=messages,
            stream=True
        )
        bot_reply = ''.join([chunk.choices[0].delta.content or "" for chunk in response])
    except Exception as e:
        bot_reply = f"Error: {e}"

    history.append((user_message, bot_reply))
    return history, ""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type your message and press Enter", show_label=False)
    
    def submit(user_message, history):
        return chat_with_gpt(history, user_message)

    user_input.submit(submit, inputs=[user_input, chatbot], outputs=[chatbot, user_input])

demo.launch()