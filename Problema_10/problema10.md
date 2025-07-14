# 10. Correspondência de Expressão Regular (Regular Expression Matching)

**Dificuldade:** Difícil  
**Tópicos:** Programação Dinâmica  
**Descrição:**

Dado uma string de entrada `s` e um padrão `p`, implemente a correspondência de expressão regular com suporte para os caracteres especiais `.` e `*`, onde:

- `.` corresponde a **qualquer caractere único**.  
- `*` corresponde a **zero ou mais ocorrências do elemento anterior**.

A correspondência deve **cobrir toda a string de entrada**, ou seja, **não pode ser parcial**.

---

## Exemplos:

### Exemplo 1:

**Entrada:**  
`s = "aa"`  
`p = "a"`  

**Saída:**  
`false`  

**Explicação:**  
"a" não corresponde à string inteira "aa".

---

### Exemplo 2:

**Entrada:**  
`s = "aa"`  
`p = "a*"`  

**Saída:**  
`true`  

**Explicação:**  
`*` significa "zero ou mais ocorrências do elemento anterior", no caso, 'a'.  
Portanto, ao repetir 'a' uma vez, a string se torna "aa".

---

### Exemplo 3:

**Entrada:**  
`s = "ab"`  
`p = ".*"`  

**Saída:**  
`true`  

**Explicação:**  
`.*` significa "zero ou mais de qualquer caractere", o que cobre qualquer string.

---

## Restrições:

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- A string `s` contém apenas letras minúsculas do alfabeto inglês.
- O padrão `p` contém apenas letras minúsculas do alfabeto inglês, `.` e `*`.
- É garantido que para cada ocorrência do caractere `*`, haverá um caractere válido anterior para ser correspondido.
