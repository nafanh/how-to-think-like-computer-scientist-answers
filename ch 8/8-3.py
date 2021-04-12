def count_letters(str,letter):
    count = 0
    for char in str:
        if char == letter:
            count += 1
    return count

print(count_letters('banana','a'))
print(count_letters('banana','x'))
print(count_letters('banana','n'))