for i in range(5):
  print(i)


def sample(name: str, age: int, *args, **kargs):
  print(name)
  print(age)
  for arg in args:
    print(arg)

  for key in kargs:
    print(f'{key} : {kargs[key]}')

age: int = 0 


print(age)

sample("sandi", 32, "hasko", susuk="usil", abik=34)


print("salah")
print("hallo buddy")


print("hay sob")


print("marge 3")

print("from master")
print("cf3 change")
