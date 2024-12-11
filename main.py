from colorama import Fore, Style
from InquirerPy import inquirer
import random

def descricao_ataques():
    lucario = {
        "Aura Esférica": "Esse ataque não pode errar",
        "Quebra Meteoro": "25% de chance de curar o usuário",
        "Voadora Alta": "Se esse ataque errar, o usuário toma 50% do dano",
        "Dança das Espadas": "O ataque do usuário aumenta consideravelmente"
        }
    
    infernape = {
        "Blitz de Chamas": "Quando usada, o usuário toma 1/3 do dano causado como recuo",
        "Porradaria": "Ataque sem efeitos adicionais, mas com grande poder",
        "Ataque de Fúria": "Pode acertar de 2 a 5 vezes",
        "Cabeçada": "50% de chance de causar o dobro de dano"
    }
    print()
    for nome, descricao in lucario.items():
        print(f"{Fore.LIGHTGREEN_EX}{nome}:{Style.RESET_ALL} {Fore.CYAN}{descricao}{Style.RESET_ALL}")
    print()
    for nome, descricao in infernape.items():
        print(f"{Fore.LIGHTRED_EX}{nome}:{Style.RESET_ALL} {Fore.YELLOW}{descricao}{Style.RESET_ALL}")
        
def exibir_vida(atual, maximo, largura=30):
    porcentagem_vida = atual / maximo
    blocos_cheios = int(porcentagem_vida * largura)
    blocos_vazios = largura - blocos_cheios
    if porcentagem_vida > 0.5:
        cor = Fore.GREEN
    elif porcentagem_vida > 0.25:
        cor = Fore.YELLOW
    else:
        cor = Fore.LIGHTRED_EX
    barra = f"{cor}{'█' * blocos_cheios}{' ' * blocos_vazios}{Style.RESET_ALL}"
    return f"{cor}{atual}: {barra}"

poke1_hp = 1000
poke2_hp = 1000
max_hp = 1000
danca_das_espadas = False
ataques_infernape = ["Blitz de Chamas (Poder: 120 Precisão: 100%)",
                     "Porradaria (Poder: 110 Precisão: 75%)",
                     "Ataque de Fúria (Poder: 35 Precisão: 85%)",
                     "Cabeçada (Poder: 80 Precisão: 80%)"]

ataques_lucario = ["Aura Esférica (Poder: 85   Precisão: 100%)",
                   "Quebra Meteoro (Poder: 100   Precisão: 80%)",
                   "Voadora Alta (Poder: 130   Precisão: 70%)",
                   "Dança das Espadas (Poder: 0   Precisão: 100%)"]
descricao_ataques()


# Loop da batalha
while poke1_hp > 0 and poke2_hp > 0:
    print(f"\n{Fore.LIGHTCYAN_EX}HP Lucario:  {Style.RESET_ALL} {exibir_vida(poke1_hp, max_hp)}\n")
    print(f"{Fore.LIGHTRED_EX}HP Infernape:{Style.RESET_ALL} {exibir_vida(poke2_hp, max_hp)}\n")

    # Prompt para escolher o ataque
    ataque = inquirer.select(
        message="Escolha seu movimento:",
        choices= ataques_lucario
    ).execute()

    # Lógica dos ataques do Lucario
    print(f"\n{Fore.LIGHTGREEN_EX}Lucario usa {ataque.split('(')[0].strip()}!{Style.RESET_ALL}")
    if ataque == "Aura Esférica (Poder: 85   Precisão: 100%)":
        dano = 85 + danca_das_espadas
        poke2_hp -= dano  
        print(f"{Fore.CYAN}Infernape toma {dano} de dano!{Style.RESET_ALL}\n")
        
    elif ataque == "Quebra Meteoro (Poder: 100   Precisão: 80%)":
        if random.randint(1, 100) > 80:
            print(f"{Fore.RED}Lucario errou!{Style.RESET_ALL}")
        else:
            dano = 100 + danca_das_espadas
            poke2_hp -= dano
            print(f"{Fore.CYAN}Infernape toma {dano} de dano!{Style.RESET_ALL}")
            if random.randint(1, 100) <= 20:
                poke1_hp += 20
                print(f"{Fore.CYAN}Lucario se cura 20 pontos!{Style.RESET_ALL}\n")
                
    elif ataque == "Voadora Alta (Poder: 130   Precisão: 70%)":
        if random.randint(1, 100) > 70:
            poke1_hp -= 60
            print(f"{Fore.RED}Lucario errou e se feriu, tomando 60 de dano!{Style.RESET_ALL}")
        else:
            dano = 130 + danca_das_espadas
            poke2_hp -= dano
            print(f"{Fore.CYAN}Infernape toma {dano} de dano!{Style.RESET_ALL}\n")
            
    elif ataque == "Dança das Espadas (Poder: 0   Precisão: 100%)":
        if danca_das_espadas:
            print(f"{Fore.CYAN}O Ataque falhou!{Style.RESET_ALL}")
        else:
            danca_das_espadas = 25
            print(f"{Fore.CYAN}O poder de ataque de Lucario aumentou nos próximos turnos!{Style.RESET_ALL}\n")
        
    # Turno do Infernape
    ataque_infernape = random.choice(ataques_infernape)
    print(f"\n{Fore.LIGHTRED_EX}Infernape usa {ataque_infernape.split('(')[0].strip()}!{Style.RESET_ALL}")

    if ataque_infernape == "Blitz de Chamas (Poder: 120 Precisão: 100%)":
        poke1_hp -= 120
        dano_recoil = int(120/3)
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

    # Verifica se o Infernape foi derrotado
    if poke2_hp <= 0:
        print(f"{Fore.YELLOW}Infernape foi derrotado! Lucario vence!{Style.RESET_ALL}")
        vencedor = "Lucario"
        break
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





