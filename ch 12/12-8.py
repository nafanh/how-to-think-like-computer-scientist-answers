from unit_tester import test
import string
def cleanword(str):
    a = ""
    for ch in str:
        if ch not in string.punctuation:
            a += ch
    return a


def has_dashdash(str):
    return "--" in str

def extract_words(str):
    a = ''

    for ch in str:
        if ch in string.punctuation:
            a += " "
            continue
        a += ch.lower()

    return a.split()

def wordcount(word,wrd_list):
    count = 0
    for wrd in wrd_list:
        if wrd == word:
            count += 1
    return count

def wordset(wrd_list):
    a = []
    for wrd in wrd_list:
        if wrd not in a:
            a.append(wrd)
    return sorted(a)

def longestword(wrd_list):
    longest = 0
    for wrd in wrd_list:
        if len(wrd) > longest:
            longest = len(wrd)
    return longest


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)