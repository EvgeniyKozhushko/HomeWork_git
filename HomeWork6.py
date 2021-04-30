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

        sep = w

        if int(s_2) % 2 == 0:
            sep = b
            print(w)
        else:
            print(sep)

        print(f'{dict.get(h_1)[0]} {dict.get(h_2)[0]}   {dict.get(min_1)[0]} {dict.get(min_2)[0]}   {dict.get(s_1)[0]} {dict.get(s_2)[0]}')
        print(f'{dict.get(h_1)[1]} {dict.get(h_2)[1]}   {dict.get(min_1)[1]} {dict.get(min_2)[1]}   {dict.get(s_1)[1]} {dict.get(s_2)[1]}')
        print(f'{dict.get(h_1)[2]} {dict.get(h_2)[2]}   {dict.get(min_1)[2]} {dict.get(min_2)[2]}   {dict.get(s_1)[2]} {dict.get(s_2)[2]}')
        print(f'{dict.get(h_1)[3]} {dict.get(h_2)[3]}   {dict.get(min_1)[3]} {dict.get(min_2)[3]}   {dict.get(s_1)[3]} {dict.get(s_2)[3]}')
        print(f'{dict.get(h_1)[4]} {dict.get(h_2)[4]} {sep} {dict.get(min_1)[4]} {dict.get(min_2)[4]} {sep} {dict.get(s_1)[4]} {dict.get(s_2)[4]}')
        print(f'{dict.get(h_1)[5]} {dict.get(h_2)[5]} {sep} {dict.get(min_1)[5]} {dict.get(min_2)[5]} {sep} {dict.get(s_1)[5]} {dict.get(s_2)[5]}')
        print(f'{dict.get(h_1)[6]} {dict.get(h_2)[6]}   {dict.get(min_1)[6]} {dict.get(min_2)[6]}   {dict.get(s_1)[6]} {dict.get(s_2)[6]}')
        print(f'{dict.get(h_1)[7]} {dict.get(h_2)[7]}   {dict.get(min_1)[7]} {dict.get(min_2)[7]}   {dict.get(s_1)[7]} {dict.get(s_2)[7]}')
        print(f'{dict.get(h_1)[8]} {dict.get(h_2)[8]}   {dict.get(min_1)[8]} {dict.get(min_2)[8]}   {dict.get(s_1)[8]} {dict.get(s_2)[8]}')
        print(f'{dict.get(h_1)[9]} {dict.get(h_2)[9]}   {dict.get(min_1)[9]} {dict.get(min_2)[9]}   {dict.get(s_1)[9]} {dict.get(s_2)[9]}') 

        time.sleep(1)
        
main()     