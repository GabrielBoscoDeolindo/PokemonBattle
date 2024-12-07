from InquirerPy import inquirer
import random
from colorama import Fore, Style

def exibir_vida(atual, maximo):
    porcentagem = (atual / maximo) * 100
    if porcentagem > 50:
        cor = Fore.GREEN
    elif porcentagem > 25:
        cor = Fore.YELLOW
    else:
        cor = Fore.RED
    return f"{cor}{atual}/{maximo} HP{Style.RESET_ALL}"

poke1_hp = 750
poke2_hp = 750
max_hp = 750
ataques_infernape = ["Blitz de Chamas (Poder: 120 Precisão: 100%)", "Porradaria (Poder: 120 Precisão: 75%)", "Ataque de Fúria (Poder: 35 Precisão: 85%)", "Cabeçada (Poder: 80 Precisão: 80%)"]

# Descrição dos ataques do Lucario
print("\nDescrições dos Ataques do Lucario:")
print(f"{Fore.GREEN}{Style.BRIGHT}Aura Esférica:{Style.RESET_ALL} {Fore.CYAN}{Style.BRIGHT}Esse ataque não pode errar{Style.RESET_ALL}")
print(f"{Fore.GREEN}{Style.BRIGHT}Quebra Meteoro:{Style.RESET_ALL} {Fore.CYAN}{Style.BRIGHT}20% de chance de curar o usuário{Style.RESET_ALL}")
print(f"{Fore.GREEN}{Style.BRIGHT}Voadora Alta:{Style.RESET_ALL} {Fore.CYAN}{Style.BRIGHT}Se esse ataque errar, o usuário toma 50% do dano{Style.RESET_ALL}")
print(f"{Fore.GREEN}{Style.BRIGHT}Dança das Espadas:{Style.RESET_ALL} {Fore.CYAN}{Style.BRIGHT}O ataque do usuário aumenta consideravelmente{Style.RESET_ALL}")

# Descrição dos ataques do Infernape
print("\nDescrições dos Ataques do Infernape:")
print(f"{Fore.RED}{Style.BRIGHT}Blitz de Chamas:{Style.RESET_ALL} {Fore.YELLOW}{Style.BRIGHT}Quando usada, o usuário toma 33% do dano causado como recuo{Style.RESET_ALL}")
print(f"{Fore.RED}{Style.BRIGHT}Porradaria:{Style.RESET_ALL} {Fore.YELLOW}{Style.BRIGHT}Ataque sem efeitos adicionais, mas com grande poder{Style.RESET_ALL}")
print(f"{Fore.RED}{Style.BRIGHT}Ataque de Fúria:{Style.RESET_ALL} {Fore.YELLOW}{Style.BRIGHT}Pode acertar de 2 a 5 vezes{Style.RESET_ALL}")
print(f"{Fore.RED}{Style.BRIGHT}Cabeçada:{Style.RESET_ALL} {Fore.YELLOW}{Style.BRIGHT}50% de chance de causar o dobro de dano{Style.RESET_ALL}\n")

# Loop da batalha
while poke1_hp > 0 and poke2_hp > 0:
    print(f"\nLucario: {exibir_vida(poke1_hp, max_hp)}")
    print(f"Infernape: {exibir_vida(poke2_hp, max_hp)}\n")

    # Prompt para escolher o ataque
    ataque = inquirer.select(
        message="Escolha seu movimento:",
        choices=[
            "Aura Esférica (Poder: 85   Precisão: 100%)",
            "Quebra Meteoro (Poder: 90   Precisão: 80%)",
            "Voadora Alta (Poder: 130   Precisão: 70%)",
            "Dança das Espadas (Poder: 0   Precisão: 100%)"
        ]
    ).execute()

    # Lógica dos ataques do Lucario
    if ataque == "Aura Esférica (Poder: 85   Precisão: 100%)":
        poke2_hp -= 85
        print(f"{Fore.GREEN}{Style.BRIGHT}Infernape toma 85 de dano!{Style.RESET_ALL}\n")
    elif ataque == "Quebra Meteoro (Poder: 90   Precisão: 80%)":
        if random.randint(1, 100) > 80:
            print(f"{Fore.RED}{Style.BRIGHT}Lucario errou!{Style.RESET_ALL}")
        else:
            poke2_hp -= 90
            print(f"{Fore.GREEN}{Style.BRIGHT}Infernape toma 90 de dano!{Style.RESET_ALL}\n")
            if random.randint(1, 100) <= 20:
                poke1_hp += 20
                print(f"{Fore.GREEN}{Style.BRIGHT}Lucario se cura!{Style.RESET_ALL}")
    elif ataque == "Voadora Alta (Poder: 130   Precisão: 70%)":
        if random.randint(1, 100) > 70:
            poke1_hp -= 60
            print(f"{Fore.RED}{Style.BRIGHT}Lucario errou e foi ferido!{Style.RESET_ALL}")
        else:
            poke2_hp -= 130
            print(f"{Fore.GREEN}{Style.BRIGHT}Infernape toma 130 de dano!{Style.RESET_ALL}\n")
    else:
        poke1_hp += 80
        print(f"{Fore.GREEN}{Style.BRIGHT}Lucario se cura!{Style.RESET_ALL}\n")
        
    # Verifica se Infernape foi derrotado   
    if poke2_hp <= 0:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Infernape foi derrotado! Lucario vence!{Style.RESET_ALL}")
        break

    # Lógica dos ataques do Infernape
    ataque_infernape = random.choice(ataques_infernape)
    
    if ataque_infernape == "Blitz de Chamas (Poder: 120 Precisão: 100%)":
        print(f"{Fore.RED}{Style.BRIGHT}Infernape usou Blitz de Chamas!{Style.RESET_ALL}")
        poke1_hp -= 120
        dano_recoil = int(120 * 0.33)  
        poke2_hp -= dano_recoil
        print(f"{Fore.GREEN}{Style.BRIGHT}Lucario toma 120 de dano!{Style.RESET_ALL}")
        print(f"{Fore.RED}{Style.BRIGHT}Infernape sofre {dano_recoil} de dano devido ao recuo!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Porradaria (Poder: 120 Precisão: 75%)":
        print(f"{Fore.RED}{Style.BRIGHT}Infernape usou Porradaria!{Style.RESET_ALL}")
        if random.randint(1, 100) <= 75:
            poke1_hp -= 120
            print(f"{Fore.GREEN}{Style.BRIGHT}Lucario toma 120 de dano!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Infernape errou!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Ataque de Fúria (Poder: 35 Precisão: 85%)":
        print(f"{Fore.RED}{Style.BRIGHT}Infernape usou Ataque Fúria!{Style.RESET_ALL}")
        acertos = 0
        for i in range(2):
            if random.randint(1, 100) <= 85:
                acertos += 1
            else:
                break  
        for _ in range(3):
            if random.randint(1, 100) <= 50:
                acertos += 1
            else:
                break
        dano_total = acertos * 35
        poke1_hp -= dano_total
        print(f"{Fore.GREEN}{Style.BRIGHT}Ataque de Fúria acerta {acertos} vez(es), causando {dano_total} de dano!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Cabeçada (Poder: 80 Precisão: 80%)":
        print(f"{Fore.RED}{Style.BRIGHT}Cabeçada!{Style.RESET_ALL}")
        if random.randint(1, 100) <= 80:
            dano = 80
            if random.randint(1, 100) <= 50:  
                dano *= 2
                print(f"{Fore.RED}{Style.BRIGHT}Golpe crítico! Dano dobrado!{Style.RESET_ALL}")
            poke1_hp -= dano
            print(f"{Fore.GREEN}{Style.BRIGHT}Lucario toma {dano} de dano!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Infernape errou a Cabeçada!{Style.RESET_ALL}\n")

    # Verifica se o Lucario foi derrotado
    if poke1_hp <= 0:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Lucario foi derrotado! Infernape vence!{Style.RESET_ALL}")
        break
