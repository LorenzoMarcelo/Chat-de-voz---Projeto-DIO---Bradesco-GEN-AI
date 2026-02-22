# 🚀 CHATVOZ – Integração com a API da OpenAI  
Projeto desenvolvido como parte do desafio da DIO, demonstrando como integrar Python com a API da OpenAI para enviar uma mensagem a um modelo de linguagem e exibir a resposta no terminal.

---

## 📌 Objetivo do Projeto
O objetivo é criar um script simples em Python capaz de:

- Conectar-se à API da OpenAI  
- Enviar uma mensagem para um modelo de linguagem  
- Receber e exibir a resposta no terminal  

Este projeto serve como base para aplicações maiores, como chatbots, assistentes virtuais, automações e muito mais.

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Virtualenv**
- **Biblioteca `openai`**
- **VS Code / Terminal**

---

## 📁 Estrutura do Projeto

CHATVOZ/
│── main.py

from openai import OpenAI

client = OpenAI(api_key="client = OpenAI(api_key="SUA_CHAVE_AQUI")")

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
│── requirements.txt
│── README.md
└── venv/
