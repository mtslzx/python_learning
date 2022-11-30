# Task 2


csv = open('./temperatures.csv', 'w')
year = 1723
with open('./temperatures.txt', 'r') as f:
    f.readline()  # skip first line
    lines = f.readlines()
    for line in lines:
        line = line.split()
        # line = line.strip()
        csv.write(str(year) + ',')
        csv.write(','.join(line) + '\n')
        year += 1
csv.close()

        
    