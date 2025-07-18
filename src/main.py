# src/main.py (Completo com a integração Fintech corrigida)

import sys
import os
# Adiciona o diretório raiz do projeto ao PATH para que fintech.py possa ser importado.
# Assumimos que 'fintech.py' estará no mesmo nível que 'src/' ou acessível no PATH.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from src.utils.whatsapp_client import send_whatsapp_message
from src.games.jokenpo import play_jokenpo, OPTIONS
from src.games.forca import ForcaGame
from src.games.adivinhacao import AdivinhacaoGame

# --- Importando a lógica da Fintech ---
# Importa a classe CSVAnalyzer do arquivo fintech.py
from fintech import CSVAnalyzer 
# --- FIM NOVIDADE ---


app = Flask(__name__)

user_states = {} # {'user_id': {'game': 'jokenpo', 'game_instance': {...}}}

# --- Funções para obter o texto dos menus de forma organizada ---
def get_main_menu_text():
    """Retorna o texto do menu principal do chatbot."""
    return (
        "Olá! Eu sou o Chatbot de Jogos! Escolha um jogo:\n"
        "1. Jokenpo\n"
        "2. Forca\n"
        "3. Adivinhação\n"
        "4. Fintech (Análise de Custos)\n" # <<<<< Esta linha garante que a opção Fintech aparece no menu principal!
        "Digite 'menu' a qualquer momento para ver as opções novamente."
    )

def get_fintech_menu_text():
    """Retorna o texto do menu da Análise de Custos da Fintech."""
    return (
        "Ok, vamos para a Análise de Custos da Fintech!\n"
        "Escolha uma opção:\n"
        "1. Custo total por departamento\n"
        "2. Custo médio por funcionário ativo\n"
        "3. Departamento mais e menos custoso\n"
        "4. Eficiência por ano de experiência\n"
        "5. Melhor custo-benefício\n"
        "6. Projeção de economia\n"
        "0. Sair da Análise de Custos (e voltar ao menu principal de jogos)"
    )


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

    # Prioriza o comando 'oi' ou 'menu' para resetar o estado e mostrar o menu principal
    if incoming_message == "oi" or incoming_message == "menu":
        response_message = get_main_menu_text()
        user_states[user_number] = {} # Reseta o estado
    
    # --- Lógica para o usuário DENTRO de um jogo/módulo ---
    # Primeiro, verifica se o usuário JÁ ESTÁ em um jogo ou módulo (como Fintech)
    elif current_game == 'jokenpo':
        # Lógica existente para Jokenpo
        if incoming_message in OPTIONS:
            result_msg, bot_choice = play_jokenpo(incoming_message)
            response_message = (
                f"Você escolheu: {incoming_message.capitalize()}\n"
                f"Eu escolhi: {bot_choice.capitalize()}\n"
                f"{result_msg}\n\n"
                "Quer jogar Jokenpo de novo? Ou digite 'menu' para outros jogos."
            )
        else:
            response_message = "Escolha inválida para Jokenpo. Por favor, digite 'pedra', 'papel' ou 'tesoura'."
    
    elif current_game == 'forca':
        # Lógica existente para Forca
        game = current_user_state.get('game_instance')
        if game:
            guess_result = game.make_guess(incoming_message)
            state = game.get_current_state()

            response_message = f"{guess_result}\nPalavra: {state['word_display']}\nLetras tentadas: {state['guessed_letters']}"

            if state['is_game_over']:
                if state['has_won']:
                    response_message += f"\n\nParabéns! Você ganhou! 🎉\n"
                else:
                    response_message += f"\n\nGame Over! Você perdeu! 😢\nA palavra era: {game.word}\n"
                response_message += "Digite 'menu' para jogar novamente."
                user_states[user_number] = {} # Reseta o estado
            else:
                response_message += f"\nVocê tem {state['attempts_left']} tentativas restantes.\nDigite uma letra:"
        else:
            response_message = "Erro no jogo. Digite 'menu' para começar novamente."
            user_states[user_number] = {}

    elif current_game == 'adivinhacao':
        # Lógica existente para Adivinhação
        game = current_user_state.get('game_instance')
        if game:
            guess_result = game.make_guess(incoming_message)
            response_message = guess_result

            if game.is_game_over:
                response_message += f"\n\nDigite 'menu' para jogar novamente."
                user_states[user_number] = {}
            else:
                response_message += f"\nTentativas restantes: {game.attempts_left}"
        else:
            response_message = "Erro no jogo. Digite 'menu' para começar novamente."
            user_states[user_number] = {}
    
    # --- Lógica para processar comandos DENTRO da Fintech ---
    elif current_game == 'fintech':
        fintech_analyzer = current_user_state.get('game_instance')
        if fintech_analyzer:
            # Processa o comando usando o método process_command do CSVAnalyzer do fintech.py
            fintech_response = fintech_analyzer.process_command(incoming_message)
            response_message = fintech_response

            # Se o comando resultou em saída do Fintech (verifica a mensagem de "Já vai?" que o fintech.py retorna)
            if "Já vai?" in fintech_response: 
                response_message += "\n" + get_main_menu_text() # Adiciona o menu principal dos jogos
                user_states[user_number] = {} # Reseta o estado para o menu principal
            # Se o Fintech não entendeu o comando (verifica a mensagem de erro do fintech.py)
            elif "Não entendi o que você pediu" in fintech_response: 
                response_message += "\n" + get_fintech_menu_text() # Reapresenta o menu da fintech para o usuário
            else: # Se a análise foi bem-sucedida, mantém no modo Fintech e lembra as opções
                response_message += (
                    "\n\nPara outras análises da Fintech, escolha um número (1-6).\n"
                    "Para voltar ao menu principal de jogos, digite '0'."
                )
        else:
            response_message = "Erro na Análise de Custos. Digite 'menu' para começar novamente."
            user_states[user_number] = {} # Reseta o estado
    # --- FIM Lógica Fintech ---

    # --- Lógica para o usuário ESCOLHENDO um NOVO JOGO (se não está em nenhum jogo) ---
    elif current_game is None: # Se o usuário não está em nenhum jogo
        if incoming_message == "1" or incoming_message == "jokenpo":
            response_message = "Vamos jogar Jokenpo! Escolha: pedra, papel ou tesoura."
            user_states[user_number] = {'game': 'jokenpo'}
        elif incoming_message == "2" or incoming_message == "forca":
            game = ForcaGame()
            state = game.get_current_state()
            response_message = f"Vamos jogar Forca!\nPalavra: {state['word_display']}\nDigite uma letra:"
            user_states[user_number] = {'game': 'forca', 'game_instance': game}
        elif incoming_message == "3" or incoming_message == "adivinhacao":
            game = AdivinhacaoGame()
            response_message = f"Vamos jogar Adivinhação!\nTente adivinhar o número entre {game.min_num} e {game.max_num}.\nVocê tem {game.max_attempts} tentativas:"
            user_states[user_number] = {'game': 'adivinhacao', 'game_instance': game}
        # --- Lógica para INICIAR o jogo Fintech ---
        elif incoming_message == "4" or incoming_message == "fintech" or incoming_message == "analise de custos":
            try:
                fintech_analyzer = CSVAnalyzer() 
                if not fintech_analyzer.data: # Se não conseguiu carregar os dados (ex: problema com a planilha)
                    response_message = "Não foi possível carregar os dados para a análise Fintech. Verifique a planilha ou a conexão."
                    user_states[user_number] = {} # Não entra no modo Fintech se não houver dados válidos
                else:
                    user_states[user_number] = {'game': 'fintech', 'game_instance': fintech_analyzer}
                    response_message = get_fintech_menu_text() # Mostra o menu completo da Fintech
            except Exception as e:
                response_message = f"Erro ao iniciar a Análise de Custos: {e}. Digite 'menu' para tentar novamente."
                user_states[user_number] = {}
        # --- FIM Lógica para INICIAR Fintech ---
        else:
            response_message = "Desculpe, não entendi. Digite 'menu' para ver os jogos disponíveis."
    
    # Esta linha final serve como um "catch-all" caso a mensagem ainda seja a padrão
    # e o usuário esteja em um estado não coberto explicitamente acima.
    if response_message == "Desculpe, não entendi. Digite 'menu' para ver os jogos disponíveis." and current_game is not None:
        # Isso significa que o usuário estava em um jogo, mas a mensagem não foi tratada por ele.
        # Poderíamos adicionar uma mensagem mais específica aqui para o jogo atual, se necessário.
        pass # Mantém a mensagem padrão de "não entendi, testando jihuihihijhi"


    send_whatsapp_message(user_number, response_message)

    return jsonify({"status": "Mensagem processada", "response": response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)