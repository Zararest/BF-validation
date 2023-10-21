from Boot import get_output

# Каждый тест возвращает результат и название

def print_red(str):
  red_text = '\033[91m'
  end_escape = '\033[0m'
  print(red_text + str + end_escape)

def wrong_output(test_name, out):
  print_red(test_name + ': wrong output {' + out + '}')

def non_zero_status(test_name):
  print_red(test_name +': process returned nonzero exit staus')

def print_descr(test_name):
  print('\nDescription of the test', test_name)


def test_byte_operations(verbose=False):
  test_name = 'Byte-operations'

  if (verbose):
    print('\nDescription of the test', test_name)
    print('\tmodule: cell operations')

  success, out = get_output('./BF-code/Byte-operations.bf', as_bytes=True)

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False

  if (out != bytes([1, 0, 2, 255])):
    if (verbose):
      wrong_output(test_name, str(out))
    return test_name, False
  
  return test_name, True

def test_data_pointer_shift_neg(verbose=False):
  test_name = 'Data-pointer-shift-negative'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: negative test on shifting pointer to -1')

  success, out = get_output('./BF-code/Data-pointer-shift-negative.bf', as_bytes=True)

  if (success):
    if (verbose):
      print_red(test_name, ':', 'returned 0, but an error should have occurred')
    return test_name, False
  
  return test_name, True

def test_data_pointer_shift(verbose=False):
  test_name = 'Data-pointer-shift'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: data pointer shifting error check')

  success, out = get_output('./BF-code/Data-pointer-shift.bf')

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False

  return test_name, True

def test_fibonachi(verbose=False):
  test_name = 'Fibonachi'

  if (verbose):
    print_descr(test_name)
    print('\tend-to-end: fibonachi sequence implementation')

  success, out = get_output('./BF-code/Fibonachi.bf', '9')

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != '1 2 3 5 8 = E R g '):
    if (verbose):
      wrong_output(test_name, out)
    return test_name, False

  return test_name, True

def test_hello_world(verbose=False):
  test_name = 'Hello-world'

  if (verbose):
    print_descr(test_name)
    print('\tend-to-end: hello world implementation')

  success, out = get_output('./BF-code/Hello-world.bf')

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != 'Hello World!'):
    if (verbose):
      wrong_output(test_name, out)
    return test_name, False

  return test_name, True

def test_input_output(verbose=False):
  test_name = 'Input-output'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: echo program')

  success, out = get_output('./BF-code/Input-output.bf', 'A')

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != 'A'):
    if (verbose):
      wrong_output(test_name, out)
    return test_name, False

  return test_name, True

def test_loop(verbose=False):
  test_name = 'Loop'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: prints all the symbols less than 10')

  success, out = get_output('./BF-code/Loop.bf', as_bytes=True)

  right_values = [10]
  for c in reversed(range(10)):
    right_values.append(c)
  right_values.pop()

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != bytes(right_values)):
    if (verbose):
      wrong_output(test_name, str(out))
    return test_name, False

  return test_name, True

def test_output(verbose=False):
  test_name = 'Output'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: print cell value')

  success, out = get_output('./BF-code/Output.bf', as_bytes=True)

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != bytes([0])):
    if (verbose):
      wrong_output(test_name, str(out))
    return test_name, False

  return test_name, True

def test_zero_init(verbose=False):
  test_name = 'Zero-init'

  if (verbose):
    print_descr(test_name)
    print('\tmodule: print multiple celles value')

  success, out = get_output('./BF-code/Zero-init.bf', as_bytes=True)

  if (not success):
    if (verbose):
      non_zero_status(test_name)
    return test_name, False
  
  if (out != bytes([0, 0, 0, 0, 0])):
    if (verbose):
      wrong_output(test_name, str(out))
    return test_name, False

  return test_name, True