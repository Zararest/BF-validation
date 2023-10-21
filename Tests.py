from Boot import get_output

# Каждый тест возвращает результат и название

def test_byte_operations():
  test_name = 'bute-operations'
  

def test_HelloWorld(verbose = False):
  test_name = 'Hello-world'

  if (verbose):
    print('Description of test', test_name)
    print('\tend-to-end: hello world implementation')

  success, out = get_output('./BF-code/Hello-world.bf', '')

  if (not success):
    if (verbose):
      print(test_name, ':', 'process returned nonzero exit staus')
    return test_name, False
  
  if (out != 'Hello World!'):
    if (verbose):
      print(test_name, ':', 'wrong output {', out, '}')
    return test_name, False
  return test_name, True
