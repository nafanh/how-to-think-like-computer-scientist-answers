import string

text = '''It is a long established fact that a reader will be distracted by the readable content of a page when 
looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, 
as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing 
packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will 
uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, 
sometimes on purpose (injected humour and the like). 
'''
def filter_text(text):
    filtered_text = ''
    for ch in text:
        if ch not in string.punctuation:
            filtered_text += ch
    word_list = filtered_text.split()
    count = 0
    for word in word_list:
        if word.find('e') != -1:
            count += 1

    print('Your text contains {0} words, of which {1} ({2:.1f}%) contain an "e".'.format(
        len(word_list), count, 100*(count/len(word_list))
    ))

filter_text(text)