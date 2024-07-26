## Notas de aula referente ao módulo 03 do curso de Git e Github da WoMakersCode em parceiria com a Potencia Feminina. 

## Criando uma nova branch pelo terminal

Comando para a criação de uma nova branch via terminal

### git checkout -b (nome da nova branch)

### git branch 
**git branch** = para saber quais branchs tem e a que estiver verde é a que eu estou conectada, portanto todo push que eu fizer será nesta branch que está selecionada.

**git branch checkout (nome da branch)** = para mudar de branch.

## Para criar a branch pelo github
1) Acessar o repositório;
2) Ir na sessão de listagem das branchs;
3) Inserir o nome da nova branch;
4) Confirmar a criação dessa nova branch.

### Caso queira excluir uma branch pelo github:
1) Vá na sessão de listagem das branchs 
2) Clique no ícone de lixeira para realizar a exclusão dessa branch.

## Para fazer o merge entre a branch e o main
### git checkout main
Retornará para o main, ou seja, sairá da branch

### git pull 
Esse código vai trazer todos os arquivos da branch para meu main.

### git status
Permite conferir se houve modificações, normalmente vem a mensagem "Your branch is ahead of 'origin/main' by "X" commit."

### git push 
Para atualizar tudo e fazer o merge.

>Geralmente é uma boa prática quando feito o merge deletar a branch. Pois todos os arquivos que estão no nosso main já serão os principais, pois foram aprovados.



