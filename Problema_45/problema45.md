# [45. Jogo dos Saltos II (Jump Game II)](https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=dynamic-programming)

**Dificuldade:** Média  
**Tópicos:** Programação Dinâmica  
**Descrição:**

Você recebe um array de inteiros `nums` indexado em 0 e de comprimento `n`. Você começa posicionado em `nums[0]`.

Cada elemento `nums[i]` representa o **tamanho máximo de salto para frente** a partir do índice `i`. Em outras palavras, se você está em `nums[i]`, pode saltar para qualquer posição `nums[i + j]`, onde:

- `0 <= j <= nums[i]` e  
- `i + j < n`

Retorne o **menor número de saltos necessários para chegar a `nums[n - 1]`**.

Os casos de teste são garantidos de forma que é **sempre possível** chegar ao último índice.

---

## Exemplos

### Exemplo 1:

**Entrada:**  
`nums = [2,3,1,1,4]`  

**Saída:**  
`2`  

**Explicação:**  
O número mínimo de saltos para alcançar o último índice é 2.  
Pule 1 passo do índice 0 para o índice 1, depois 3 passos até o final.

---

### Exemplo 2:

**Entrada:**  
`nums = [2,3,0,1,4]`  

**Saída:**  
`2`  

---

## Restrições:

- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 1000`
- É garantido que você pode alcançar `nums[n - 1]`.
