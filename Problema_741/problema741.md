# [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/description/)

Você recebe uma **grade** **n × n** representando um campo de cerejas. Cada célula é um de três possíveis números inteiros:

- **0** significa que a célula está vazia, então você pode passar por ela.

- **1** significa que a célula contém uma cereja que você pode pegar e passar por ela.

- **-1** significa que a célula contém um espinho que bloqueia seu caminho.

Retorne o número máximo de cerejas que você pode coletar seguindo as regras abaixo:

- Começando na posição **(0, 0)** e alcançando **(n - 1, n - 1)** movendo-se para direita ou para baixo através de células de caminho válidas (células com valor **0** ou **1**).

- Depois de chegar a **(n - 1, n - 1)**, retornando para **(0, 0)** movendo-se para esquerda ou para cima através de células de caminho válidas.

- Ao passar por uma célula de caminho que contém uma cereja, você a pega, e a célula se torna uma célula vazia **(0)**.

- Se não houver um caminho válido entre **(0, 0)** e **(n - 1, n - 1)**, então nenhuma cereja pode ser coletada.

## Exemplo 1:
![exemplo 1](https://github.com/projeto-de-algoritmos-2025/PD_ExerciciosResolvidos-Leetcode/blob/ed148c2a4cfda3ecd8ef97213489ebe7093ecc73/Problema_741/img/ex1jpg.jpg)<br>
*exemplo 1* <br>
**Entrada: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]**
**Saída: 5**
#### Explicação:
O jogador começou em (0, 0) e foi para baixo, baixo, direita, direita para chegar a (2, 2).
4 cerejas foram pegas durante essa única viagem, e a matriz se torna [[0,1,-1],[0,0,-1],[0,0,0]].
Então, o jogador foi para a esquerda, para cima, para cima, para a esquerda para retornar para casa, pegando mais uma cereja.
O número total de cerejas pegas é 5, e este é o máximo possível.

## Exemplo 2:
**Entrada: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]**
**Saída: 0**

## Restrições:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- grid[i][j] is -1, 0, ou 1.
- grid[0][0] != -1
- grid[n - 1][n - 1] != -1

# Solução
![Problema 1235](https://github.com/projeto-de-algoritmos-2025/PD_ExerciciosResolvidos-Leetcode/blob/ed148c2a4cfda3ecd8ef97213489ebe7093ecc73/Problema_741/img/sol71.png) <br>
*Problema 1235 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/PD_ExerciciosResolvidos-Leetcode/blob/ed148c2a4cfda3ecd8ef97213489ebe7093ecc73/Problema_741/problema741.py)