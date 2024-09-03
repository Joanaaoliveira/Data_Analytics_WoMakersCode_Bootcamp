## Estatística com Python: Frequências e Medidas

Medidas de tendencia central
média
mediana
moda

### Análise de disperação de variáveis
São medidas que buscam resumir como os dados estão destribuídos. O quão concentrados os dados estão em determinados intervalos e o grau de variação das informações (somente variáveis numéricas)

**Amplitude** - Diferença entre o maior e o menor valor dos dados.
**Variância** - Número que nos dias o quão distante da média os dados estão.
**Desvio padrão** - Também nos diz o quão distante da média estão os dados. É a raiz quadrada da variância - preserva a unidade de medida original.

### Variância Populacional vs Amostral
As medidas populacionais podem ser usadas quando estamos analisando ados de uma população completa "sem margem de erro"
Já as medidas amostrais são mais utilizadas no dia a dia. Utiliza-se elas no caso de ter uma amostra de dados para analisar.
A diferença das formulas está no denominador. No caso amostral dividimos por N-1, para aplicar um fator de correção e no caso populacional por N.

### Análise Exploratória de Variáveis Numéricas 
Quando vamos analisar dados é importante começarmos por uma análise exploratória dos dados.
Para variáveis numéricas podemos analisar as seguintes características:
* Média, moda, mediana;
* Variância e desvio padrão;
* Valores mínimos e máximos;
* Análise do histograma;
* Análise do boxplot;
* Verificar outliers;
* Verificar valores nulos ou faltantes.

Considerando cada variável uma coluna.

**Valores nulos e variáveis numéricas**
Análise dos valores nulos é uma etapa muito importante na análise exploratória dos dados. Em muitos caso, no dia a dia, podemos ter variáveis importantes e pouco preenchidas. Neste caso quando devemos substituir valores nulos? e por quais valores substituir?
**A substituição vai ser a critério do analista e da análise**
Mas uma boa prática é:
* Verificar se a informação faltante, assim como o outlier, possui sentido de negócio;
* Substituir pela média, moda, mediana;
* Fazer um gráfico de barras de quantidade ou % de valores faltantes para cada variável (coluna)
** Sempre que substituido um valor, documentar isso para ficar claro que a análise precisou passar por esse tratamento e a pessoa que pegar sua análise entender o que foi realizado, e quais caminhos foram tomados.
** Outro ponto importante é deixar o gráfico de valores faltantes para cada variável (coluna) na documentação, para deixar mais claro a opção em deletar ou substituir os valores.
** Uma outra dica é substituir por um valor aleatório que seja muito diferente do grupo de dados, pois neste caso em colunas com sentido de negócio pode ajudar a identificar alguma fraude ou algo do tipo. Então o valor pode ser -1 ou 999.

### Análise Exploratória de Variáveis Categóricas
Para variáveis categóricas podemos analisar as seguintes características:
1. Moda dos dados
2. Análise de frequência das categorias ou cardinalidade:
    a. Quantas categorias existem?
    b. Qual a frequência de cada uma das categorias? (gráfico de barras)
3. Agrupamento de variáveis de alta cardinalidade
4. Substituição de valores nulos: ou pela Moda ou criar a categoria "Nulo"
