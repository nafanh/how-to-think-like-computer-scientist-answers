myfile = open("test.txt","r")
line_list = myfile.readlines()
myfile.close()
line_list.reverse()

outfile = open("outfile.txt","w")
for line in line_list:
    outfile.write(line)
outfile.close()