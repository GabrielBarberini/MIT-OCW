from datetime import datetime
from tabular import make_change
from exhaustive_enumeration import tabuall_make_change
from decision_tree import tree_make_change

print("Optimized Exhaustive Enumeration ")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", tabuall_make_change(list(range(1,50)), 250))
print("coin_val = [1, 3, 4, 5], change = 7: ", tabuall_make_change([1, 3, 4, 5], 7))
print("coin_val = [1, ..., 103], change = 1032: ", tabuall_make_change(list(range(1,103)), 1032))
print("coin_val = [1], change = 250: ", tabuall_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Tabular")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", make_change(list(range(1,50)), 250))
print("coin_val = [1, 3, 4, 5], change = 7: ", make_change([1, 3, 4, 5], 7))
print("coin_val = [1, ..., 103], change = 1032: ", make_change(list(range(1,103)), 1032))
print("coin_val = [1], change = 250: ", make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Optimized Decision Tree")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", tree_make_change(list(range(1,50)), 250))
print("coin_val = [1, 3, 4, 5], change = 7: ", tree_make_change([1, 3, 4, 5], 7))
print("coin_val = [1, ..., 103], change = 1032: ", tree_make_change(list(range(1,103)), 1032))
print("coin_val = [1], change = 250: ", tree_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")
