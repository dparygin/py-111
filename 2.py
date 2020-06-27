"""
Считалочка (Josephus problem)
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого
человека. Когда считалка досчитывает
до k-го слога, человек, на котором она
остановилась, вылетает. Игра происходит
до тех пор, пока не останется последний
человек. Для данных N и К дать номер
последнего оставшегося человека.
"""

N = 90000
k = 13



def data_gen(People):
    """
    Генератор списка с данными
    :return: Data List
    """
    listmass = []
    for i in range(1,People+1):
        listmass.append(i)
    return listmass

dataset = data_gen(N)

r = 0
while len(dataset) > 1:
    r = (r + k - 1) % len(dataset)
    dataset.pop(r)

print(dataset[0])