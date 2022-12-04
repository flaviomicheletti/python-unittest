#!/usr/bin/python -tt
# coding: utf-8
import unittest

# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
#
# Dado um `count` como sendo o números de donuts, retornar uma string
# na forma "Número de donuts: <count>", caso `count` seja
# maior ou igual a 10 retornar "many".
def donuts(count):
    if count < 10:
        count = str(count)
    else:
        count = "many"

    return "Number of donuts: %s" % count


# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
#
# Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero).
def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


# Given a string s, return a string where
# all occurences of its first char
# have been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields(produce) 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
#
# Dado uma string `s`, retornar uma string onde
# todas as ocorrências de seu primeiro caractere
# seja alterado para '*', exceto o primeiro caracter. Exemplo:
#
# babble ---> ba**le
#
# Presuma que o tamanho da string seja 1 ou mais.
# Dica: s.replace (strA, strB) retorna uma versão da string s
def fix_start(s):
    front = s[0]
    back = s[1:]
    fixed_back = back.replace(front, "*")
    return front + fixed_back


# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#
# Dado duas string `a` e `b`, trocar os 2 primeiros caracteres entre as variáveis
# e retornar uma única string separada por espaço como no exemplo:
#
# "pezzy", "firm" ----> "fizzy perm"
def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + " " + b_swapped


class MyTest(unittest.TestCase):
    def test_donuts(self):
        self.assertEqual(donuts(4), "Number of donuts: 4")
        self.assertEqual(donuts(9), "Number of donuts: 9")
        self.assertEqual(donuts(10), "Number of donuts: many")
        self.assertEqual(donuts(99), "Number of donuts: many")

    def test_both_ends(self):
        self.assertEqual(both_ends("spring"), "spng")
        self.assertEqual(both_ends("Hello"), "Helo")
        self.assertEqual(both_ends("a"), "")
        self.assertEqual(both_ends("xyz"), "xyyz")
        self.assertEqual(both_ends("xy"), "xyxy")

    def test_fix_start(self):
        self.assertEqual(both_ends("xy"), "xyxy")
        self.assertEqual(fix_start("babble"), "ba**le")
        self.assertEqual(fix_start("aardvark"), "a*rdv*rk")
        self.assertEqual(fix_start("google"), "goo*le")
        self.assertEqual(fix_start("donut"), "donut")

    def test_mix_up(self):
        self.assertEqual(mix_up("mix", "pod"), "pox mid")
        self.assertEqual(mix_up("dog", "dinner"), "dig donner")
        self.assertEqual(mix_up("gnash", "sport"), "spash gnort")
        self.assertEqual(mix_up("pezzy", "firm"), "fizzy perm")
