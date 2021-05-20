def foo(lst):
    seen = set()
    for el in lst:
        if el in seen:
            return el
        seen.add(el)


lst = [1, 2, 3, 4, 4, 1]

print(foo(lst))
