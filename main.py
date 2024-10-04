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

    print('{:17}'.format('Diretor') + 'Quantidade de filmes')
    print(topDirectors.to_string())

def question4():
    df4 = df.copy()
    # Faz a separação de diretores e cast em listas
    df4['director'] = df4.director.str.split(', ')
    df4['cast'] = df4.cast.str.split(', ')

    # Cria uma tabela apenas com as duas colunas relevantes e retira os valores nulos
    dirCast = df4[['director', 'cast']].dropna()
    
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

def question5():
    # Cria uma cópia do dataframe para não afetar o original
    df5 = df.copy()

    # Separa os valores de 'cast' em uma lista na mesma célula
    df5['cast'] = df5.cast.str.split(', ')

    # Remove todos os valores que sejam NaN ou não tenham mais de um ator
    castFilter = df5.cast.dropna()[df5.cast.dropna().apply(lambda x: len(x) > 1)]

    # Ordena os elencos que aparecem com maior incidência juntos e seleciona os primeiro 5
    castCount = castFilter.value_counts().head(5)
    print(castCount.to_string().replace('cast', 'Os elencos que mais trabalharam juntos são:'))

def question6():
    # Ordena os anos por ordem de mais lançamentos e seleciona os primeiros 5
    topYears = df.release_year.value_counts().head(5)

    print(topYears.to_string().replace('release_year', 'Anos com maiores lançamentos são:'))

def question7():
    # Separa todos os gêneros de forma individual
    genreExplode = df.listed_in.str.split(', ').explode()

    # Ordena os gêneros por ordem de ocorrência e seleciona os primeiros 5
    genreCount = genreExplode.value_counts().head(5)

    print(genreCount.to_string().replace('listed_in', 'Gêneros mais ocorrentes são:'))

def question8():
    # Separa todos os países de forma individual
    countryExplode = df.country.str.split(', ').explode()

    # Ordena os países por ordem de ocorrência e seleciona os primeiros 5
    countryCount = countryExplode.value_counts().head(5)

    print(countryCount.to_string().replace('country', 'Os paises com mais filmes são:'))

def question9():
    # Cria uma cópia do dataframe para não afetar o original
    df9 = df

    # Gera dois novos dataframes com todos os diretores e generos separados
    explodeDir = df9.director.str.split(', ').explode().reset_index()
    explodeGenre = df.listed_in.str.split(', ').explode().reset_index()

    # Unifica os dois dataframes
    merge = explodeDir.merge(explodeGenre).dropna()

    # Ordena os pares de diretores e gêneros que mais aparecem juntos e seleciona os 5 primeiros
    mergeCount = merge.value_counts(['director', 'listed_in']).head(5)
    
    print('Diretores que mais repetiram gêneros são:')
    print(mergeCount.to_string().replace('director', 'Diretor').replace('listed_in', ' Gênero'))    

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
5 - Quais elencos mais trabalharam juntos?
6 - Quais anos possuem a maior quantidade de obras lançadas?
7 - Quais gêneros são os mais ocorrentes?
8 - Quais países têm mais filmes?
9 - Quais diretores trabalharam mais vezes com o mesmo gênero?
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
            case '5': question5()
            case '6': question6()
            case '7': question7()
            case '8': question8()
            case '9': question9()
            case _: print('Insira um input válido!')
        print()

def test():
    question5()

if __name__ == "__main__":
    mainFunction()