SOME_NUMBERS = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

def transformation(num, x):
    if 0<=num<4:
        return SOME_NUMBERS[1*x]*(num)
    elif 5<=num<9:
        return SOME_NUMBERS[5*x]+(SOME_NUMBERS[1*x]*(num - 5))
    elif num == 4:
        return SOME_NUMBERS[1*x]+SOME_NUMBERS[5*x]
    elif num == 9:
        return SOME_NUMBERS[1*x]+SOME_NUMBERS[10*x]

def roman_number(limit_num):
    int_num = 1
    counter = 1
    while True:
        if counter <= limit_num:
            if len(str(int_num)) == 1:
                unit = transformation(int_num, 1)
        else:break

def run():
    limit_num = 1000
    roman_number(limit_num)

if __name__=='__main__':
    run()