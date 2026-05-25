
import random
palavras = [
    'elefante',
    'girafa',
    'cachorro',
    'gato',
    'tigre',
    'leão',
    'urso',
    'coelho',
    'macaco',
    'zebra',
    'jacaré',
    'pinguim',
    'tartaruga',
    'golfinho',
    'pantera'
]
letrasusadas = []
palavra_secreta = random.choice(palavras)
tentativas = 6
lista= list(palavra_secreta)
oculto = ['_'] * len(palavra_secreta)
print ("Bem-vindo ao Jogo da Forca")

jogar = input("deseja jogar? digite s para sim ou n para não: ")
if jogar == 'n':
    print("Obrigado por jogar! Até a próxima!")
    print("Vamos começar! e boa sorte!")
elif jogar == 's':
 while True:
  
   
    print("Palavra escolhida:", ' '.join(oculto))
    print("Tentativas restantes:", tentativas)
    tentativa = input("Digite uma letra: ")
    # verificar se possui mais de uma letra
    if len(tentativa)!=1:
     print ("tente apenas uma letra")
     continue
    # verificar se a letra foi usada
    if tentativa in letrasusadas:
     print ("voce ja escolheu esta letra")
     continue
    letrasusadas.append(tentativa)
    if tentativa in lista:
     for i in range(len(lista)):
      if lista[i] == tentativa:
            oculto[i] = tentativa
            print("Letra correta!")
            print(letrasusadas)
            print("Palavra escolhida:", ' '.join(oculto))
    elif tentativa not in lista:
            tentativas -= 1
            print("Letra incorreta!")
            print("Palavra escolhida:", ' '.join(oculto))
            print("Tentativas restantes:", tentativas)
    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)
        break
    if '_' not in oculto:
        print("Parabéns! Você ganhou! A palavra secreta era:", palavra_secreta)
        break