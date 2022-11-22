#!/usr/bin/python -tt
# coding: utf-8
import unittest

def remove_adjacent(nums):
  result = []

  for num in nums:
    if len(result) == 0 or num != result[-1]:
      result.append(num)

  return result


def linear_merge(list1, list2):
  result = []

  while len(list1) and len(list2):
    # testa a string, ex:
    # se "aa" < "bb"
    if list1[0] < list2[0]:
      # armazenar "aa"
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))

  result.extend(list1)
  result.extend(list2)
  return result

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


class MyTest(unittest.TestCase):
  def test_remove_adjacent(self):
    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    # Repare que são excluídos apenas os valores repetidos e adjacentes
    self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
    self.assertEqual(remove_adjacent([]), [])

  def test_linear_merge(self):
    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])

if __name__ == '__main__':
  unittest.main()