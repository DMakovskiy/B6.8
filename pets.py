from cats import Cat

cat1 = Cat('Барон', 'мальчик', 2)
cat2 = Cat('Сэм', 'мальчик', 2)

print('Имя первого кота:', cat1.getName())
print('Пол первого кота:', cat1.getGender())
print('Возраст первого кота:', cat1.getAge())
print('Имя второго кота:', cat2.getName())
print('Пол второго кота:', cat2.getGender())
print('Возраст второго кота:', cat2.getAge())