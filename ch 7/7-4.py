def words_len_five(str_list):
    five_count = 0
    for word in str_list:
        if len(word) == 5:
            five_count += 1
    return five_count

print(words_len_five(["fadsf","ddf","daf","fffff"]))