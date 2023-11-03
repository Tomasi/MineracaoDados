import pandas as pd

df = pd.read_csv('C:/Users/Igor Tomasi/dev/MineracaoDados/N2/titanic3.csv', sep=';')

df['age'] = df['age'].str.replace(',', '.')
df['age'] = pd.to_numeric(df['age'], errors='coerce')

media_sexo_idade = df.groupby('sex')['age'].mean()
sexo_maior_idade = media_sexo_idade.idxmax()

print(f"O sexo com a maior média de idade é: {sexo_maior_idade}")
print("\n")

descritiva_generos = df.groupby('sex').describe()
descriva_classe = df.groupby('pclass').describe()
print("Estatísticas descritivas para cada gênero:")
print(descritiva_generos)
print("\n")

print("Estatísticas descritivas para cada classe de passageiros:")
print(descriva_classe)
print("\n")

sobreviventes = df[df['survived'] == 1.0]
sobreviventes_generos = sobreviventes['sex'].value_counts()
sobreviventes_classes = sobreviventes['pclass'].value_counts()

genero_mais_sobrevivente = sobreviventes_generos.idxmax()
classe_mais_sobrevivente = sobreviventes_classes.idxmax()

print("Número de sobreviventes por gênero:")
print(sobreviventes_generos)

print("\nGênero com o maior número de sobreviventes:")
print(genero_mais_sobrevivente)

print("\nNúmero de sobreviventes por classe:")
print(sobreviventes_classes)

print("\nClasse com o maior número de sobreviventes:")
print(classe_mais_sobrevivente)