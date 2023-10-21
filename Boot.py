import subprocess as subproc
import os

# Загрузка ubuntu модуля
def get_package():
  subproc.run(['sudo', 'apt', 'install', 'bf'], check=True)

# Вызов bf интерпретатора
#   - возвращает: успешное/неуспешное завершение, stdout
def get_output(test_file, test_input='', as_bytes=False):
  cwd = os.path.dirname(os.path.realpath(__file__))
  try:
    test_output = subproc.run(['bf', test_file], 
                                cwd=cwd,
                                timeout=5,
                                capture_output=True, 
                                input=test_input, 
                                check=True,
                                text=(not as_bytes))
    test_output.check_returncode()
  except subproc.CalledProcessError:
    return False, ''
  return True, test_output.stdout
