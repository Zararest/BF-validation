# Программа для валидации интерпретатора bf
# Описание языка взято из https://en.wikipedia.org/wiki/Brainfuck
# Зависимости: tabulate

import Boot
import Validation
import getopt
import sys


def main():
  argv = sys.argv[1:]
  verbose_arg = False
  install = False
  try:
    opts, args = getopt.getopt(argv, 'vm:i', ['verbose', 'install'])
    for opt in opts:
      if (opt == 'v' or opt == 'verbose'):
        verbose_arg = True
      if (opt == 'i' or opt == 'install'):
        verbose_arg = True  
  except getopt.GetoptError:
    print('Invalid options')
    sys.exit(2)

  if (install):
    Boot.get_package()

  results = Validation.validate(verbose=verbose_arg)
  Validation.draw_tests(results)

if __name__ == '__main__':
    main()