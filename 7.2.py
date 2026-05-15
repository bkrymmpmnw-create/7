n = [3, 7, 2, 7, 8, 3, 5]
print("Список:", n)
for i in n:
    if n.count(i) > 1:
        print("Повторяющийся элемент:", i)
        break