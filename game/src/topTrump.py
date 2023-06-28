import requests
import random
import pygame
import sys
import tkinter as tk

#pygame top trump game - remove the comments to run
"""
# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Trumps Game")

# Set up the fonts
font_small = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 48)

# Set up the game variables
stat_options = [
    ("ID", "id"),
    ("Height", "height"),
    ("Weight", "weight"),
    ("Base Experience", "base_experience")
]

player_score = 0
opponent_score = 0
turns_remaining = 0
chosen_stat = ""
game_over = False

# Function to get a random Pokemon from the API
def get_random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'abilities': [ability['ability']['name'] for ability in pokemon['abilities']],
        'stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']}
    }

# Function to compare the chosen stat between player and opponent
def compare_stats():
    global player_score, opponent_score
    player_pokemon = get_random_pokemon()
    opponent_pokemon = get_random_pokemon()
    player_stat = player_pokemon.get(chosen_stat, 0)
    opponent_stat = opponent_pokemon.get(chosen_stat, 0)

    if int(player_stat) > int(opponent_stat):
        result_text = "You Win!"
        player_score += 1
    elif int(player_stat) < int(opponent_stat):
        result_text = "You Lose!"
        opponent_score += 1
    else:
        result_text = "It's a Draw!"

    return player_pokemon, opponent_pokemon, player_stat, opponent_stat, result_text

# Function to reset the game
def reset_game(num_turns):
    global player_score, opponent_score, turns_remaining, chosen_stat, game_over
    player_score = 0
    opponent_score = 0
    turns_remaining = num_turns
    chosen_stat = ""
    game_over = False

# Function to render text on the screen
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Main game loop
def play_game():
    global chosen_stat, turns_remaining, game_over

    running = True
    num_turns = int(input("Enter the number of rounds (1-5): "))
    reset_game(num_turns)

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_1:
                    chosen_stat = "id"
                elif event.key == pygame.K_2:
                    chosen_stat = "height"
                elif event.key == pygame.K_3:
                    chosen_stat = "weight"
                elif event.key == pygame.K_4:
                    chosen_stat = "base_experience"
                elif event.key == pygame.K_SPACE and chosen_stat != "":
                    if turns_remaining > 0:
                        player_pokemon, opponent_pokemon, player_stat, opponent_stat, result_text = compare_stats()
                        render_text(f"You: {player_stat}", font_small, (0, 0, 0), WIDTH // 4, HEIGHT - 100)
                        render_text(f"Opponent: {opponent_stat}", font_small, (0, 0, 0), WIDTH * 3 // 4, HEIGHT - 100)
                        render_text(result_text, font_large, (255, 0, 0), WIDTH // 2, HEIGHT - 50)
                        turns_remaining -= 1

                        if turns_remaining == 0:
                            game_over = True

                    chosen_stat = ""

            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH // 2 - 50 <= mouse_pos[0] <= WIDTH // 2 + 50 and HEIGHT // 2 <= mouse_pos[1] <= HEIGHT // 2 + 50:
                    reset_game(num_turns)

        if not game_over:
            render_text("Choose a Stat:", font_large, (0, 0, 0), WIDTH // 2, 50)
            render_text("1. ID", font_small, (0, 0, 0), WIDTH // 2, 150)
            render_text("2. Height", font_small, (0, 0, 0), WIDTH // 2, 200)
            render_text("3. Weight", font_small, (0, 0, 0), WIDTH // 2, 250)
            render_text("4. Base Experience", font_small, (0, 0, 0), WIDTH // 2, 300)
            render_text(f"Turns Remaining: {turns_remaining}", font_small, (0, 0, 0), WIDTH // 2, 400)
        else:
            render_text(f"You: {player_score} - Opponent: {opponent_score}", font_small, (0, 0, 0), WIDTH // 2, 400)
            render_text("Game Over!", font_large, (255, 0, 0), WIDTH // 2, HEIGHT // 2 - 50)
            render_text("Play Again", font_small, (0, 0, 0), WIDTH // 2, HEIGHT // 2 + 25)

        pygame.display.update()


# Start the game
play_game()
"""
#basic terminal game top trump game - remove the comments to run
"""
def get_random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'abilities': [ability['ability']['name'] for ability in pokemon['abilities']],
        'stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']}
    }

def run():
    player_score = 0
    opponent_score = 0

    num_rounds = int(input("Enter the number of rounds you want to play: "))
    print("Lets play Top Trumps!")

    for round in range(1, num_rounds + 1):
        print(f"\n---- Round{round} ----")

        player_pokemon = get_random_pokemon()
        print(f"You were given {player_pokemon['name']} (ID: {player_pokemon['id']})")

        print("Available stats:")
        print("1. ID")
        print("2. Height")
        print("3. Weight")
        print("4. Base Experience")
        print("5. Abilities")
        print("6. Stats")

        stat_choice = input("Choose the stat number you want to use: ")
        stat_name = get_stat_name(stat_choice)

        opponent_pokemon = get_random_pokemon()
        print(f"The opponent chose {opponent_pokemon['name']} (ID: {opponent_pokemon['id']})")

        player_stat = player_pokemon[stat_name]
        opponent_stat = opponent_pokemon[stat_name]

        print(f"\nYour {stat_name.capitalize()}: {player_stat}")
        print(f"\nOpponent's {stat_name.capitalize()}: {opponent_stat}")

        if player_stat > opponent_stat:
            player_score += 1
            print("You win!")
        elif player_stat < opponent_stat:
            opponent_score += 1
            print("You lose!")
        else:
            print("It's a draw!")

    print("\n---- Game Over ----")
    print(f"Player Score: {player_score}")
    print(f"Opponent Score: {opponent_score}")

    if player_score > opponent_score:
        print("Congratulations! You win the Game!")
    elif player_score < opponent_score:
        print("You lose the Game!")
    else:
        print("It's a draw")


def get_stat_name(stat_choice):
    stat_mapping = {
        '1': 'id',
        '2': 'height',
        '3': 'weight',
        '4': 'base_experience',
        '5': 'abilities',
        '6': 'stats'
    }
    return stat_mapping.get(stat_choice, 'id')


if __name__ == "__main__":
    run()
"""
#tkinter game top trump game - remove the comments to run
'''
def play_game():
    def choose_stat():
        selected_stat = stat_var.get()
        stat_name = get_stat_name(selected_stat)
        compare_stats(stat_name)

    def compare_stats(stat_name):
        player_pokemon = get_random_pokemon()
        opponent_pokemon = get_random_pokemon()

        player_stat = player_pokemon.get(stat_name, 0)
        opponent_stat = opponent_pokemon.get(stat_name, 0)

        player_pokemon_label.config(text=f"You: {player_stat}")
        opponent_pokemon_label.config(text=f"Opponent: {opponent_stat}")

        if int(player_stat) > int(opponent_stat):
            result_label.config(text="You Win!")
            update_scores("win")
        elif int(player_stat) < int(opponent_stat):
            result_label.config(text="You Lose!")
            update_scores("lose")
        else:
            result_label.config(text="It's a Draw!")

        turns_remaining[0] -= 1
        if turns_remaining[0] <= 0:
            play_button.config(state="disabled")
            result_label.config(text=f"Game Over! Final Score: You {player_score[0]} - Opponent {opponent_score[0]}")

    def get_stat_name(stat_choice):
        stat_mapping = {
            '1': 'id',
            '2': 'height',
            '3': 'weight',
            '4': 'base_experience'
        }
        return stat_mapping.get(stat_choice, 'id')

    def update_scores(outcome):
        if outcome == "win":
            player_score[0] += 1
        elif outcome == "lose":
            opponent_score[0] += 1

    def reset_game():
        turns_remaining[0] = int(turns_entry.get())
        player_score[0] = 0
        opponent_score[0] = 0
        play_button.config(state="normal")
        result_label.config(text="")
        player_pokemon_label.config(text="")
        opponent_pokemon_label.config(text="")

    root = tk.Tk()
    root.title("Top Trumps Game")

    stat_options = [
        ("ID", "1"),
        ("Height", "2"),
        ("Weight", "3"),
        ("Base Experience", "4")
    ]

    stat_var = tk.StringVar()
    stat_var.set("1")  # Default selection

    stat_frame = tk.Frame(root)
    stat_frame.pack(pady=10)

    for text, value in stat_options:
        stat_radio = tk.Radiobutton(stat_frame, text=text, variable=stat_var, value=value)
        stat_radio.pack(side="left")

    play_button = tk.Button(root, text="Play", command=choose_stat)
    play_button.pack(pady=10)

    turns_frame = tk.Frame(root)
    turns_frame.pack()

    turns_label = tk.Label(turns_frame, text="Number of Turns:")
    turns_label.pack(side="left")

    turns_entry = tk.Entry(turns_frame, width=10)
    turns_entry.pack(side="left")

    reset_button = tk.Button(root, text="Reset", command=reset_game)
    reset_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    player_pokemon_label = tk.Label(root, text="")
    player_pokemon_label.pack(pady=5)

    opponent_pokemon_label = tk.Label(root, text="")
    opponent_pokemon_label.pack(pady=5)

    turns_remaining = [0]
    player_score = [0]
    opponent_score = [0]

    root.mainloop()


if __name__ == "__main__":
    play_game()
'''
