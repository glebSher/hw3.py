# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

sp = [1, 2, 5, 2, 4, 1, 2]
ran = range(0, len(sp))
sp = list(ran)
for i in range(sp):
    if list[i] != list[i + 1:len(list)]:
        print(i)