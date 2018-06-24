def lcm(a, b):
  copy_of_a = a
  while (copy_of_a % b) != 0:
        copy_of_a = copy_of_a + a
  return copy_of_a

a, b = map(int, input().split())
print(lcm(a, b))
