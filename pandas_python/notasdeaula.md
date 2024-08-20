### Estatísticas resumidas em python

.median() - calcula mediana
.mode() - calcula a moda - valores mais frequentes.
.min() - retorna o valor minimo
.max() - retorna o valor máximo
.var() - calcula a variância, uma medida da dispersão de dados
.std() - calcula o desvio padrão, indicando a dispersão média dos dados em relação à média
.sum() - soma todos os valores do conjunto de dados
.quantile() - calcula um percentil específico em um conjunto de dados, indicando o valor abaixo do qual uma determinada porcentagem dos dados está.

### Sobre Index
set_index('nome_coluna') -- pode colocar uma coluna do df como índice
reset_index() - redefine os índices
reset_index(drop=True) - a coluna que antes era index é excluída do df

**Usar index facilita filtrar algo**
exemplo, usando um nome como index posso utilizar o seguinte código, exemplo:
df_cachorros.loc[['Max', 'Zoe']] -- o nome já é index neste caso



