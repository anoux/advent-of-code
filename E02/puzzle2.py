
def parseInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    policies = []
    for line in lines:
        policy = line.split(" ")
        min_max = policy[0].split("-")
        letra = policy[1].strip(":")
        password = policy[2].strip("\n")       
        policies.append([min_max, letra, password])
    return policies

def count_ocurrences(letter, word):
    contador = 0
    for l in word:
        if l == letter:
            contador = contador + 1
    return contador

def p1(policies):
    valid_passwords = 0
    for policy in policies:
        n = count_ocurrences(policy[1], policy[2])
        if n >= int(policy[0][0]) and n <= int(policy[0][1]):
           valid_passwords += 1
    return valid_passwords

i1 = parseInput("/home/anouxis/TrySomethingElse/AdventOfCode/E02/input2.txt")
i2 = parseInput("/home/anouxis/TrySomethingElse/AdventOfCode/E02/example.txt")


def letter_position(policies):
    valid_passwords = 0
    for policy in policies:
        mini = int(policy[0][0]) -1
        maxi = int(policy[0][1]) -1
        letra = policy[1]
        password = policy[2]
        if (password[mini] == letra) ^ (password[maxi] == letra):
            valid_passwords += 1
    return valid_passwords



print(letter_position(i1))




















