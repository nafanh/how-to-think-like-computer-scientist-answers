#creates layout
layout = ""
for i in range(12):
    layout += "{" + str(i) + ":>4}"

#Creates table
for i in range(1,13):

    if i == 1:
        print("\t" + layout.format(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11, i * 12))
        print(" :--------------------------------------------------")

    print(str(i) + ":", end = '\t')
    print(layout.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))