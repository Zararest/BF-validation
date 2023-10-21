import Tests
from tabulate import tabulate

# Формат результатов: название статус
def draw_tests(test_results):
  numbered_test_res = []
  failed_tests = []
  for num in range(len(test_results)):
    name = test_results[num][0]
    result = test_results[num][1]
    result_line = '\033[92m' + 'Passed'
    if (result == False):
      failed_tests.append(name)
      result_line = '\033[91m' + 'Failed'
    numbered_test_res.append([num, name, result_line])
  print('\n')
  print(tabulate(numbered_test_res, headers=["N", "Name", "Result"]))
  print('\n')


def validate():
  test_results = []
  name, status = Tests.test_HelloWorld(True)
  test_results.append([name, status])
  return test_results
