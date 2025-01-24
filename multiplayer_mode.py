def multiplayer():
    print("Want to play Hangman ?")

    num_players = int(input("Enter the number of players: "))

    player_names = []
    for i in range(num_players):
        name = input("Enter player " + str(i+1) + " name: ")
        player_names.append(name)

    player_scores = {}
    for name in player_names:
        player_scores[name] = 0

    words = ["apple", "banana", "cherry", "date", "elderberry"]
    word_to_guess = random.choice(words)

    chances = 3

    guessed_letters = set()

    while chances > 0:
        for player_name in player_names:
            print("\n" + player_name + "'s turn:")

            word_display = ""
            for letter in word_to_guess:
                if letter in guessed_letters:
                    word_display += letter + " "
                else:
                    word_display += "_ "
            print(word_display)

            guess = input("Enter your guess: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid guess! Please enter a single letter.")
                continue
            elif guess in guessed_letters:
                print("You already guessed that letter! Try again.")
                continue
            elif guess not in word_to_guess:
                print("Incorrect guess!")
                chances -= 1
                guessed_letters.add(guess)
            else:
                print("Correct guess!")
                player_scores[player_name] += 1
                guessed_letters.add(guess)

                if all(letter in guessed_letters for letter in word_to_guess):
                    print("Congratulations, " + player_name + "! You won!")
                    return

    print("\nGame over! Final scores:")
    for player, score in player_scores.items():
        print(player + ": " + str(score))

multiplayer()
