# src/main.py
from flask import Flask, request, jsonify
from src.utils.whatsapp_client import send_whatsapp_message
from src.games.jokenpo import play_jokenpo, OPTIONS # Importar o jogo Jokenpo

app = Flask(__name__)

user_states = {} # {'user_id': {'game': 'jokenpo', 'data': {...}}}

@app.route('/')
def home():
    return "Olá, mundo! Este é o seu chatbot de jogos!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Dados recebidos no webhook:", data)

    user_number = data.get('from', '5511999999999')
    incoming_message = data.get('text', '').lower().strip()

    response_message = "Desculpe, não entendi. Digite 'menu' para ver os jogos disponíveis."

    # Obter o estado atual do usuário
    current_user_state = user_states.get(user_number, {})
    current_game = current_user_state.get('game')

    if incoming_message == "oi" or incoming_message == "menu":
        response_message = "Olá! Eu sou o Chatbot de Jogos! Escolha um jogo:\n1. Jokenpo\n2. Forca\n3. Adivinhação"
        user_states[user_number] = {} # Reseta o estado
    elif incoming_message == "1" or incoming_message == "jokenpo":
        response_message = "Vamos jogar Jokenpo! Escolha: pedra, papel ou tesoura."
        user_states[user_number] = {'game': 'jokenpo'}
    elif current_game == 'jokenpo':
        # Se o usuário está no jogo Jokenpo, processar a escolha
        if incoming_message in OPTIONS:
            result_msg, bot_choice = play_jokenpo(incoming_message)
            response_message = f"Você escolheu: {incoming_message.capitalize()}\nEu escolhi: {bot_choice.capitalize()}\n{result_msg}\n\nQuer jogar Jokenpo de novo? Ou digite 'menu' para outros jogos."
        else:
            response_message = "Escolha inválida para Jokenpo. Por favor, digite 'pedra', 'papel' ou 'tesoura'."
    # ... (Adicionar lógica para outros jogos depois)

    send_whatsapp_message(user_number, response_message)

    return jsonify({"status": "Mensagem processada", "response": response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)