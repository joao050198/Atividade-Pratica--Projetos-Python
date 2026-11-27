import os
os.system("cls")

import time
print ("|======= BEM VINDO Á BATALHA POKÉMON =======|")
        
print ("|             ...Carregando...              |\n")
time.sleep (2)

print ("______________________________________")
print ("|                                    |")
print ("|                                    |")
print ("|====== ESCOLHA SEU POKÉMON ======== |")
print ("|          ⇣  POKÉMONS  ⇣             |")
print ("|   [1] 🔥  CHARMANDER  🔥           |")
print ("|   [2] 🍃  BUBASSAUR   🍃           |")
print ("|   [3] 💧  SQUIRTLE    💧           |")
print ("|____________________________________| \n")


pokemon = int(input("Digite sua escolha de pokémon: "))

if (pokemon == 1):
    print ("Você escolheu Charmander!")
elif (pokemon == 2):
    print ("Você escolheu Bubassaur!")
else :
    print ("Você escolheu Squirtle!")
print("Computador escolheu Pikachu\n")

vida = 100
vida_bot = 100

print ("______________________________________")
print ("|                                    |")
print ("|                                    |")
print ("|======= ⚠ HORA DA BATALHA ⚠ =======|")
print ("|                                    |")
print ("|                                    |")
print ("|____________________________________|")

print("...Carregando...")
time.sleep (2)

while vida > 0 and vida_bot > 0:

    print("\n=== MENU DE BATALHA ===")
    print("Sua vida:", vida)
    print("Vida do computador:", vida_bot)

    print("\n[1] Atacar")
    print("[2] Curar")
    print("[3] Fugir")

    acao = int(input("Escolha sua ação: "))

    if acao == 1:
        print("Você atacou!")
        vida_bot = vida_bot - 20
    elif acao == 2:
        print("Você se curou!")
        vida = vida + 10        
    elif acao == 3:
        print("Você fugiu!")
        break
    else:
        print("Ação inválida!")
        
    if vida_bot > 0:
        print("Pikachu atacou!")
        vida = vida - 15

    time.sleep(1)

if vida_bot <= 0:
    print("---VOCÊ VENCEU!---")
elif vida <= 0:
    print("---VOCÊ PERDEU!---")


