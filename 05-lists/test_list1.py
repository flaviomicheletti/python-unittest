#!/usr/bin/python -tt
# coding: utf-8
import unittest

# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
#
# Dado um lista de strings `words`, retornar o total de strings
# se cada palavra for maior ou igual a dois e
# se o primeiro caracter coincidir com o último
def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count + 1
    return count


# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
#
# Dado uma lista de strings, retornar uma lista de string ordenadas,
# exceto todo grupo de strings que comece com "x" virá primeiro.
#
# Dica: isto pode ser feito com 2 listas ordenando cada uma delas e
# depois combinado-as. Veja os testes para maiores detalhes.
def front_x(words):
    lista_x = []
    lista_normal = []

    for word in words:
        if word[0] == "x":
            lista_x.append(word)
        else:
            lista_normal.append(word)

    lista_x.sort()
    lista_normal.sort()

    return lista_x + lista_normal


def last(a):
    return a[-1]


# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
#
# Dado uma lista de tuplas não vazias, retornar uma lista ordenada
# pelo último elemento de cada tupla.
#
# Dica: use um função personalizada `last()` para extrair
# o último elemento, ela deve ser passada no segundo parâmetro
# da função sorted()
def sort_last(tuples):
    return sorted(tuples, key=last)


class MyTest(unittest.TestCase):
    def test_match_ends(self):
        self.assertEqual(match_ends(["aba", "xyz", "aa", "x", "bbb"]), 3)
        self.assertEqual(match_ends(["", "x", "xy", "xyx", "xx"]), 2)
        self.assertEqual(match_ends(["aaa", "be", "abc", "hello"]), 1)

    def test_front_x(self):
        self.assertEqual(
            front_x(["bbb", "ccc", "axx", "xzz", "xaa"]),
            ["xaa", "xzz", "axx", "bbb", "ccc"],
        )
        self.assertEqual(
            front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]),
            ["xaa", "xcc", "aaa", "bbb", "ccc"],
        )
        self.assertEqual(
            front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]),
            ["xanadu", "xyz", "aardvark", "apple", "mix"],
        )

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(
            sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
            [(2, 2), (1, 3), (3, 4, 5), (1, 7)],
        )
