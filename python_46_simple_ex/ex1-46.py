###########ex1
#!/usr/bin/env python

"""
Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


if __name__ == "__main__":
    print max(2, 5)
    print max(5, 2)
    print max(5, 5)

###########ex2
#!/usr/bin/env python

"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""

from ex1 import max


def max_of_three(a, b, c):
    max_temp = max(a, b)
    return max(max_temp, c)


if __name__ == "__main__":
    print max_of_three(1, 2, 3)

###########ex3
#!/usr/bin/env python

"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def length(string):
    count = 0
    for i in string:
        count += 1
    return count


if __name__ == "__main__":
    print length("test string")

###########ex4
#!/usr/bin/env python

"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print is_vowel(1)
    print is_vowel('a')
    print is_vowel('b')

###########ex5
#!/usr/bin/env python

"""
Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""

from ex4 import is_vowel


def translate(string):
    results = []
    for word in string.split():
        result = ''
        for char in word:
            if not is_vowel(char):
                result += char + 'o' + char
            else:
                result += char
        results.append(result)
    return ' '.join(results)


if __name__ == "__main__":
    print translate("this is fun")

###########ex6
#!/usr/bin/env python

"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of
numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


if __name__ == "__main__":
    print sum([1, 2, 3, 4])
    print multiply([1, 2, 3, 4])

###########ex7
#!/usr/bin/env python

"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""


def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)


print reverse("I am testing")

###########ex8
#!/usr/bin/env python

"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""


def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    print is_palindrome("aabbaa")
    print is_palindrome("abc")
    print is_palindrome("radar")

###########ex9
#!/usr/bin/env python

"""
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True
if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the
exercise you should pretend Python did not have this operator.)
"""


def is_member(x, a):
    if len(a) == 0:
        return False
    return x == a[0] or is_member(x, a[1:])


if __name__ == "__main__":
    print is_member(1, [1, 2])
    print is_member('a', ['a'])
    print is_member('b', [1, 2, 'a'])

###########ex10
#!/usr/bin/env python

"""
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False
otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should
(also) write it using two nested for-loops.
"""


def overlapping(li1, li2):
    for elem1 in li1:
        for elem2 in li2:
            if elem1 == elem2:
                return True
    return False


if __name__ == "__main__":
    print overlapping([1, 2], [3, 4])
    print overlapping([1, 2], [2, 3])
    print overlapping(['a', 'b', 'c'], ['c', 'd'])

###########ex11
#!/usr/bin/env python

"""
Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long,
consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx".
(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
For the sake of the exercise you should ignore that the problem can be solved in this manner.)
"""


def generate_n_chars(n, c):
    result = ''
    for i in range(n):
        result += c
    return result


if __name__ == "__main__":
    print generate_n_chars(3, 'c')

###########ex12
#!/usr/bin/env python

"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

from ex11 import generate_n_chars


def histogram(li):
    for n in li:
        print generate_n_chars(n, '*')


if __name__ == "__main__":
    histogram([4, 9, 7])

###########ex13
#!/usr/bin/env python

"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how
many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
"""


def max_in_list(li):
    max = li[0]
    for n in li:
        if n > max:
            max = n
    return max


if __name__ == "__main__":
    print max_in_list([1, 2, 5, 3])

###########ex14
#!/usr/bin/env python

"""
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
"""


def map_list_to_len(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


if __name__ == "__main__":
    words = ['test', 'abc', 'biggest one']
    print map_list_to_len(words)

###########ex15
#!/usr/bin/env python

"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""

from ex14 import map_list_to_len


def find_longest_word(words):
    return max(map_list_to_len(words))


if __name__ == "__main__":
    print find_longest_word(['a', 'abc', 'longest'])

###########ex16
#!/usr/bin/env python

"""
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are
longer than n.
"""


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]


if __name__ == "__main__":
    print filter_long_words(['a', 'avg', 'abcde', 'zxcw', 'b'], 3)

###########ex17
#!/usr/bin/env python

"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna
hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation
"Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
"""

import string
from ex8 import is_palindrome


def is_palindrome_extended(candidate):
    candidate = ''.join([word for word in candidate.lower().split()])
    candidate = ''.join([char for char in candidate if char not in string.punctuation])
    return is_palindrome(candidate)


if __name__ == "__main__":
    print is_palindrome_extended("Rise to vote sir")

###########ex18
#!/usr/bin/env python

"""
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""

import string


def is_pangram(candidate):
    letters = set(string.ascii_lowercase)
    candidate = set(candidate.replace(" ", "").lower())
    return letters == candidate or False


if __name__ == "__main":
    print is_pangram("The quick brown fox jumps over the lazy dog")

###########ex19
#!/usr/bin/env python

"""
"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it
has a very repetitive format which is easy to memorize, and can take a long time to sing.
The song's simple lyrics are as follows:

    99 bottles of beer on the wall, 99 bottles of beer.
    Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle.
The song is completed when the singer or singers reach zero.
Your task here is write a Python program capable of generating all the verses of the song.
"""


def sing_99_bottles():
    for i in range(99, 0, -1):
        print "%d bottles of beer on the wall, %d bottles of beer.\n" \
              "Take one down, pass it around, %d bottles of beer on the wall." % (i, i, i - 1)


if __name__ == "__main__":
    sing_99_bottles()

###########ex20
#!/usr/bin/env python

"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""


def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return [lexicon[word] for word in words]


if __name__ == "__main__":
    print translate(['merry', 'christmas'])

###########ex21
#!/usr/bin/env python

"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def char_freq(string):
    freq = {key: 0 for key in string}
    for i in string:
        freq[i] += 1
    return freq


if __name__ == "__main__":
    print char_freq("abbabcbdbabdbdbabababcbcbab")

###########ex22
#!/usr/bin/env python

"""
In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is
replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be
replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with
his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13.
In Python, the key for ROT-13 may be represented by means of the following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

Your task in this exercise is to implement an encoder/decoder of ROT-13.
Once you're done, you will be able to read the following secret message:

   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written in
English.
"""


def rot13_decode(secret):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    words = [words for words in secret.split()]
    results = []
    for word in words:
        results.append("".join([key[char] if char in key.keys() else char for char in word]))
    return " ".join(results)


if __name__ == "__main__":
    print rot13_decode("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")

###########ex23
#!/usr/bin/env python

"""
Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or more
occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period
is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return
"This is very funny and cool. Indeed!" Tip: Use regular expressions!
"""

import re


def correct(string):
    string = re.sub(r'[.]([a-zA-Z])', r'. \1', string)
    string = re.sub(r'( )+', r'\1', string)
    return string


if __name__ == "__main__":
    print correct("This   is  very funny  and    cool.Indeed!")

###########ex24
#!/usr/bin/env python

"""
The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the
infinitive form: run -> runs. A simple set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s

Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its
third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must
be regarded as heuristic, in the sense that you must not expect them to work for all cases.
Tip: Check out the string method endswith().
"""

import re


def make_3sg_form(verb):
    es = ('o', 'ch', 's', 'sh', 'x', 'z')
    if verb.endswith('y'):
        return re.sub('y$', 'ies', verb)
    elif verb.endswith(es):
        return verb + 'es'
    else:
        return verb + 's'


if __name__ == "__main__":
    print make_3sg_form('try')
    print make_3sg_form('brush')
    print make_3sg_form('run')
    print make_3sg_form('fix')

###########ex25
#!/usr/bin/env python

"""
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:

    a. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    b. If the verb ends in ie, change ie to y and add ing
    c. For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    d. By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its
present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such
simple rules to work for all cases.
"""

from ex4 import is_vowel


def make_ing_form(verb):
    if verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif verb.endswith('e') and (verb[-2].endswith('e') or len(verb) == 2):
        return verb + 'ing'
    elif verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif not is_vowel(verb[-1]) and is_vowel(verb[-2]) and not is_vowel(verb[-3]):
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'


if __name__ == "__main__":
    print make_ing_form('be')
    print make_ing_form('lie')
    print make_ing_form('see')
    print make_ing_form('move')
    print make_ing_form('hug')

###########ex26
#!/usr/bin/env python

"""
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the
largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function
directly?
"""

from ex1 import max


def max_in_list(numbers):
    return reduce(max, numbers)


if __name__ == "__main__":
    print max_in_list([1, 3, 5, 10, 1, 25])

###########ex27
#!/usr/bin/env python

"""
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.
"""


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]


if __name__ == "__main__":
    words = ['abv', 'try me', 'test']
    print map_to_lengths_for(words)
    print map_to_lengths_map(words)
    print map_to_lengths_lists(words)

###########ex28
#!/usr/bin/env python

"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
Use only higher order functions.
"""


def find_longest_word(words):
    return max(map(len, words))


if __name__ == "__main__":
    print find_longest_word(['small', 'biggest', 'a huge one here'])

###########ex29
#!/usr/bin/env python

"""
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""


def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)


print filter_long_words(['test', 'not', 'this should'], 5)

###########ex30
#!/usr/bin/env python

"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} and use it to translate your
Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that
takes a list of English words and returns a list of Swedish words.
"""


def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return map(lambda word: lexicon[word], words)


if __name__ == "__main__":
    print translate(["merry", "christmas"])

###########ex31
#!/usr/bin/env python

"""
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
"""


def map(function, iterable):
    results = []
    for i in iterable:
        results.append(function(i))
    return results


def filter(function, iterable):
    return [i for i in iterable if function(i) == True]


def reduce(function, iterable):
    #TODO: http://docs.python.org/2/library/functions.html#reduce
    pass


if __name__ == "__main__":
    pass

###########ex32
#!/usr/bin/env python

"""
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line
to the screen if it is a palindrome.
"""

from ex17 import is_palindrome_extended


def palidrome_file(filepath):
    file = open(filepath)
    for line in file.read().split("\n"):
        if is_palindrome_extended(line):
            print line


if __name__ == "__main__":
    palidrome_file('io_files/ex32.txt')

###########ex33
#!/usr/bin/env python

"""
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed
desserts". Note, by the way, that each pair by itself forms a palindrome!
"""


def is_semordnilap(filepath):
    file = open(filepath)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results


if __name__ == "__main__":
    print is_semordnilap('io_files/ex33.txt')

###########ex34
#!/usr/bin/env python

"""
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency
listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to
the screen.
"""

import re


def char_freq_table(filepath):
    file = open(filepath)
    chars = file.read().lower().replace(" ", "").replace("\n", "")
    freqs = {key: 0 for key in chars}
    for char in chars:
        freqs[char] += 1
    for word in freqs:
        print "%s: %s" % (word, freqs[word])


if __name__ == "__main__":
    char_freq_table('io_files/ex34.txt')

###########ex35
#!/usr/bin/env python

"""
The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet
acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced
and understood by those who transmit and receive voice messages by radio or telephone regardless of their native
language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one
version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken
ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS
(Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken.
(Under UNIX/Linux and Windows, something similar might exist.)

Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the
length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word
spoken.
"""

#TODO###########ex36
#!/usr/bin/env python

"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
language, the works of an author, or in a single text. Define a function that given the file name of a text will return
all its hapaxes. Make sure your program ignores capitalization.
"""

import re


def hapax(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print word


hapax('io_files/ex36.txt')

###########ex37
#!/usr/bin/env python

"""
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).
"""


def numbered_file(filepath):
    file_in = open(filepath)
    file_out = open('io_files/ex37_out.txt', 'w')
    for line, content in enumerate(file_in):
        file_out.write('%s %s' % (line + 1, content))


if __name__ == "__main__":
    numbered_file('io_files/ex37.txt')

###########ex38
#!/usr/bin/env python

"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths
of the word tokens in the text, divided by the number of word tokens).
"""

import re


def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)


if __name__ == "__main__":
    print avg_word_length('io_files/ex38.txt')

###########ex39
#!/usr/bin/env python

"""
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1
and 20. (Source: http://inventwithpython.com)

This is how it should work when run in a terminal:

import guess_number
Hello! What is your name?
Torbjorn
Well, Torbjorn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjorn! You guessed my number in 3 guesses!
"""

import random

name = raw_input("Hello! What is your name?\n")
print "Well, %s, I am thinking of a number between 1 and 20." % name

secret = random.randint(1, 20)
input = int(raw_input("Take a guess.\n"))
count = 1

while input != secret:
    if input < secret:
        print "Your guess is too low."
    elif input > secret:
        print "Your guess is too high."
    input = int(raw_input("Take a guess.\n"))
    count += 1

print "Good job, %s! You guessed my number in %d guesses!" % (name, count)

###########ex40
#!/usr/bin/env python

"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or
phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place.
Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w
(thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the
user is invited to guess the original word. It may be a good idea to work with (say) colour words only.
The interaction with the program may look like so:

import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
"""

import random
import itertools

words = ['red', 'black', 'brown', 'green']
word, anagram = random.sample(words, 1)[0], ''

perms = itertools.permutations(word)
for perm in perms:
    if ''.join(perm) != word:
        anagram = ''.join(perm)
        break

print "Colour word anagram: %s" % anagram
input = raw_input("Guess the colour word!\n")

while input != word:
    input = raw_input("Guess the colour word!\n")

print "Correct!"

###########ex41
#!/usr/bin/env python

"""
In a game of Lingo, there is a hidden word, five characters long.
The object of the game is to find this word by guessing, and in return receive two kinds of clues:
1) the characters that are fully correct, with respect to identity as well as to position, and
2) the characters that are indeed present in the word, but which are placed in the wrong position.
Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and
ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the
word "tiger", you should be able to interact with it in the following way:

import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
"""

target = 'tiger'
input = raw_input('')

while input != target:
    output = ''
    for pos, char in enumerate(input):
        if char in target:
            if target[pos] == input[pos]:
                output += '[' + char + ']'
            else:
                output += '(' + char + ')'
        else:
            output += char

    print "Clue: " + output
    input = raw_input('')

print "Found!"

###########ex42
###########ex43
###########ex44
###########ex45
###########ex46
###########ex47
###########ex48
###########ex49
