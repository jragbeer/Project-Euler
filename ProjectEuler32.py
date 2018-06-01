import numpy as np

ii = np.arange(10001).tolist()
r = []
for i in ii:
    for p in ii:
        if i*p < 10001:
            a = len(str(int(i))+str(int(p))+str(int(i*p)))
            if a == 9:
                count = 0
                c = str(int(i))+str(int(p))+str(int(i*p))
                for each in c:
                    if each=='1':
                        count = count + 1
                    elif each == '2':
                        count = count + 2
                    elif each == '3':
                        count = count + 3
                    elif each == '4':
                        count = count + 4
                    elif each == '5':
                        count = count + 5
                    elif each == '6':
                        count = count + 6
                    elif each == '7':
                        count = count + 7
                    elif each == '8':
                        count = count + 8
                    elif each == '9':
                        count = count + 9
                if count ==45:
                    if len(set(c))== 9:
                        r.append(i*p)
print(sum(set(r)))