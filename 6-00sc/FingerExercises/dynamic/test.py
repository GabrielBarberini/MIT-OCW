from datetime import datetime
from tabular import make_change
from tabular_all import tabuall_make_change

print("Tabular")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", make_change(list(range(1,50)), 250))
print("coin_val = [1, 3, 4, 5], change = 7: ", make_change([1, 3, 4, 5], 7))
print("coin_val = [1], change = 250: ", make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Tabular-all")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", tabuall_make_change(list(range(1,50)), 250))
print("coin_val = [1, 3, 4, 5], change = 7: ", tabuall_make_change([1, 3, 4, 5], 7))
print("coin_val = [1], change = 250: ", tabuall_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")
