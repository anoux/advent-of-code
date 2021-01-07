#Example for Challenge 3 part I
def parse_input(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    example_input = []
    for line in lines:
        linea = line.strip ("\n")
        example_input.append(linea)
    return example_input

example = parse_input("/home/anouxis/TrySomethingElse/AdventOfCode/E03/example_input.txt")

def trees_in_slope(mapa):
    trees_number = 0
    x = 0
    y = 0
    while x < len(mapa):
        if mapa[x][y] == "#":
            trees_number += 1
        x += 1
        y += 3       
        
        if y > len(mapa[0])-1:
            y = y - len(mapa[0])
    return trees_number 
            
print (trees_in_slope(example))

#%%

#Example for Challenge 3 part II

def parse_input(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    example_input = []
    for line in lines: 
        linea = line.strip ("\n")
        example_input.append(linea)
    return example_input

def trees_in_slope(mapa, right, down):
    trees_number = 0
    x = 0
    y = 0
    while x < len(mapa):
        if mapa[x][y] == "#":
            trees_number += 1
        x += down
        y += right               
        if y > len(mapa[0])-1:
            y = y - len(mapa[0])            
    return trees_number 
            
def part1(mapa):
    slope_1 = (trees_in_slope(mapa,1,1))
    slope_2 = (trees_in_slope(mapa,3,1))
    slope_3 = (trees_in_slope(mapa,5,1))
    slope_4 = (trees_in_slope(mapa,7,1))
    slope_5 = (trees_in_slope(mapa,1,2))
    total_trees = slope_1 * slope_2 * slope_3 * slope_4 * slope_5
    return total_trees    

def main():
    example = parse_input("/home/anouxis/TrySomethingElse/AdventOfCode/E03/example_input.txt")
    i1= parse_input("/home/anouxis/TrySomethingElse/AdventOfCode/E03/input3.txt")
    #part1(i1)
    #part2(i1)

#main()

print(part1(example))
    











