import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_excel('C:/Users/Igor Tomasi/dev/MineracaoDados/N2/sfo 2018_data file_final_Weightedv2.xlsx')
df.columns = df.columns.str.strip()

colunas_analise = ['NETPRO', 'Q20Age', 'Q21Gender', 'Q22Income', 'Q23FLY', 'Q5TIMESFLOWN', 'Q6LONGUSE']

data = df[colunas_analise].dropna()

print(f"Dados em análise de outlier \n{data}")

# Padronização dos dados para ter média 0 e desvio padrão 1
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

kmeans = KMeans(n_clusters=2) 
kmeans.fit(scaled_data)

# Adicionado etiquetas de cluster ao DataFrame
df['Cluster'] = kmeans.labels_

# centroides de cada cluster
cluster_centers = kmeans.cluster_centers_

# Distâncias Euclidianas de cada ponto de dados em relação aos centroides
distances = []
for i in range(len(scaled_data)):
    distances_to_centers = np.linalg.norm(scaled_data[i] - cluster_centers, axis=1)
    distances.append(distances_to_centers)

average_distances = [distances[i][df['Cluster'].iloc[i]] for i in range(len(scaled_data))]

outlier_threshold = 3.0 # Limite considerado um outlier, maior ou igual a esse valor é um outlier
outliers = df[np.array(average_distances) >= outlier_threshold]

# Demonstração de cada cluster (Tamanho (%) em relação ao tamanho da amostra de dados)

cluster_sizes = df['Cluster'].value_counts(normalize=True)

for cluster, size in cluster_sizes.items():
    print(f"Cluster {cluster} - Tamanho: {size * 100:.2f}%")
    cluster_data = df[df['Cluster'] == cluster]
    cluster_profile = cluster_data[colunas_analise].mean()
    print("Perfil do grupo:")
    print(cluster_profile)
    print("\n")

print("Valores Atípicos:")
print(outliers)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# Plotagem dos cluster 
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_, cmap='viridis')
plt.title('Agrupamento de Passageiros')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()