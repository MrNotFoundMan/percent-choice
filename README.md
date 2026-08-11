#Здравствуйте это мой модуль для различных шансов я создавал его для игр но возможно вы найдете применения в других направлениях
#Ниже вы найдете python code с тестами и объяснением чтобы поверхностно понять как работает мой модуль
#Hello, this is my module for handling various probabilities; I created it for games, but you might find uses for it in other areas as well.
#Below, you will find Python code with tests and explanations to give you a basic understanding of how the module works.


#``` bash: pip install percent_choice


import percent_choice
#для того чтобы работать с моим модулем нужно передать список с названиями класами и так далее
#затем надо передать список с процентами, 0 индекс в первом списке равен 0 индексу во втором списке

#To work with my module, you need to pass a list containing class, names and so on.
#Then you need to pass the list of percentages; the element at index 0 in the first list corresponds to the element at index 0 in the second list.
choice = percent_choice.Percent(["Common","Uncommon","Rare","Epic","Mythical","Legendary"],[40,30,20,8.99,1,0.01])
#например шанс у Common равен 40% так как индекс 0 в первом списке равен индексу 0 во втором
#For example, the chance for "Common" is 40%, since index 0 in the first list corresponds to index 0 in the second.



#тест на время милион итераций всего за 0.42462172900013684 Timing test: a million iterations in just 0.42462172900013684.
"""import time
start = time.perf_counter()
for _ in range(1_000_000):
    choice.get()
end = time.perf_counter()
print(end - start)"""





#тест на работу процентов  Percentage calculation test
"""from collections import Counter
results = Counter(choice.get() for _ in range(1_000_000))
print(results)
for name, count in results.items():
    print(name,count / 1_000_000 * 100,"%")"""
#за милион раз прокручиваний получились такие ответы  After running through the process a million times, these are the answers I got.
#Counter({'Common': 399745, 'Uncommon': 300666, 'Rare': 199788, 'Epic': 89733, 'Mythical': 9972, 'Legendary': 96})
# такой ответ + - он совпадает  This answer matches + - .
"""Common 39.960699999999996 %
Epic 9.006599999999999 %
Uncommon 29.976999999999997 %
Rare 20.0342 %
Mythical 1.0109 %
Legendary 0.0106 %"""




#функция get работает предслучайно (модуль random) это значит что если вы хороши в криптографии вы можете предсказать наносекунду 
#когда выпадет легендарка если вам это не подходит вы можете использовать супер предслучайный выбор secrets
#он выберает рандом исходя из ваших действий на пк и так далее, предсказать это невозможно
#минусы время. Оно работает медленее чем random и также в secrets float работает криво из за этого я убрал использование secret числа с запятой

# The get function operates using pseudorandomness (the random module); this means that if you are skilled in cryptography, you could predict the exact nanosecond
# a legendary item will drop. If that doesn't suit your needs, you can use the highly unpredictable selection provided by the secrets module.
# It generates randomness based on your PC activity and similar factors, making it impossible to predict.
# The downside is speed: it is slower than random, and the secrets module also handles floats poorly —which is why I didn't use it for the `secret` version..

choice = percent_choice.SecurePercent(["Common","Uncommon","Rare","Epic","Mythical","Legendary"],[40,30,20,6,3,1])
#я получил 2.0263745570009633 разница между random полтора секунда грубо говоря
#I got 2.0263745570009633—the difference between the random values, roughly speaking, was one and a half seconds.
"""import time
start = time.perf_counter()
for _ in range(1_000_000):
    choice.get()
end = time.perf_counter()
print(end - start)"""

#я получил такие данные
#I received this data.
"""Counter({'Common': 399408, 'Uncommon': 299725, 'Rare': 200627, 'Epic': 59987, 'Mythical': 30236, 'Legendary': 10017})
Uncommon 29.972500000000004 %
Common 39.940799999999996 %
Rare 20.0627 %
Epic 5.9986999999999995 %
Legendary 1.0017 %
Mythical 3.0236 %"""

"""from collections import Counter
results = Counter(choice.get() for _ in range(1_000_000))
print(results)
for name, count in results.items():
    print(name,count / 1_000_000 * 100,"%")"""
