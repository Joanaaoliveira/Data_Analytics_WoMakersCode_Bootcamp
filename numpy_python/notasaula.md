## Conhecendo a biblioteca Numpy
cria um array de 3 linhas e duas colunas de zeros.
``` 
np.zeros((3,2)) 
``` 
cria um array de 1 até 10, funciona como o método range() do python.
``` 
np.arrange(1,11)
``` 
### Conversão e coerção

dtype como argumento
``` 
arr_float32 = np.array([2.14, 6.25, 160.87], dtype=np.float32)
``` 
**Conversão**

arr_vf = np.array([[true, false], [true, true]], dtype = np.bool8)
arr_vf.astype(np.int32)

**Coerção**
``` 
np.array(['pedra', False, 42, 42.42])
``` 
**Hierarquia de coerção**

* Adicionar um float a um array de int mudará todos os valores para float.
* Adicionar um inteiro em um array de booleanos transformará todo o array em inteiros.

### Index

Indexa linha e coluna

Lembrando que o index começa em 0

``` 
arr = np.array([2, 4, 6, 8])
arr[2]
-- retorna 6
```

**Ordenar um array**
```
np.sort(variavel)
```

Para fazer uma ordenação considerando por linha
```
np.sort(variavel, axis=0)
```
### Eixos (axis)

axis 0 - horizontal <br/>
axis 1 - vertical







