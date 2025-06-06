import numpy as np
import os
from time import sleep as sl

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
#----------------------------------------Comentários------------------------------------------------#
#--------------Este programa é um Analisador de Dados para E-mail Marketing-------------------------#
#----------Ele ajuda empresas de marketing a identificar qual público pode ou não receber e-mails---#
#---------------------------------avaliando dados como idade e classe social------------------------#
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

# --- Função Auxiliar para Limpar a Tela ---
def limpar_tela():
    # Limpa o terminal dependendo do sistema operacional
    if os.name == 'nt':  # Se for Windows
        _ = os.system('cls')
    else:  # Se for Linux, macOS (sistemas Unix-like)
        _ = os.system('clear')

# --- Função de Pausa e Retorno ao Menu ---
def voltar():
    input("\nPressione ENTER para voltar ao menu principal...")
    limpar_tela()

# --- Função de Carregamento e Análise Inicial dos Dados ---
def Lista():
    nomes=[
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Hugo", "Isabela", "João",
    "Karen", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quiteria", "Rafael", "Sofia", "Thiago",
    "Ursula", "Vitor", "Wanessa", "Xavier", "Yasmin", "Zeca", "Amanda", "Beatriz", "Caio", "Diana",
    "Emerson", "Fernanda", "Gustavo", "Heloisa", "Igor", "Julia", "Kleber", "Larissa", "Marcelo", "Nathalia",
    "Otavio", "Patricia", "Quezia", "Renan", "Sara", "Thiago", "Uriel", "Vanessa", "Wagner", "Xenia",
    "Yago", "Zelia", "Aline", "Bernardo", "Cintia", "Diego", "Erica", "Fabio", "Gisele", "Heitor",
    "Ines", "Juliano", "Kamila", "Leandro", "Mirella", "Norberto", "Osmar", "Pamela", "Quintino", "Ricardo",
    "Sandra", "Tadeu", "Ulisses", "Veronica", "Wendell", "Ximena", "Yara", "Zoe", "Adilson", "Barbara",
    "Cesar", "Debora", "Everton", "Flavia", "Gilberto", "Humberto", "Iara", "Jonas", "Katia", "Livia",
    "Marcos", "Nelson", "Orlando", "Priscila", "Quirino", "Regina", "Sergio", "Tatiana", "Valdir", "Vivian" 
    ]
    idades_respectivamente=[
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 56, 57, 58, 22, 23, 25,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 56, 57, 58, 25, 12, 28] 
    classe = [
    "a", "b", "c", "d", "a", "b", "c", "d", "a", "b",
    "c", "d", "a", "b", "c", "d", "a", "b", "c", "d",
    "a", "b", "c", "d", "a", "b", "c", "d", "a", "b",
    "c", "d", "a", "b", "c", "d", "a", "b", "c", "d",
    "a", "b", "c", "d", "a", "b", "c", "d", "a", "b",
    "c", "d", "a", "b", "c", "d", "a", "b", "c", "d",
    "a", "b", "c", "d", "a", "b", "c", "d", "a", "b",
    "c", "d", "a", "b", "c", "d", "a", "b", "c", "d",
    "a", "b", "c", "d", "a", "b", "c", "d", "a", "b",
    "c", "d", "a", "b", "c", "d", "a", "b", "c", "d"
    ] 

    #Transformar as listas em array numpy
    nomesNP = np.array(nomes) 
    idadesNP = np.array(idades_respectivamente)    
    classeNP = np.array(classe)

    # Conta o número total de registros/pessoas
    totalDePessoas = idadesNP.size 
    
    # Calcula a idade máxima e mínima
    idadeMaxima = np.max(idadesNP)
    idadeMinima = np.min(idadesNP)

    return idadesNP, totalDePessoas, classeNP, nomesNP


# --- Função para Análise de E-mail Marketing de Álcool ---
def EmpresasDeAlcool():
    print("\n--- Análise para E-mail Marketing de Álcool ---")
    print("Verificando clientes com idade > 18...")
    idades_np, total_pessoas, _, _ = Lista()
    permitido_alcool = idades_np >= 18
    total_permitido = np.sum(permitido_alcool)

    if total_permitido == total_pessoas:
        print("Resultado: Todos os clientes são elegíveis para receber e-mail de álcool.")
    elif total_permitido > 0:
        print(f"Resultado: Alguns clientes ({total_permitido} de {total_pessoas}) são elegíveis para receber e-mail de álcool.")
    else:
        print("Resultado: Nenhum cliente é elegível para receber e-mail de álcool.")
    voltar()

# --- Função para Análise de E-mail Marketing de Brinquedos ---
def EmpresasBrinquedos():
    print("\n--- Análise para E-mail Marketing de Brinquedos ---")
    print("Verificando clientes com idade <= 12...")
    idades_np, total_pessoas, _, _ = Lista() 
    permitido_brinquedos = idades_np <= 12
    total_permitido = np.sum(permitido_brinquedos)

    if total_permitido == total_pessoas:
        print("Resultado: Todos os clientes são elegíveis para receber e-mail de brinquedos.")
    elif total_permitido > 0:
        print(f"Resultado: Alguns clientes ({total_permitido} de {total_pessoas}) são elegíveis para receber e-mail de brinquedos.")
    else:
        print("Resultado: Nenhum cliente é elegível para receber e-mail de brinquedos.")
    voltar() 

# --- Função para Análise de E-mail Marketing de Passagens de Avião ---
def EmpresasPassagemDeAvião():
    print("\n--- Análise para E-mail Marketing de Passagens de Avião ---")
    print("Verificando clientes com idade >= 22 e classes 'a', 'b', ou 'c'...")
    
    idades_np, total_pessoas, social_classe_np, nomes_np = Lista()
    classes_elegiveis = ["a", "b", "c"]
    mascara_classes_elegiveis = np.isin(social_classe_np, classes_elegiveis)
    mascara_idade_elegivel = idades_np >= 22
    mascara_final_permitidos = mascara_idade_elegivel & mascara_classes_elegiveis

    # Conta o número total de pessoas que atendem a todos os critérios
    total_permitidos = np.sum(mascara_final_permitidos)
    if total_permitidos == total_pessoas:
        print("Resultado: Todos os clientes atendem aos critérios para e-mail de passagem de avião.")
    elif total_permitidos > 0:
        print(f"Resultado: Alguns clientes ({total_permitidos} de {total_pessoas}) são elegíveis para e-mail de passagem de avião.")
        print("\nClientes elegíveis:")
        for nome, idade, classe_social in zip(
            nomes_np[mascara_final_permitidos],
            idades_np[mascara_final_permitidos],
            social_classe_np[mascara_final_permitidos]
        ):
            print(f"- {nome} (Idade: {idade}, Classe: {classe_social})")
    else:
        print("Resultado: Nenhum cliente atende aos critérios para e-mail de passagem de avião.")
    voltar()


# --- Função do Menu Principal de Escolhas ---
def Escolhas():
    while True: 
        print("\n--- Menu Principal de Análise de Marketing ---")
        print("Escolha uma das opções:")
        print("1: Exibir Dados Gerais Carregados")
        print("2: Análise para E-mail Marketing de Álcool")
        print("3: Análise para E-mail Marketing de Brinquedos")
        print("4: Análise para E-mail Marketing de Passagens de Avião")
        print("0: Sair do Programa")
        try:
            escolha = int(input("Digite o número da sua escolha: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro (0-4).")
            sl(1)
            limpar_tela()
            continue
        if escolha == 1:
            print("\nExibindo os dados gerais da lista...")
            idades_np, total_pessoas, classe_np, nomes_np = Lista() 
            print(f"Nomes dos clientes: {nomes_np}")
            print(f"Essas são todas as idades: {idades_np}")
            print(f"Número total de pessoas: {total_pessoas}")
            print(f"As classes sociais: {classe_np}")
            print(f"Idade máxima: {np.max(idades_np)}")
            print(f"Idade mínima: {np.min(idades_np)}")
            voltar() 
        elif escolha == 2:
            EmpresasDeAlcool()
        elif escolha == 3:
            EmpresasBrinquedos()
        elif escolha == 4:
            EmpresasPassagemDeAvião()
        elif escolha == 0:
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("Escolha fora do intervalo. Por favor, digite um número entre 0 e 4.")
            sl(1)
            limpar_tela()

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    limpar_tela()
    Escolhas()

