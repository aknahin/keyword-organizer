f = open('line.txt')
a = list()
c = 0
for line in f:
    try:
        a = line.rstrip()
        print(a,'\b, ', end = '')
    except:
        continue
input()
