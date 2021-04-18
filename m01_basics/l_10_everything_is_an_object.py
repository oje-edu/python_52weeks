# Traditional Languages - primitives
# Python: Everything Is An Object - HIGHER-LEVEL objects
print("\n\n----- Regular variables, e.g. INTEGERS and STRINGS, which are IMMUTABLE (unveränderbar) ----------")
i = 1
print(f"i = {i} {type(i)} id(i): {id(i)}")
#i = i + 1
i += 1
print(f"i = {i}, id(i): {id(i)}  <--- after i = i + 1")
j = i
print(f"\ni = {i}, id(i): {id(i)}")
print(f"j = {j}, id(j): {id(j)}  <--- after j = i")
#i = i + 1
i += 1
print(f"\ni = {i}, id(i): {id(i)}")
print(f"j = {j}, id(j): {id(j)}  <--- after i = i + 1")

print("\n\n")

print("----- LISTs variables, wich are MUTABLE (veränderbar) ----------")
l1 = [1]
print(f"l1 = {l1} {type(l1)} id(l1): {id(l1)}  <--- original l1")
l1.append(2)
print(f"l1 = {l1}, id(l1): {id(l1)}  <--- after l1.append(2)")
l2 = l1
print(f"\nl1 = {l1}, id(l1): {id(l1)}")
print(f"l2 = {l2}, id(l2): {id(l2)}  <--- l2 = l1")
l1.append(3)
print(f"\nl1 = {l1}, id(l1): {id(l1)}")
print(f"l2 = {l2}, id(l2): {id(l2)}  <--- l1.append(3)")

print("\n\n")
print("----- Function call, where immutable vs mutable is especially important ----------")

def f(r_var, l_var):
    r_var += 1
    l_var.append(5)
    print(f"inside function: regular_var={r_var}, list_var={l_var}")

regular_var = 1
list_var = [1, 2, 3]
print(f"before:          regular_var={regular_var}, list_var={list_var}")

f(regular_var, list_var)
print(f"after:           regular_var={regular_var}, list_var={list_var}")

print("\n\n")
print("----- REMEMBER -----")
print("IMMUTABLE (unveränderbar): INTEGERS, STRINGS, TUPLES")
print("MUTABLE (veränderbar): LISTS, DICTS, SETS")