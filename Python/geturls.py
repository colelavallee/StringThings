with open('C:/Users/Cole/Documents/StringThings/Python/Test.txt','r') as file:
    lines = file.readlines()

for line in lines[2:]:
    columns = line.split()
    print(columns[0] + columns[6])