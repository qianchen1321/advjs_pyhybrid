#coding:utf-8

a : int = 2
print('5 + a', 5 + a)

def add(a: int) -> int:
    return a + 1

print(add(1.5))

from typing import List, Tuple, Dict, Mapping, Set, AbstractSet, Sequence, NoReturn
name: List[str] = ['Germey', 'Guido']
version: Tuple[int, int, int] = (3, 7 , 4)
operation: Dict[str, bool] = {"show": False, 'sort': True}

def size(rect: Mapping[str, int]) -> Dict[str, int]:
    return {'width': rect['width'] + 100, 'height': rect['width'] + 100}

def describe(s: AbstractSet[int]) -> Set[int]:
    return set(s)

def square(elements: Sequence[float]) -> List[float]:
    return [x ** 2 for x in elements]

def hello() -> NoReturn:
    print('hello')
