# src/games/jokenpo.py
import random

OPTIONS = ["pedra", "papel", "tesoura"]

def play_jokenpo(user_choice):
    """
    Joga uma rodada de Jokenpo.
    Retorna uma tupla: (mensagem de resultado, escolha do bot)
    """
    user_choice = user_choice.lower().strip()

    if user_choice not in OPTIONS:
        return "Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.", None

    bot_choice = random.choice(OPTIONS)

    if user_choice == bot_choice:
        result = f"Empate! Ambos escolheram {user_choice}."
    elif (user_choice == "pedra" and bot_choice == "tesoura") or \
         (user_choice == "papel" and bot_choice == "pedra") or \
         (user_choice == "tesoura" and bot_choice == "papel"):
        result = f"Você ganhou! {user_choice.capitalize()} ganha de {bot_choice}."
    else:
        result = f"Eu ganhei! {bot_choice.capitalize()} ganha de {user_choice}."

    return result, bot_choice

if __name__ == '__main__':
    # Teste simples da lógica do jogo
    print(play_jokenpo("pedra"))
    print(play_jokenpo("papel"))
    print(play_jokenpo("tesoura"))
    print(play_jokenpo("banana")) # Teste de entrada inválida