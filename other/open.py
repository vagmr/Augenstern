import gradio as gr
import requests
import secrets

# 生成一个安全的密钥
secret_key = secrets.token_hex(16)

def predict(text):
    try:
        r = requests.post(
            "https://api.ai.chat/v1/gpt3.5",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {secret_key}"
            },
            json={
                "input_text": text,
                "model_id": "test",
                "temperature": 0.9,
                "num_tokens_to_produce": 50
            }
        )
        return r.json()["output_text"]
    except Exception as e:
        return str(e)

interface = gr.Interface(fn=predict,
                         inputs=gr.inputs.Textbox(label="请输入您的问题"),
                         outputs="text",
                         title="AI 机器人",
                         auth=True,  # 启用用户验证功能
                         share=False,
                         )

# 在 Gradio 界面上启动公共链接和用户验证功能
if __name__ == "__main__":
    interface.launch(share=True, auth=True, server_name="my_interface", server_port=7878, password=secret_key)
