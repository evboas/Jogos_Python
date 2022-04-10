# Jogo da Forca e Jogo da Adivinhação em Python

Essa é a versão do jogo da forca e jogo da adivinhação em linguagem Python.
Nesta versão do jogo da forca foi implementado uma melhoria na parte gráfica.

Ambos os jogos foram desenvolvidos durante estudos do curso básico de Python parte 1 e 2 da Alura e são jogados via terminal.

## Rodando o jogo

 - Para jogar você precisa ter o Python 3 instalado no computador.

Basta abrir o terminal na pasta do código e executar o comando:

``` python3 jogos.py ```

Ou ainda executar o código por meio da sua IDE.

Também é possível rodar o jogo executando o mesmo comando para os arquivos ``forca.py`` ou ``adivinhacao.py``. 

## Jogo da  adivinhação

O jogo da adivinhação é simples de ser jogado, uma vez que ao iniciar você deve tentar adivinhar o número (de 1 a 100) que o computador sorteou aleatóriamente.

Inicialmente o jogo perguntará qual o nível de dificuldade que deseja, sendo possível escolher entre três opções:

1. ***Fácil***: neste nível o jogador terá a possibilidade de fazer 10 tentativas;
1. ***Médio***:neste nível o jogador terá a possibilidade de fazer 8 tentativas;
1. ***Dificil***:neste nível o jogador terá a possibilidade de fazer 5 tentativas.

Assim que o nível de dificuldade for escolhido se apresentará a seguinte tela:

![Tela de inicio do jogo](/Imagens/Captura%20de%20tela%20-%20Jogo%20adivinhacao.png)

 A cada "chute" o jogo deve informar se o seu número foi maior ou menor que o número sorteado pelo computador.

![Tentativas](/Imagens/Captura%20de%20tela%20-%20Jogo%20adivinhacao2.png)

## Jogo da Forca

O jogo da forca é um clássico conhecido por todos.

As palavras são sorteadas pelo computador e estão registradas no arquivo ```palavras.txt```, onde o usuário poderá registrar outras palavras.

O jogo foi programado com os desenhos característicos para o jogo de forca.

![jogo da forca](/Imagens/Forca.png)