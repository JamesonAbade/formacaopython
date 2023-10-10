import random


def jogar():
  numero_secreto = random.randrange(10)

  # print(numero_secreto)
  total_tentativas = 0
  pontos = 10

  print("Qual nível de dificuldade?")
  print("(1) Fácil, (2) Médio (3)Difícil")
  nivel = int(input("Defina o nível: "))

  if(nivel == 1):
    total_tentativas = 20
  elif(nivel == 2):
    total_tentativas = 10
  elif(nivel == 3):
    total_tentativas = 5


  for rodada in range (1, total_tentativas +1):
    print("tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um numero entre 1 e 10: ")
    print("Você digitou o número ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100")
      continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
      print("Você acertou e fez {} pontos!".format(pontos))
      break
    else:
      if(maior):
        print("Você errou! O seu chute foi maior que o número secreto")
      elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()