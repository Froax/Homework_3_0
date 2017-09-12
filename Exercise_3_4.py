#3_4

list = ['maandag', 'dinsdag', 'woensdag']

for i in list:
    print(i[:2])

#3_5

num_list = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for e in num_list:
    if e%2==0:
        print(e)


#3_6

s = "Guido van Rossum heeft programmeertaal Python bedacht."

for l in s:
    if l in 'aeuio':
        print(l)