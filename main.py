from InquirerPy import inquirer
import random
from colorama import Fore, Style

def exibir_vida(atual, maximo):
    porcentagem_vida = (atual / maximo) * 100
    if porcentagem_vida > 50:
        cor = Fore.GREEN
    elif porcentagem_vida > 25:
        cor = Fore.YELLOW
    else:
        cor = Fore.RED
    return f"{cor}{atual}/{maximo} HP{Style.RESET_ALL}"

poke1_hp = 750
poke2_hp = 750
max_hp = 750
ataques_infernape = ["Blitz de Chamas (Poder: 120 Precisão: 100%)", "Porradaria (Poder: 110 Precisão: 75%)", "Ataque de Fúria (Poder: 35 Precisão: 85%)", "Cabeçada (Poder: 80 Precisão: 80%)"]

# Descrição dos ataques do Lucario
print(f"\n{Fore.LIGHTGREEN_EX}Descrições dos Ataques do Lucario:")
print(f"{Fore.LIGHTGREEN_EX}Aura Esférica:{Style.RESET_ALL} {Fore.CYAN}Esse ataque não pode errar{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Quebra Meteoro:{Style.RESET_ALL} {Fore.CYAN}25% de chance de curar o usuário{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Voadora Alta:{Style.RESET_ALL} {Fore.CYAN}Se esse ataque errar, o usuário toma 50% do dano{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Dança das Espadas:{Style.RESET_ALL} {Fore.CYAN}O ataque do usuário aumenta consideravelmente{Style.RESET_ALL}")

# Descrição dos ataques do Infernape
print(f"\n{Fore.LIGHTRED_EX}Descrições dos Ataques do Infernape:")
print(f"{Fore.LIGHTRED_EX}Blitz de Chamas:{Style.RESET_ALL} {Fore.YELLOW}Quando usada, o usuário toma 33% do dano causado como recuo{Style.RESET_ALL}")
print(f"{Fore.LIGHTRED_EX}Porradaria:{Style.RESET_ALL} {Fore.YELLOW}Ataque sem efeitos adicionais, mas com grande poder{Style.RESET_ALL}")
print(f"{Fore.LIGHTRED_EX}Ataque de Fúria:{Style.RESET_ALL} {Fore.YELLOW}Pode acertar de 2 a 5 vezes{Style.RESET_ALL}")
print(f"{Fore.LIGHTRED_EX}Cabeçada:{Style.RESET_ALL} {Fore.YELLOW}50% de chance de causar o dobro de dano{Style.RESET_ALL}\n")


danca_das_espadas = False

# Loop da batalha
while poke1_hp > 0 and poke2_hp > 0:
    print(f"\nLucario: {exibir_vida(poke1_hp, max_hp)}")
    print(f"Infernape: {exibir_vida(poke2_hp, max_hp)}\n")

    # Prompt para escolher o ataque
    ataque = inquirer.select(
        message="Escolha seu movimento:",
        choices=[
            "Aura Esférica (Poder: 85   Precisão: 100%)",
            "Quebra Meteoro (Poder: 100   Precisão: 80%)",
            "Voadora Alta (Poder: 130   Precisão: 70%)",
            "Dança das Espadas (Poder: 0   Precisão: 100%)"
        ]
    ).execute()

    # Lógica dos ataques do Lucario
    print(f"\n{Fore.LIGHTGREEN_EX}Lucario usa {ataque.split('(')[0].strip()}!{Style.RESET_ALL}")
    if ataque == "Aura Esférica (Poder: 85   Precisão: 100%)":
        poke2_hp -= 85 + (30 if danca_das_espadas else 0)  
        print(f"{Fore.CYAN}Infernape toma {85 + (30 if danca_das_espadas else 0)} de dano!{Style.RESET_ALL}\n")
        
    elif ataque == "Quebra Meteoro (Poder: 90   Precisão: 80%)":
        if random.randint(1, 100) > 80:
            print(f"{Fore.RED}Lucario errou!{Style.RESET_ALL}")
        else:
            poke2_hp -= 90 + (30 if danca_das_espadas else 0)
            print(f"{Fore.CYAN}Infernape toma {90 + (30 if danca_das_espadas else 0)} de dano!{Style.RESET_ALL}")
            if random.randint(1, 100) <= 20:
                poke1_hp += 20
                print(f"{Fore.CYAN}Lucario se cura 20 pontos!{Style.RESET_ALL}\n")
                
    elif ataque == "Voadora Alta (Poder: 130   Precisão: 70%)":
        if random.randint(1, 100) > 70:
            poke1_hp -= 60
            print(f"{Fore.RED}Lucario errou e se feriu, tomando 60 de dano!{Style.RESET_ALL}")
        else:
            poke2_hp -= 130 + (30 if danca_das_espadas else 0)
            print(f"{Fore.CYAN}Infernape toma {130 + (30 if danca_das_espadas else 0)} de dano!{Style.RESET_ALL}\n")
            
    elif ataque == "Dança das Espadas (Poder: 0   Precisão: 100%)":
        danca_das_espadas = True
        print(f"{Fore.CYAN}O ataque de Lucario aumentou seu dano nos próximos turnos!{Style.RESET_ALL}\n")
        
    if poke2_hp <= 0:
        print(f"{Fore.YELLOW}Infernape foi derrotado! Lucario vence!{Style.RESET_ALL}")
        vencedor = "Lucario"
        break

    # Turno do Infernape
    ataque_infernape = random.choice(ataques_infernape)
    print(f"\n{Fore.LIGHTRED_EX}Infernape usa {ataque_infernape.split('(')[0].strip()}!{Style.RESET_ALL}")

    if ataque_infernape == "Blitz de Chamas (Poder: 120 Precisão: 100%)":
        poke1_hp -= 120
        dano_recoil = int(120 * 0.33)
        poke2_hp -= dano_recoil
        print(f"{Fore.YELLOW}Lucario toma 120 de dano!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Infernape sofre {dano_recoil} de dano devido ao recuo!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Porradaria (Poder: 110 Precisão: 75%)":
        if random.randint(1, 100) <= 75:
            poke1_hp -= 110
            print(f"{Fore.YELLOW}Lucario toma 110 de dano!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Infernape errou!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Ataque de Fúria (Poder: 35 Precisão: 85%)":
        acertos = 0
        if random.randint(1, 100) <= 85:
            acertos += 2
            for _ in range(3):
                if random.randint(1, 100) <= 35:
                    acertos += 1
                else:
                    break
            dano_total = acertos * 35
            poke1_hp -= dano_total
            print(f"{Fore.YELLOW}Ataque de Fúria acerta {acertos} vez(es), causando {dano_total} de dano!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Infernape errou!{Style.RESET_ALL}\n")

    elif ataque_infernape == "Cabeçada (Poder: 80 Precisão: 80%)":
        if random.randint(1, 100) <= 80:
            dano = 80
            if random.randint(1, 100) <= 50:  
                dano *= 2
                print(f"{Fore.YELLOW}Golpe crítico! Dano dobrado!{Style.RESET_ALL}")
            poke1_hp -= dano
            print(f"{Fore.YELLOW}Lucario toma {dano} de dano!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Infernape errou a Cabeçada!{Style.RESET_ALL}\n")

    # Verifica se o Lucario foi derrotado
    if poke1_hp <= 0:
        print(f"{Fore.YELLOW}Lucario foi derrotado! Infernape vence!{Style.RESET_ALL}")
        vencedor = "Infernape"
        break


if vencedor == "Lucario":
    print(f"""{Fore.LIGHTCYAN_EX}
░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓▓▓░░▒▒▒░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒▓▓▒▒▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒▓█▓▓▓▓▒▓▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓▓▓█▓▓▓▓▓▓▓░░░░░░░░░░░░░░
░░░░░░░░░░░░░▓▓▓▓▓▒░▒▓▓▓▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒▒▒░▓▓▒▒▒▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒▒▒▓▓▓▒▒▓▓░░░░░░░░░░░░░░
░░░░░░░░▒▒▒▓▓▒░░░░░░░░▒▒░░▒░░░░░░░░░░░░░
░░░░░░░░▓▓▓▒░░░░░░░░░▒▒░░░░▒▓▒░░░░░░░░░░
░░░░░░░░░▓▓▒▒░░░░░░▒▓▓▓▒▒▒▓▓▓▓▒▒░░░░░░░░
░░░░░░░░▒▒▒▒▓▓▒░░░▒▒▒▒▒▓▓▓▒▒▒▓▓▓░░░░░░░░
░░░░░░░░░░░░░░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░
░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░
░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░▒▓▓░░░░░░░░░░
░░░░░░░░░░░░░░░▒▓▓▒░░░░░░░░▒▓▒░░░░░░░░░░
░░░░░░░░░░░░░░▒▓▓▒░░░░░░░░░▒▓▓░░░░░░░░░░
░░░░░░░░░░░░░▒▓▓▓░░░░░░░░░░░▓▓▓░░░░░░░░░
░░░░░░░░░░░░▒▓▓▓▒░░░░░░░░░░░░▓▓▓▓▒░░░░░░
░░░░░░░░░░░░▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░
          """)
else:
    print(f"""{Fore.LIGHTRED_EX}
 ░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░░░░░░░░░░░░░░░▒▒▒░▒▓▓▒▒▓▓▓▒▒▒▒▒▓▓▒░░░░░░░░░░░░░
 ░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░
 ░░░░░░░░░░░▒░░▓▓▒▒▒▓▒▒▓▓▓▓▒░░▒▓▓▒░░░░░░░░░░░░░░░░
 ░░░░░░░░░░░▒▓▒▒▓▒░▒░░░▒▓▓▒░░░░░░░░░░░░░░░░▒▒░░░░░
 ░░░░░░░░░░░░▓▓░░░░▒▓▒░▓▓▓▒▒▒░░░░░░░░░░▒▓▓▓▓▒░░░░░
 ░░░░░░░░░░░░░▒▓▒▒▓▓▓▓░▒▒▒▒▒▒▒▒▒░░░░░▒▓▒▒░░░░░░░░░
 ░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▒░▒▓▓░░░░░░░░░░░░
 ░░░░░░░░░░▒▒▓▓▓▒▒▒▒▒▓▒░▒▒▒░▒░░░▒▒▓▓▒▒░░░░░░░░░░░░
 ░░░░░░░░░▒▓▓▒░░░░░░░░▒░░░▒░░░░░░░▓▓▓▓▒▒░░░░░░░░░░
 ░░░░░░░▒▒▓▒░░░░░░░░░▒▒░░░░░░▒▒░▒▓░░░▒▒▒▒░░░░░░░░░
 ░░░░░▒▒▒▓▒░░░░░░▒▒▓▓▓▓▓▓▓▒▓▒▓▒░▒▒▒░░░▒░▒▒▒░░░░░░░
 ░░░░▒▒▒▒▓░░░░░▒▒▒▓▓▓▓▒▒░░░▒▒▓▓▒▒▒▒░░░░▒▒▒▒▓▓░░░░░
 ░░░░░▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░▒▒░▒░░▒▓░▒▓▓▓▓░░░░
 ░░░░░░░▒░░░░░░░░▒▒▓▓▓▒▒░░░░░░░░░░▒░░░░░░░▒▒░▒░░░░
 ░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░▒░░░▒▒░░░░░░░░░░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▒░░░░░░░░░░
          """)





