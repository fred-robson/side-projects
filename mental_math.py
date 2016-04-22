level = 1
while True:
    top_bound = (10**level)-1
    from random import randint
    int1 = randint(0,top_bound)
    int2 = randint(0,top_bound)
    op = randint(0,2)
    answer = 0
    op_str = ''
    if(op == 0):
        op_str = '+'
        answer = int1 + int2 
    if(op == 1):
        op_str = '-'
        answer = int1 - int2
    if(op == 2): 
        op_str = '*'
        answer = int1 * int2
    print(str(int1) + op_str  + str(int2))
    response = raw_input("=")
    if str(response) == 'q':
        exit()
    if(str(response) == 'c'):
       level_str = raw_input("Choose a level between 1 and 3: ") 
       level = int(level_str)
    else:
        if response == str(answer):
            print("Correct!")
        else:
            print("Wrong")
            print("The answer was " + str(answer))
 
