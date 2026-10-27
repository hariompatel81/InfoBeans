def outer():
  x = 5
  def inner():
    print(x)
  return inner

fun1 = outer()
print(fun1.__closure__)
print(fun1.__closure__[0].cell_contents)