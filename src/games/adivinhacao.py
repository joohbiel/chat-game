# src/games/adivinhacao.py
import random

class AdivinhacaoGame:
    def __init__(self, min_num=1, max_num=100, max_attempts=7):
        self.secret_number = random.randint(min_num, max_num)
        self.min_num = min_num
        self.max_num = max_num
        self.attempts = 0
        self.max_attempts = max_attempts
        self.is_game_over = False
        self.has_won = False

    def make_guess(self, guess):
        if self.is_game_over:
            return "O jogo já acabou! Digite 'menu' para começar um novo."

        try:
            guess = int(guess)
        except ValueError:
            return "Entrada inválida. Por favor, digite um número."

        self.attempts += 1

        if guess < self.secret_number:
            result = "O número secreto é MAIOR."
        elif guess > self.secret_number:
            result = "O número secreto é MENOR."
        else:
            result = f"Parabéns! Você acertou o número secreto ({self.secret_number}) em {self.attempts} tentativas!"
            self.is_game_over = True
            self.has_won = True
            return result

        if self.attempts >= self.max_attempts:
            self.is_game_over = True
            result += f"\nSuas tentativas acabaram! O número secreto era {self.secret_number}."
        else:
            result += f"\nTentativas restantes: {self.max_attempts - self.attempts}"

        return result

    def get_current_state(self):
        return {
            "min_num": self.min_num,
            "max_num": self.max_num,
            "attempts": self.attempts,
            "max_attempts": self.max_attempts,
            "is_game_over": self.is_game_over,
            "has_won": self.has_won
        }

if __name__ == '__main__':
    # Teste simples da lógica do jogo
    game = AdivinhacaoGame(1, 10)
    print(f"Número secreto (para teste): {game.secret_number}")
    print(game.make_guess("5"))
    print(game.make_guess("8"))
    print(game.make_guess("9"))