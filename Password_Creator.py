import random

def Password_Creator(n):
    char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','9','8','0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=','+', '"','?','/']
    password = []
    random.shuffle(char)
    for i in range(n):
        a = random.randint(0, n)
        password.append(char[a])
    passwordString = ''.join(password)
    print(passwordString)

Password_Creator(26)
