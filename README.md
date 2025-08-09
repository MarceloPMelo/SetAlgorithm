# SetAlgorithm

Gera todos os subconjuntos (conjunto das partes) de um conjunto `A` com até 4 elementos, usando uma implementação simples da estrutura `Set` e backtracking.

## Requisitos
- Python 3.8+

## Como executar
No terminal, a partir da raiz do projeto:

```bash
python3 main.py
```

## Uso
Ao executar, o programa solicita a entrada dos elementos:

```
Digite até 4 elementos separados por vírgula (ex: x,x,x,x):
```

- Você pode inserir números e/ou textos. O programa tenta converter cada item para inteiro; se falhar, mantém como texto.
- O limite é de 4 elementos. Se ultrapassar, você será avisado e poderá tentar novamente.

Exemplos de entrada válidos:
- `1,2,3`
- `1, 2, 3, 4`
- `a,b,c`
- `1, a, 2`

## Saída
O programa imprime todos os subconjuntos como uma lista de listas. Por exemplo, para a entrada `1,2,3` a saída conterá algo como:

```python
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
```

A ordem pode variar, mas todos os subconjuntos (incluindo o vazio) estarão presentes.

## Implementação
- A classe `Set` fornece: `add`, `addAll`, `contains`, `equals`, `iterator`, `remove`, `size`, `toArray`.
- A função principal `getSubSets(A)`:
  - Valida `A.size() <= 4`.
  - Usa `toArray()` para obter os itens e um método auxiliar `generate_subsets(start, current)` para explorar as combinações.
  - Cada subconjunto é copiado com `addAll` para um novo `Set` e inserido em `result`.
  - `iterator()` + `equals()` são usados para evitar duplicatas ao inserir no resultado.

## Estrutura do projeto
- `main.py`: implementação da estrutura `Set`, da função `getSubSets` e interface de linha de comando.
- `README.md`: este arquivo.

## Notas
- O limite de 4 elementos é imposto para aderir ao enunciado e manter a execução simples.
- A lógica funciona para tipos mistos (inteiros e strings), mas evite elementos não hasháveis/complexos.