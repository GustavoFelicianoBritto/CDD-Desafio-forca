

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

for i in range(50):
    print("="*20)
    print("Não suba, não trapaceie")

#print(f"Debug, a palavra é: {activeWord}")
print(f"\nBem vindo ao jogo da forca!!! \n"
      f"Dica: {categoria}\n")

wordGuess = ['_']*letterQtd

def displayWord():

    return " , ".join(wordGuess[:letterQtd])




while acertos < letterQtd and vidas>0:

    notValid = 0

    print(f"Letras enviadas: {letterSend}")

    dp = displayWord().upper()
    letter = str(input(f"{dp}\n\nDigite uma letra: ").lower())

    if letter not in letterSend:
        #se a letra enviada não estiver no vetor das letras enviadas, irei colocar ela dentro e
        #darei sequencia no código

        letterSend.append(letter)

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
            vidas-=1
            print("[Opção incorreta]")
            #se o valor de notValid for igual a quantidade de letra da palavra, vou saber que n tem a letra na palavra

    else:
        #se a letra já estiver nas letras enviadas, não farei nada e indicarei que a letra ja´foi enviada
        print(f"--------------------\nLetra já enviada\n--------------------")


    print(f"Vidas restantes: {vidas}")

#final do while (acertou todas letras ou perdeu todas vidas)

if vidas <= 0:
    print(f"Você perdeu! a palavra era: {palavra}")
else:
    print(f"Parabéns, você acertou a palavra: {palavra} com {vidas} vidas")

dp = displayWord().upper()
print(dp)
#print(ActiveWord)

print(f"\n\nPressione qualquer tecla para fechar: ")