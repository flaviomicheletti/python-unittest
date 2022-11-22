#!/usr/bin/python -tt
import sys

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""


# Opção '--count'
# Imprimir as palavras em ordem alfabética + total de ocorrências, ex:
#
# <word a> <count>
# <word b> <count>
# <word c> <count>
def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count = word_count_dict(filename)
  # pegamos as chaves de forma ordenada
  words = sorted(word_count.keys())
  # percorremos cada palavra (já ordenada)  
  for word in words:
    # ...e  imprimimos <word> <count>
    print(word, word_count[word])

# Opção '--topcount'
# Imprimir as palavras em ordem alfabética + total de ocorrências, ex:
#
# <word b> <6>
# <word c> <4>
# <word a> <3>
#
# Utilize a função sorted().
# Imprima somente os 20 primeiros resultados    
def print_top(filename):
  """Prints the top count listing for the given file."""
  word_count = word_count_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  # Ordenamos as chaves conforme as ocorrências (valor de 'count')
  # Utilizamos a função "get_count()" para auxiliar a extrair o valor de 'count'  
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 20
  for item in items[:20]:
    print(item[0], item[1])


# Função auxiliar para "print_top()"
# Obs: Ela já está definida, não precisa mexer em nada.    
def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


# Função para ler o conteúdo de determinado arquivo e contar
# a ocorrência de cada palavra encontrada.
# Armazena as palavras em caixa baixa ( string.lower() ).
# Deve retornar um dicionário como por exemplo:
#
# word_count[palavra1] = n ocorrências
# word_count[palavra2] = n ocorrências
# word_count[palavra3] = n ocorrências
# etc...
def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  # percorrer cada linha do arquivo...
  for line in input_file:
    words = line.split()
    # percorrer cada palavra da linha...
    for word in words:
      word = word.lower()
      # Special case if we're seeing this word for the first time.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1

  input_file.close() # Not strictly required, but good form.
  return word_count



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]

  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
