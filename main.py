# Программа для валидации интерпретатора bf
# Описание языка взято из https://en.wikipedia.org/wiki/Brainfuck
# Зависимости: tabulate

import Validation

def main():
  results = Validation.validate()
  Validation.draw_tests(results)

if __name__ == '__main__':
    main()