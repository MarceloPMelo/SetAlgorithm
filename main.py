class Set:
    def __init__(self):
        self.elements = []
    
    def add(self, e):
        if e not in self.elements:
            self.elements.append(e)
            return True
        return False
    
    def add_all(self, other):
        changed = False
        for e in other.elements:
            if e not in self.elements:
                self.elements.append(e)
                changed = True
        return changed
    
    def contains(self, e):
        return e in self.elements
    
    def equals(self, other):
        if len(self.elements) != len(other.elements):
            return False
        for e in self.elements:
            if e not in other.elements:
                return False
        return True
    
    def __iter__(self):
        return iter(self.elements)
    
    def remove(self, e):
        if e in self.elements:
            self.elements.remove(e)
            return True
        return False
    
    def size(self):
        return len(self.elements)
    
    def to_list(self):
        return list(self.elements)


def get_subsets(input_set):

    """
    Essa função gera todos os subconjuntos (o conjunto das partes) de um Set A com até 4 elementos.
    - Primeiro, verifica se A tem mais que 4 elementos; se sim, levanta um ValueError.
    - Pega os elementos de A como uma lista, usando A.toArray(), guardando em items.
    - Cria um Set vazio chamado result para armazenar os subconjuntos (cada um também é um Set).
    - Usa uma função auxiliar backtrack(start, current) para construir os subconjuntos de forma recursiva:
      - Cria um novo Set subset, copia os elementos escolhidos até agora (current) com subset.addAll(current).
      - Adiciona esse subset em result (evitando repetições com iterator() e equals()).
      - Para cada índice i começando em start até o fim da lista items:
        - Se current ainda não tem items[i], adiciona ele com current.add(items[i]).
        - Chama backtrack(i + 1, current) para continuar construindo o subconjunto.
        - Depois remove items[i] de current para testar outras possibilidades.
    - No final, retorna result com todos os subconjuntos, incluindo o vazio.
    - Fora da função, para mostrar o resultado, percorra result.iterator() e use toArray() em cada subset.
    """


    if input_set.size() > 4:
        raise ValueError("No more than 4 elements allowed.")
    
    items = input_set.to_list()
    result = Set()
    
    def already_exists(container, candidate):
        for s in container:
            if s.equals(candidate):
                return True
        return False
    
    def backtrack(start, current):
        subset = Set()
        subset.add_all(current)
        if not already_exists(result, subset):
            result.add(subset)
        
        for i in range(start, len(items)):
            if not current.contains(items[i]):
                current.add(items[i])
                backtrack(i + 1, current)
                current.remove(items[i])
    
    backtrack(0, Set())
    return result


def main():
    s = Set()
    while True:
        raw = input("Digite até 4 elementos separados por vírgula (ex: x,x,x,x): ")
        elements = [e.strip() for e in raw.split(",") if e.strip()]
        if len(elements) > 4:
            print("Limite máximo é 4 elementos. Tente novamente.")
            continue
        
        parsed = []
        for el in elements:
            try:
                parsed.append(int(el))
            except:
                parsed.append(el)
        
        for p in parsed:
            s.add(p)
        break
    
    subsets = get_subsets(s)
    output = [sub.to_list() for sub in subsets]
    print(output)


if __name__ == "__main__":
    main()
