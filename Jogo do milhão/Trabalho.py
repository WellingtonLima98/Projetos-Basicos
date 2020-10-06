'''
TRABALHO

    Faça um programa que apresente perguntas e ofereça 4 opções de resposta,
    as quais podem ou não variar de posição. Cada resposta correta vale uma
    pontuação, caso erre o jogo acaba, e o programa mostra as 5 melhores pontuações.
    
'''

from os import system
from time import sleep

# Função que lê o arquivo "Perguntas"
def Ler_Perguntas():
    with open('Perguntas.txt', 'r') as arquivo_perguntas:
        linha = arquivo_perguntas.read()
        separar_perguntas = linha.split('\n\n')

    lista_perguntas = []
    for linha_pergunta in separar_perguntas:
        lista_perguntas.append(linha_pergunta)

    return lista_perguntas

# Função que lê o arquivo "respostas"
def Ler_Respostas():
    with open('respostas.txt', 'r') as arquivo_respostas:
        linha_respostas = arquivo_respostas.read()
        separar_respostas = linha_respostas.split()

    lista_respostas = []
    for item_resposta in separar_respostas:
        lista_respostas.append(item_resposta)

    return lista_respostas

# Função que lê o arquivo "recordes" e separa os nomes do TOP 5
def Ler_Recordes_nomes():
    arquivo_recordes = open('recordes.txt', 'r')
    record_primeiro = arquivo_recordes.readline()
    record_segundo = arquivo_recordes.readline()
    record_terceiro = arquivo_recordes.readline()
    record_quarto = arquivo_recordes.readline()
    record_quinto = arquivo_recordes.readline()
    arquivo_recordes.close()

    
                
    separa_primeiro = record_primeiro.split()
    nome_primeiro = separa_primeiro[0]

    separa_segundo = record_segundo.split()
    nome_segundo = separa_segundo[0]

    separa_terceiro = record_terceiro.split()
    nome_terceiro = separa_terceiro[0]

    separa_quarto = record_quarto.split()
    nome_quarto = separa_quarto[0]

    separa_quinto = record_quinto.split()
    nome_quinto = separa_quinto[0]


    nomes = nome_primeiro + ' ' + nome_segundo + ' ' + nome_terceiro + ' ' + nome_quarto + ' ' + nome_quinto

    return nomes

# Função que lê o arquivo "recordes" e separa os pontos do TOP 5
def Ler_Recordes_pontos():
    with open('recordes.txt', 'r') as arquivo_recordes:
        record_primeiro = arquivo_recordes.readline()
        record_segundo = arquivo_recordes.readline()
        record_terceiro = arquivo_recordes.readline()
        record_quarto = arquivo_recordes.readline()
        record_quinto = arquivo_recordes.readline()

    separa_primeiro = record_primeiro.split()
    primeiro_lugar = separa_primeiro[1]

    separa_segundo = record_segundo.split()
    segundo_lugar = separa_segundo[1]

    separa_terceiro = record_terceiro.split()
    terceiro_lugar = separa_terceiro[1]

    separa_quarto = record_quarto.split()
    quarto_lugar = separa_quarto[1]

    separa_quinto = record_quinto.split()
    quinto_lugar = separa_quinto[1]

    pontuação = primeiro_lugar + ' ' + segundo_lugar + ' ' + terceiro_lugar + ' ' + quarto_lugar + ' ' + quinto_lugar

    return pontuação

# Função que faz as perguntas do quiz
def Perguntar(quest):
    pontos = 0
    pontos_easy = 10
    pontos_normal = 20
    pontos_hard = 30
    numero_quest = 1
    numero_lista = 0
    while numero_quest <= 5:
        lista_perguntas = Ler_Perguntas()
        lista_respostas = Ler_Respostas()
        if quest == numero_quest:
            print(lista_perguntas[numero_lista])

            resposta_primeira = input('\nQual sua resposta?: ')

            if resposta_primeira.upper() == lista_respostas[numero_lista]:
                print('\nResposta Correta!!')
                sleep(3)
                system('cls')
                quest += 1
                if numero_lista == 0 or numero_lista == 1:
                    pontos += pontos_easy
                elif numero_lista == 2 or numero_lista == 3:
                    pontos += pontos_normal
                elif numero_lista == 4:
                    pontos += pontos_hard
                    return pontos
            else:
                print('\nResposta errada!!!')
                sleep(3)
                system('cls')
                if numero_lista == 0:
                    return 0
                else:
                    return pontos

        numero_quest += 1
        numero_lista += 1
        
        

    input('...')

# Função que salva os recordes no arquivo "recordes"
def Salvar_Recordes(pontos, nome):
    nomes = Ler_Recordes_nomes()
    pontuação = Ler_Recordes_pontos()

    nomes_separar = nomes.split()
    pontuação_separar = pontuação.split()

    primeiro = nomes_separar[0] + ' ' + pontuação_separar[0] + '\n'
    segundo = nomes_separar[1] + ' ' + pontuação_separar[1] + '\n'
    terceiro = nomes_separar[2] + ' ' + pontuação_separar[2] + '\n'
    quarto = nomes_separar[3] + ' ' + pontuação_separar[3] + '\n'
    quinto = nomes_separar[4] + ' ' + pontuação_separar[4] + '\n'

    linha = nome + ' ' + str(pontos) + '\n'

    if pontos < int(pontuação_separar[4]):
        pontu = open('recordes.txt','w')
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.write(quinto)
        pontu.close()
    elif pontos >= int(pontuação_separar[4]) and pontos < int(pontuação_separar[3]):
        pontu = open('recordes.txt','w')
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.write(linha)
        pontu.close()
    elif pontos >= int(pontuação_separar[3]) and pontos < int(pontuação_separar[2]):
        pontu = open('recordes.txt','w')
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(linha)
        pontu.write(quarto)
        pontu.close()
    elif pontos >= int(pontuação_separar[2]) and pontos < int(pontuação_separar[1]):
        pontu = open('recordes.txt','w')
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(linha)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()
    elif pontos >= int(pontuação_separar[1]) and pontos < int(pontuação_separar[0]):
        pontu = open('recordes.txt','w')
        pontu.write(primeiro)
        pontu.write(linha)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()
    elif pontos >= int(pontuação_separar[0]):
        pontu = open('recordes.txt','w')
        pontu.write(linha)
        pontu.write(primeiro)
        pontu.write(segundo)
        pontu.write(terceiro)
        pontu.write(quarto)
        pontu.close()

    return pontu

# Função Principal
def main():
    print('*'*46)
    nome = input('* Oi! Tudo bem contigo?! Qual é o seu nome?  *\n* ')
    print('*'*46)
    system('cls')
    print('='*60)
    print('='*60)
    print('Seja bem-vindo(a) {}. Vamos iniciar o jogo agora!'.format(nome))
    print('='*60)
    print('='*60)
    sleep(3)
    system('cls')
    
    Ler_Perguntas()
    Ler_Respostas()
    pontos = Perguntar(1)
    Ler_Recordes_nomes()
    Ler_Recordes_pontos()
    Salvar_Recordes(pontos, nome)

    system('cls')

    print('='*10)
    print('='*10)
    print('\n RANKING: \n')
    print('='*10)
    print('='*10)
    with open('recordes.txt', 'r') as recorde:
        for linha in recorde:
            print(linha)

    sleep(5)
    

if __name__ == "__main__":
    main()
