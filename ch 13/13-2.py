myfile = open("snakeread.txt","r")
for line in myfile:
    if 'snake' in line:
        print(line,end='')
myfile.close()