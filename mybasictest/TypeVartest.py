#coding:utf-8

from typing import TypeVar

height = 1.77
Height = TypeVar('Height', int, float, None)

def get_height(th: Height) -> Height:
    return th

print(get_height(1.9))

#height = 2
print(get_height(2))

#height = None
print(get_height(None))


print(get_height('why'))