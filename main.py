from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_AQUI")

def testar_chatgpt():
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Olá, você está funcionando?"}
        ]
    )
    print(resposta.choices[0].message["content"])

if __name__ == "__main__":
    testar_chatgpt()
