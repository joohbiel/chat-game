# src/games/forca.py
import random

WORDS = ["python", "programacao", "chatbot", "desenvolvimento", "inteligencia"]

class ForcaGame:
    def __init__(self):
        self.word = random.choice(WORDS).upper()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6 # Número de partes do boneco da forca
        self.display_word = ["_" for _ in self.word]

    def make_guess(self, letter):
        letter = letter.upper()

        if not letter.isalpha() or len(letter) != 1:
            return "Entrada inválida. Por favor, digite apenas uma letra."

        if letter in self.guessed_letters:
            return f"Você já tentou a letra '{letter}'. Tente outra."

        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display_word[i] = letter
            return f"Boa! A letra '{letter}' está na palavra!"
        else:
            self.incorrect_guesses += 1
            return f"Ops! A letra '{letter}' não está na palavra. Vidas restantes: {self.max_incorrect_guesses - self.incorrect_guesses}"

    def get_current_state(self):
        return {
            "word_display": " ".join(self.display_word),
            "guessed_letters": ", ".join(sorted(list(self.guessed_letters))),
            "incorrect_guesses": self.incorrect_guesses,
            "max_incorrect_guesses": self.max_incorrect_guesses,
            "is_game_over": self.is_game_over(),
            "has_won": self.has_won()
        }

    def is_game_over(self):
        return self.incorrect_guesses >= self.max_incorrect_guesses or "_" not in self.display_word

    def has_won(self):
        return "_" not in self.display_word

if __name__ == '__main__':
    # Teste simples da lógica do jogo
    game = ForcaGame()
    print(f"Palavra: {game.word}")
    print(game.get_current_state())
    print(game.make_guess("p"))
    print(game.get_current_state())
    print(game.make_guess("x"))
    print(game.get_current_state())
    print(game.make_guess("y"))
    print(game.get_current_state())