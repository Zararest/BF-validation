import Tests
from tabulate import tabulate

# Формат результатов: название статус
def draw_tests(test_results):
  green_text = '\033[92m'
  red_text = '\033[91m'
  bold_text = '\033[1m'
  end_escape = '\033[0m'

  numbered_test_res = []
  failed_tests = []
  for num in range(len(test_results)):
    name = test_results[num][0]
    result = test_results[num][1]
    result_line = bold_text + green_text + 'Passed' + end_escape + end_escape
    if (result == False):
      failed_tests.append(name)
      result_line = bold_text + red_text + 'Failed' + end_escape + end_escape
    numbered_test_res.append([num, name, result_line])
  print('\n')
  print(tabulate(numbered_test_res, headers=["N", "Name", "Result"]))
  print('\n')


def validate(verbose=False):
  test_results = []
  
  name, status = Tests.test_byte_operations(verbose)
  test_results.append([name, status])

  name, status = Tests.test_data_pointer_shift(verbose)
  test_results.append([name, status])

  name, status = Tests.test_data_pointer_shift_neg(verbose)
  test_results.append([name, status])

  name, status = Tests.test_output(verbose)
  test_results.append([name, status])

  name, status = Tests.test_zero_init(verbose)
  test_results.append([name, status])

  name, status = Tests.test_input_output(verbose)
  test_results.append([name, status])

  name, status = Tests.test_loop(verbose)
  test_results.append([name, status])

  name, status = Tests.test_fibonachi(verbose)
  test_results.append([name, status])

  name, status = Tests.test_hello_world(verbose)
  test_results.append([name, status])

  return test_results
