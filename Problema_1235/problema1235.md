# [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/)

Temos **n** trabalhos, onde cada trabalho é agendado para ser feito de **startTime[i]** a **endTime[i]**, rendendo um lucro de **profit[i]**.

São dados os arrays **startTime**, **endTime** e **profit**. Retorne o lucro máximo que você pode obter, de forma que não haja dois trabalhos no subconjunto escolhido com intervalos de tempo sobrepostos.

Se você escolher um trabalho que termina no tempo **X**, poderá iniciar outro trabalho que começa no tempo **X**.

## Exemplo 1:
![exemplo 1]( )<br>
*exemplo 1* <br>
**Entrada: startTime  = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]**
**Saída: 120**
#### Explicação:
O subconjunto escolhido é o primeiro e o quarto trabalho.
Intervalo de tempo [1 - 3] + [3 - 6], obtemos um lucro de 120 = 50 + 70.

## Exemplo 2:
![exemplo 2]( )<br>
*exemplo 2* <br>
**Entrada: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]**
**Saída: 150**
#### Explicação:
Explicação: O subconjunto escolhido é o primeiro, o quarto e o quinto trabalho.
Lucro obtido 150 = 20 + 70 + 60.

## Exemplo 3:
![exemplo 3]( )<br>
*exemplo 3* <br>
**Entrada: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]**
**Saída: 6**

## Restrições:
- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
- 1 <= startTime[i] < endTime[i] <= 10^9
- 1 <= profit[i] <= 10^4

# Solução
![Problema 1235]( ) <br>
*Problema 1235 aceitação*

[Solução]( )