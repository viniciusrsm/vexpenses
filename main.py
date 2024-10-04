# EXECUTE O PROGRAMA PARA CONFERIR AS RESPOSTAS #

import pandas as pd

# INICIA O DATAFRAME
df = pd.read_csv('netflix_titles.csv')

# PERGUNTA 1
def question1():
    columns = list(df.columns)
    print(f'Existem {len(columns)} colunas, sendo elas:')
    print(*columns, sep=', ')

# PERGUNTA 2
def question2():
    # Cria uma lista de booleanos, onde true significa que o valor da coluna type é 'Movie'
    isMovieList = (df.type.values == 'Movie')
    # Calcula a sum da lista anterior, onde cada true irá adicionar 1 na soma final e false 0
    movieCount = isMovieList.sum()
    print(f'Existem {movieCount} filmes disponíveis')

# PERGUNTA 3
def question3():
    """ Como podem existir vários diretores em um único filme, 
    primeiro separamos a Serie e depois juntamos todos os diretores separados em uma nova Serie """
    directorList = df.director.str.split(', ', expand=True).stack()

    # Ordena os diretores com maior incidência e seleciona os cinco primeiros
    topDirectors = directorList.value_counts().head(5)

    print('{:17}'.format('Diretores') + 'Quantidade de filmes')
    print(topDirectors.to_string())

def question4():
    # Faz a separação de diretores e cast em listas
    df['director'] = df.director.str.split(', ')
    df['cast'] = df.cast.str.split(', ')

    # Cria uma tabela apenas com as duas colunas relevantes e retira os valores nulos
    dirCast = df[['director', 'cast']].dropna()
    
    # Cria outra coluna chamada overlap, onde ela é igual a uma lista da interseção entre diretor e atores
    dirCast['overlap'] = [
        list(set(a) & set(b))
        if set(a) & set(b) != set() else None 
        for a, b in zip(dirCast.director, dirCast.cast)
    ]

    # Espalha os conteúdos das lista, separando todos os valores de forma individual
    explode = dirCast.overlap.dropna().explode().value_counts().head(5)
    print(f'{'Diretor':<25}Filmes próprios atuados')
    for i, v in explode.items():
        print(f'{i:<25}{v}')

def mainFunction():
    print('#-'*35 + '\n')
    print('Seja bem-vindo ao Sistema VExpenses')
    print('Utilize os números na tabela abaixo para acessar as funções!\n')
    print('#-'*35)
    text = """
1 - Quantas colunas estão presentes no dataset?
2 - Quantos filmes estão disponíveis na Netflix?
3 - Quem são os 5 diretores com mais filmes e séries na plataforma?
4 - Quais diretores também atuaram como atores em suas próprias produções?
q - Sair do programa
"""
    print(text)
    while (True):
        req = input()
        match req:
            case 'q': break
            case '1': question1()
            case '2': question2()
            case '3': question3()
            case '4': question4()
            case _: print('Insira um input válido!')
        print()

if __name__ == "__main__":
    mainFunction()


#pontos importantes
# *raúl campos aparece com um sobrenome a mais em uma ocasião, mas não é computado pois poderia ser outra pessoa