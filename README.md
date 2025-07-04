# Chat Game - Chatbot de Jogos para WhatsApp

Um chatbot desenvolvido pela turma Educafro Tech que oferece jogos interativos via WhatsApp.

## 🎮 Jogos Disponíveis

1. **Jokenpô (Pedra, Papel, Tesoura)** - Jogue contra o bot
2. **Forca** - Adivinhe a palavra letra por letra
3. **Adivinhação** - Descubra o número secreto entre 1 e 100

## 📁 Estrutura do Projeto

```
chat-game/
├── src/
│   ├── games/
│   │   ├── __init__.py
│   │   ├── jokenpo.py          # Lógica do jogo Jokenpô
│   │   ├── forca.py            # Lógica do jogo da Forca
│   │   └── adivinhacao.py      # Lógica do jogo da Adivinhação
│   ├── utils/
│   │   └── whatsapp_client.py  # Cliente SIMULADO para envio de mensagens WhatsApp
│   └── main.py                 # Aplicação Flask e lógica principal do chatbot
├── test_webhook.py             # Script para testar o webhook localmente
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
└── LICENSE                     # Licença do projeto
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chat-game.git
cd chat-game
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando o Projeto

1. Inicie o servidor Flask:
```bash
python src/main.py
```

2. O servidor estará rodando em `http://127.0.0.1:5000`

3. Para testar os jogos, execute o script de teste:
```bash
python test_webhook.py
```

## 🌐 Endpoints da API

### GET /
- Retorna uma mensagem de boas-vindas

### POST /webhook
- Processa mensagens do WhatsApp
- Corpo da requisição:
```json
{
    "from": "5511999999999",
    "text": "oi"
}
```

## 🎯 Como Usar o Chatbot

1. Envie "oi" ou "menu" para ver os jogos disponíveis
2. Escolha um jogo digitando o número (1, 2, ou 3) ou o nome do jogo
3. Siga as instruções para cada jogo
4. Digite "menu" a qualquer momento para voltar ao menu principal

### Comandos dos Jogos

**Jokenpô:**
- Digite: "pedra", "papel" ou "tesoura"

**Forca:**
- Digite uma letra por vez para adivinhar a palavra

**Adivinhação:**
- Digite um número entre 1 e 100 para tentar acertar

## 🔧 Integração com WhatsApp Real

Este projeto usa um cliente simulado de WhatsApp. Para integração real, você pode usar:

- **Twilio API for WhatsApp**
- **WhatsApp Business API oficial**
- **Bibliotecas como pywhatkit** (para automação via WhatsApp Web)

Exemplo de configuração com pywhatkit está comentado no arquivo `whatsapp_client.py`.

## 🧪 Testes

Execute o script de teste para verificar se todos os jogos estão funcionando:

```bash
python test_webhook.py
```

Este script testa:
- Menu principal
- Jogo Jokenpô
- Jogo da Forca
- Jogo de Adivinhação

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** - Framework web
- **Requests** - Para requisições HTTP (nos testes)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

## 📞 Contato

Projeto desenvolvido pela turma **Educafro Tech**.

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!




python -m venv venv
.\venv\Scripts\activate
pip install Flask
python src/main.py

http://127.0.0.1:5000/



# Chatbot de Jogos para WhatsApp em Python

Este é um projeto desenvolvido para iniciantes em programação, com o objetivo de criar um chatbot interativo para WhatsApp que permite jogar Jokenpô, Forca e Adivinhação. O projeto utiliza Flask para a API web e simula a integração com o WhatsApp.

---

## Funcionalidades

* **Menu de Jogos:** O usuário pode digitar 'Oi' ou 'Menu' para ver a lista de jogos disponíveis.
* **Jokenpô:** Jogue Pedra, Papel ou Tesoura contra o bot.
* **Forca:** Adivinhe a palavra secreta chutando letras, com um número limitado de tentativas.
* **Adivinhação:** O bot pensa em um número e o usuário tenta adivinhar, recebendo dicas de "maior" ou "menor".

---

## Tecnologias Utilizadas

* **Python 3.8+:** Linguagem de programação principal.
* **Flask:** Microframework web para criar a API do chatbot.
* **Ngrok:** Ferramenta para expor o servidor local à internet (necessário para simular webhooks).

---

## Estrutura do Projeto

---

## Como Rodar o Projeto (Ambiente de Desenvolvimento)

Siga os passos abaixo para configurar e rodar o chatbot em sua máquina local.

### 1. Pré-requisitos

* Python 3.8 ou superior instalado.
* Visual Studio Code (ou seu editor de código preferido) instalado.
* Ngrok instalado e configurado (baixe em [ngrok.com/download](https://ngrok.com/download)).

### 2. Configuração do Ambiente

1.  **Clone o repositório (ou crie a estrutura de pastas manualmente):**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_SE_HOUVER>
    cd chatbot_jogos
    ```
    Ou crie a pasta `chatbot_jogos` e as subpastas `src/`, `src/games/`, `src/utils/`.

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    Se você estiver começando do zero, instale o Flask primeiro: `pip install Flask`.
    Depois de todas as aulas, você pode gerar o `requirements.txt` com `pip freeze > requirements.txt`.

### 3. Rodando o Chatbot

1.  **Inicie o servidor Flask:**
    Abra um terminal na pasta `chatbot_jogos` (com o ambiente virtual ativado) e execute:
    ```bash
    python src/main.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000/`.

2.  **Exponha o servidor local com Ngrok:**
    Abra **outro terminal** e execute:
    ```bash
    ngrok http 5000
    ```
    O Ngrok fornecerá um URL público (ex: `https://abcd1234.ngrok-free.app`). **Este será o URL do seu webhook para testes.**

### 4. Testando o Chatbot (Via Postman/cURL)

Como não estamos usando a API oficial do WhatsApp Business diretamente, vamos simular o envio de mensagens usando ferramentas como Postman ou `curl`.

Envie requisições **POST** para o **URL do Ngrok** (o que você obteve no passo anterior, seguido de `/webhook`), com o cabeçalho `Content-Type: application/json` e um corpo JSON no formato:

```json
{
    "from": "5511987654321",
    "text": "Sua Mensagem Aqui"
}
```
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://globalcards-inmetrics.postman.co/collection/9485476-ebed8ec1-252a-42ad-a13d-1b21f4ab9438?source=rip_markdown)

---

### **Materiais de Consulta e Referência**

Aqui estão alguns recursos úteis para os alunos:

**1. Python Básico:**

* **Documentação Oficial do Python:** Excelente para referência. [docs.python.org/pt-br/3/](https://docs.python.org/pt-br/3/)
* **Curso em Vídeo - Python (Gustavo Guanabara):** Um curso muito popular e didático em português no YouTube, ideal para iniciantes. [youtube.com/playlist?list=PLHz_ArekSsAt2RPLZSazS0VyQB_yQzXWV](https://www.youtube.com/playlist?list=PLHz_ArekSsAt2RPLZSazS0VyQB_yQzXWV)
* **Codecademy (Python 3):** Cursos interativos com exercícios práticos. [codecademy.com/learn/learn-python-3](https://www.codecademy.com/learn/learn-python-3)

**2. Flask (Web Framework):**

* **Documentação Oficial do Flask:** [flask.palletsprojects.com/en/latest/](https://flask.palletsprojects.com/en/latest/) (Começar com o Quickstart)
* **Tutoriais do Flask no Miguel Grinberg:** Uma série de tutoriais muito completos e bem explicados para construir aplicações Flask. [blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) (Pode ser um pouco avançado para iniciantes absolutos, mas excelente para aprofundamento.)

**3. APIs e Webhooks:**

* **O que são APIs? Um Guia para Iniciantes:** Artigos e vídeos que explicam o conceito de APIs de forma simples. Pesquise por "what is an API for beginners".
* **Webhook.site:** Uma ferramenta online para testar webhooks e ver as requisições que chegam ao seu URL. Útil para depuração. [webhook.site](https://webhook.site/)

**4. Ngrok:**

* **Documentação Oficial do Ngrok:** Para instalação e uso básico. [ngrok.com/docs](https://ngrok.com/docs)

**5. Git e GitHub (Opcional, mas Recomendado):**

* **Guia do GitHub para Iniciantes:** Se você quiser versionar o código. [guides.github.com/activities/hello-world/](https://guides.github.com/activities/hello-world/)
* **Git Sencillo:** Um guia interativo para os comandos básicos do Git. [rogerdudler.github.io/git-guide/index.pt_BR.html](https://rogerdudler.github.io/git-guide/index.pt_BR.html)

**6. Ferramentas de Teste de API:**

* **Postman:** Ferramenta gráfica para testar APIs. Existe uma versão gratuita para desktop e web. [postman.com/downloads/](https://www.postman.com/downloads/)
* **Insomnia:** Uma alternativa ao Postman, também popular. [insomnia.rest/download](https://insomnia.rest/download)

---

Com este roteiro detalhado, código de exemplo e recursos, seus alunos terão uma excelente base para construir um chatbot de jogos e entender conceitos fundamentais de programação e desenvolvimento web!

---