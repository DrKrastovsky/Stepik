'''На вход вашей программе поступает положительное целое число n,
а ваша задача вывести в порядке возрастания все цифры, которые встречались в этом числе,
и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в числе n '''
n = input()
count = [0] * 10
for i in n:
    count[int(i)] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])
