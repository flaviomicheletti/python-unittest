#!/usr/bin/python -tt
# coding: utf-8
import unittest

# Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
#
# Dado um a lista de números, retorna uma lista onde
# todo elemento adjacente e repetido será deletado reduzindo a um único elemento.
# Então, [1, 2, 2, 3] retornará [1, 2, 3]
# Você pode criar uma nova lista ou modificar a lista atual.
def remove_adjacent(nums):
    result = []

    if len(nums) > 1:
        result.append(nums[0])

    for num in nums:
        if num != result[-1]:
            result.append(num)

    return result


# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# Dado duas listas ordenadas em ordem crescente, criar e retornar uma
# lista de todos os elementos em ordem algabética.
# Você pode modificar as listas passadas.
# Idealmente, a solução deve trabalhar em tempo "linear", que passa uma única vez em ambas as listas.
def linear_merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result


class MyTest(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        # Repare que são excluídos apenas os valores repetidos e adjacentes
        self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(
            linear_merge(["aa", "xx", "zz"], ["bb", "cc"]),
            ["aa", "bb", "cc", "xx", "zz"],
        )
        self.assertEqual(
            linear_merge(["aa", "xx"], ["bb", "cc", "zz"]),
            ["aa", "bb", "cc", "xx", "zz"],
        )
        self.assertEqual(
            linear_merge(["aa", "aa"], ["aa", "bb", "bb"]),
            ["aa", "aa", "aa", "bb", "bb"],
        )
