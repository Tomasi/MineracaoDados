# Domínio de Exemplo (Techniques of Data Mining In Healthcare)

Artigo - [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=82289448146b86c6160bf5225bd5e3cea35a8c57]

A mineração de dados desempenha um papel de extrema importância no domínio da saúde, uma vez que as organizações de saúde em todo o mundo armazenam os dados relacionados à saúde em formato eletrônico. Esses dados de saúde contêm informações detalhadas sobre pacientes e todas as partes envolvidas na indústria da saúde. A quantidade de dados desse tipo está aumentando rapidamente, levando a uma complexidade significativa. Tradicionalmente, extrair informações significativas desses dados era uma tarefa árdua, mas avanços nas áreas de estatística, matemática e outras disciplinas tornaram possível identificar padrões relevantes.

A mineração de dados desempenha um papel crucial ao extrair padrões significativos que anteriormente eram desconhecidos. Esses padrões podem ser integrados ao conhecimento existente e utilizados para tomar decisões essenciais. Existem várias vantagens na aplicação da mineração de dados na área da saúde, como a detecção de fraudes e abusos, a oferta de tratamentos médicos mais eficazes a preços razoáveis, a detecção precoce de doenças e a criação de sistemas inteligentes de apoio à decisão em saúde.

As técnicas de mineração de dados são extremamente úteis no domínio da saúde, pois melhoram os serviços médicos prestados aos pacientes e auxiliam as organizações de saúde em várias decisões de gerenciamento médico. Alguns dos serviços oferecidos pelas técnicas de mineração de dados na área da saúde incluem a estimativa do tempo de internação em um hospital, a classificação de hospitais, tratamentos mais eficazes, detecção de fraudes em seguros médicos, readmissão de pacientes, identificação de métodos de tratamento melhores para grupos específicos de pacientes e a construção de sistemas eficazes de recomendação de medicamentos.

Métodos de clusterização baseados em densidade desempenham um papel muito importante na pesquisa biomédica porque são capazes de lidar com qualquer cluster de forma arbitrária. Pesquisas recentes comprovam que este método pode ser eficiente e eficaz para extrair padrões significativos de um banco de dados muito grande composto principalmente por imagens biomédicas

Usando a "propriedade Apriori", permitindo que a mineração de associações fosse aplicada a bancos de dados reais para extrair regras de associação. A fim de descobrir os padrões frequentes e as relações interessantes entre um conjunto de itens de dados no repositório de dados, a associação é uma das abordagens mais essenciais da mineração de dados. Isso tem um grande impacto no campo da saúde para detectar as relações entre doenças, estado de saúde e sintomas. Pesquisadores atualmente usam essa abordagem para determinar as relações entre diversas doenças e os medicamentos prescritos para elas. Essa abordagem é amplamente utilizada pelas companhias de seguros de saúde para identificar fraudes e abusos.


![image](https://github.com/Tomasi/MineracaoDados/assets/61890715/336f4f9d-46cf-4146-91c4-907360f2b969)

![image](https://github.com/Tomasi/MineracaoDados/assets/61890715/4474f8d2-703d-4009-88ec-a974050392cc)

# Questões Analísticas (QA)

Usando o exemplo de classificação para doenças cardiovasculares, será formulado três questões analíticas:

- O fator idade é um dado de importância para classificar o paciente?
- Qual a faixa considerada normal de frequência cardiaca para as idades contidas no modelo?
- Qual a faixa considerada normal de pressão arterial para as idades contidas no modelo?

# Entendimento e Preparação de Dados

| Id | Age | Gender | Heart Rate (bpm) | Blood Pressure (mmHg) | Heart Problem | BMI | Cholesterol Level | Diabetes | Smoking | Insurance Provider | Address              | Contact Number    |
|----|-----|--------|-------------------|------------------------|--------------|-----|-------------------|----------|---------|--------------------|----------------------|-------------------|
| 1  | 45  | Male   | 72                | 120/80                 | No           | 26.5| 190               | No       | No      | ABC Health         | 123 Main St, City    | (555) 123-4567    |
| 2  | 62  | Female | 78                | 140/90                 | Yes          | 29.2| 220               | Yes      | No      | XYZ Insurance      | 456 Elm St, Town     | (555) 987-6543    |
| 3  | 35  | Male   | 65                | 110/70                 | No           | 22.0| 160               | No       | Yes     | ABC Health         | 789 Oak Ave, Village | (555) 456-7890    |
| 4  | 50  | Female | 80                | 130/85                 | No           | 27.8| 200               | No       | Yes     | LMN Insurance      | 101 Pine Rd, City    | (555) 789-0123    |
| 5  | 55  | Male   | 68                | 125/82                 | Yes          | 25.3| 180               | No       | No      | XYZ Insurance      | 222 Cedar Ln, Town  | (555) 321-9876    |
| 6  | 42  | Female | 75                | 118/78                 | No           | 23.7| 175               | No       | No      | DEF Health         | 333 Maple St, City  | (555) 234-5678    |
| 7  | 68  | Male   | 70                | 135/88                 | Yes          | 28.1| 210               | Yes      | No      | LMN Insurance      | 444 Birch Ave, Town | (555) 876-5432    |
| 8  | 47  | Female | 72                | 122/79                 | No           | 26.0| 195               | No       | Yes     | DEF Health         | 555 Walnut Rd, City | (555) 345-6789    |
| 9  | 58  | Male   | 76                | 128/84                 | Yes          | 27.5| 205               | No       | No      | GHI Insurance      | 666 Oakwood Ln, Town| (555) 987-6543    |
| 10 | 40  | Female | 68                | 115/75                 | No           | 24.6| 170               | No       | Yes     | GHI Insurance      | 777 Cedar Ave, City | (555) 234-5678    |


