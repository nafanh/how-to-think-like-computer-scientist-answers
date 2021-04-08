def count_letters(str,letter):
    count = 0
    for i in range(len(str)):
        if str.find(letter,i,i+1) != -1:
            count +=1
    return count

print(count_letters('banana','a'))
print(count_letters('banana','x'))
print(count_letters('banana','n'))