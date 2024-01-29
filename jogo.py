import random 
from os import system, name
from unidecode import unidecode

def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear') 

def game():
    clear_terminal()
    
    print('Welcome to Hangman Game')
    print('Guess the word below:\n')
    
    with open('palavras.txt','r',encoding='utf8') as arquivo:
        conteudo = arquivo.read()
    word_list = conteudo.split('\n')    
    word = unidecode(random.choice(word_list).lower())       
   
    guessed_letters = ['_' if letter != " " else " " for letter in word]

    chances = 6
    wrong_letters = []
    
    while chances > 0: 
        print(" ".join(guessed_letters))
        print(f"\nRemaining chances: {chances}")        
        print("Wrong letters: "," ".join(wrong_letters))
        attempt = input('\nType a Letter:').lower()
        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    guessed_letters[index] = letter
                index += 1    
        else: 
            chances -= 1
            wrong_letters.append(attempt)
            if chances == 0:
                print(f"You lost, the word was: {word}")
        if '_' not in guessed_letters:
            print(f'You won, the word was: {word}')    
            break
        
if __name__ == "__main__":
    game()
    






    
