# Versão recursiva pura
def vence(n: int) -> bool:
    if n == 0:
        return False  # posição perdedora

    for i in [1, 2, 3]:
        if n - i >= 0 and not vence(n - i):
            return True  # existe uma jogada que deixa o oponente em P

    return False  # todas as jogadas deixam o adversário vencer

print(vence(4))  # False
print(vence(5))  # True
print(vence(7))  # True
print(vence(8))  # False


# Função recursiva com memoização

from functools import lru_cache
@lru_cache(maxsize=None)
def vence(n: int) -> bool:
    if n == 0:
        return False  # posição perdedora

    for i in [1, 2, 3]:
        if n - i >= 0 and not vence(n - i):
            return True

    return False  # todas as jogadas deixam o adversário vencer


print(vence(4))  # False
print(vence(5))  # True
print(vence(10))  # True
print(vence(100))  # False
print(vence(1000))  # True



