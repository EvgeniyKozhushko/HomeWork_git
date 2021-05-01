import time
import os

w = " " #"\u2B1C"
b = "█" #"\u2588"

dict = {
    "1" :
    [w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b],

    "2" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+w+w,
    b+b+w+w+w+w,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    "3" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    "4" : 
    [b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b],

    "5" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+w+w,
    b+b+w+w+w+w,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    "6" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+w+w,
    b+b+w+w+w+w,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    "7" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b],

    "8" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    "9" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b,
    w+w+w+w+b+b],

    "0" : 
    [b+b+b+b+b+b,
    b+b+b+b+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+w+w+b+b,
    b+b+b+b+b+b,
    b+b+b+b+b+b],

    }

def seporator():
    var = 0
    while True:
        if var % 2:
            var += 1
            yield [w, w, w, w, b, b, w, w, w, w]
        else:
            var += 1
            yield [w, w, w, w, w, w, w, w, w, w]

seporator_1 = seporator()

def main():
    while True:
        os.system('cls')
        t1 = list(time.strftime('%H:%M:%S'))
        h_1 = t1[0]
        h_2 = t1[1]
        min_1 = t1[3]
        min_2 = t1[4]
        s_1 = t1[6]
        s_2 = t1[7]
        sep = next(seporator_1)
        
        for i in range(10):
            print(f'{dict.get(h_1)[i]} {dict.get(h_2)[i]} {sep[i]} {dict.get(min_1)[i]} {dict.get(min_2)[i]} {sep[i]} {dict.get(s_1)[i]} {dict.get(s_2)[i]}')
        
        time.sleep(0.5)
main()