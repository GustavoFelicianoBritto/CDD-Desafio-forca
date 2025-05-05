import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

forcaDraw = [
    """
  +---+
  |   |
      |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========"""
]

estagioForca=0
palavra = input("Jogador desafiante, digite a palavra para o jogador 2: ").lower() or "Carro".lower()
if palavra=="carro":
    categoria="Veiculo"
else:
    categoria=input("Jogador desafiante, qual a categoria dessa palavra? ")

#Quantidade de letra da palavra escolhida
letterQtd = len(palavra)
acertos=0
vidas=6
letterSend =[]

clearConsole()
print("==========================\n")
print(f"Bem vindo ao jogo da forca!!! \n"
      f"Dica: {categoria}\n")

wordGuess = ['_']*letterQtd

def displayWord():
    return " , ".join(wordGuess[:letterQtd])

while acertos < letterQtd and vidas>0:
    notValid = 0
    print(f"Letras enviadas: {letterSend}")
    print(forcaDraw[estagioForca])
    dp = displayWord().upper()
    letter = str(input(f"{dp}\n\nDigite uma letra: ").lower())
    clearConsole()

    if letter not in letterSend:
        letterSend.append(letter)
        # se a letra enviada não estiver no vetor das letras enviadas, irei colocar ela dentro e darei sequencia no código
        print("==========================\n")

        for indexLetter, currentLetter in enumerate(palavra):
            if letter == currentLetter:
                print(f"Letra '{letter}' encontrada na posição {indexLetter +1}")
                #colocando a letra encontrada na posição do _ do vetor da forca
                wordGuess[indexLetter] = letter
                acertos+=1
            else:
                notValid+=1
                #a cada giro no for, adiciono +1 pra cada slot que a letra não estiver (continua abaixo)

        if notValid == letterQtd:
            clearConsole()
            vidas-=1
            estagioForca+=1
            print("==========================\n")
            print("[Opção incorreta]")
            #se o valor de notValid for igual a quantidade de letra da palavra, vou saber que n tem a letra na palavra
    else:
        #se a letra já estiver nas letras enviadas, não farei nada e indicarei que a letra ja´foi enviada
        clearConsole()
        print("==========================\n")
        print(f"--------------------\nLetra já enviada\n--------------------")

    print(f"Vidas restantes: {vidas}")

#final do while (acertou todas letras ou perdeu todas vidas)
clearConsole()
print("==========================\n")
if vidas <= 0:
    print(forcaDraw[estagioForca])
    print(f"Você perdeu! a palavra era: {palavra.upper()}")
else:
    print(forcaDraw[estagioForca])
    print(f"Parabéns, você acertou a palavra: {palavra} com {vidas} vidas")

dp = displayWord().upper()
print(dp)
print(f"Letras enviadas: {letterSend}")
#print(ActiveWord)

print(f"\nPressione enter para fechar: ")
input()