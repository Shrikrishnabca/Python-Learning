# String is a collection of characters
# String is immutable - cannot change the original object
# String is bond with '', "", """"""
import re

from Data_type.data_type_list import words
from about_python.built_in_functions import value

print('Helo world')
print("Hello world")
print("""Hello world""")

# len() is a built in function gives the length of collection data type
print(len("haii"))  # 4 counts starts from 1

# empty string
a = ''
b = str()
print(a, b)

# Raw string prefixed with r and its not consider the \ slash character its treat as a normal string
# in python \ character has special meaning
# \t tab
# \n new line
# \\ escape sequence
print("hello \n world")
print(r"Hello \n world")

# Indexing is a process of extracting one corrector at a time
# Indexing start from Zero
# In indexing we can give positive indexing or negative
a = "shrikrishna"

# First character
print(a[0])  # s
print(a[-len(a)])  # s

# last character
print(a[-1])  # a
print(a[len(a) - 1])  # a

# slicing is process of extracting one or more character at a time
# str_obj[start index(0): end index(-1): step count(1)]
print(a[::])  # Whole string
print(a[::2])  # Even Index chatterers
print(a[1::2])  # Odd Index corrector
print(a[::3])  # dividend of 3 characters
print(a[::-1])  # reverse a string

# String formating is a process of injecting the dynamic value to the string during run time
# we will use {} and string prefixed with f""
name = "shri krishna"
name_1 = "shri krishna"
print(name_1 is name)  # if create a string instance with same value it will not create new instance, instead
# both pointing to same instance in
print(f"my name is {name}")

# String builtin methods
# Upper() convert all character to upper case
print(name.upper())  # it will not modify original string, so its immutable
name = 'SHRI KRISHNA'

# lower() convert all character to lower
print(name.lower())

# dir() is built in function give all attributes attached to the object
print(dir(name))

# swap case() converts lower to upper and vice versa
print(name.swapcase())

# capitalize returns string starts with upper case
print(name.capitalize())

# count return number of occurrence of specified string in original string (case-sensitive)
name = "shri krishna"
# count(sub_string, start index, end index)
print(name.count("s"))  # 2
print(name.count("s", 1))  # 1

# returns zero if sub string is not present in original string
print(name.count("z"))

# merging string adding two string using arithmetic operator +
# is an example of operator overloading
print("Hello " + "Krishna")

# Type conversion
# Number to string
a = 123
print(str(a))  # "123"

# Floating to string
a = 1.23
print(str(a))

# Boolean to string
a = True
print(str(a))  # "True"

# list to string
a = [1, 2, 3]
print(str(a))  # "[1,2,3]"

# tuple to string
a = (1, 2, 3)
print(str(a))  # "(1,2,3)"

# dictionary to string
print(str({'a': 1, 'b': 2}))  # "{'a': 1, 'b': 2}"

# None to string
print(str(None))  # "None"

# string to int
a = "12"
print(type(int(a)))

# string to list
a = "[1,2,3]"
print(list(a))  # it will treat each as a char ['[', '1', ',', '2', ',', '3', ']']
a = "123"
print(list(a))

# Write a program to reverse a string
a = "hello"
print(a[::-1])


def reverse_string(word: str):
    return word[::-1]


print(reverse_string("shrikrishna"))


# Check if the string is palindrome
def is_palindrome(word: str):
    return word == word[::-1]


print("given word is palindrome" if is_palindrome("mom") else "given word is not palindrome")


# Count the occurrence of charactor
def count_char(s, char):
    return s.count(char)


print("shrikrishna".count("s"))  # 2


def char_count(word, char):
    count = 0
    for ch in word:
        if ch == char:
            count += 1
    return count


print(char_count("shrikrishn", "s"))  # 2

# Find the no repeated character
word = "hello"
for ch in word:
    if word.count(ch) == 1:
        print(ch)

# remove the duplicate from a string
word = "hello"
removed_word = ""
for ch in word:
    if word.count(ch) == 1:
        removed_word += ch
print(removed_word)


def remove_duplicate(word: str):
    return "".join(set(word))


print(remove_duplicate("shrikrishna"))  # snhirka


# Count the number of words in a string
def count_word(s: str):
    return len(s.split())  # list of words


print(count_word("Hello world"))  # 2


# Check two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


print(is_anagram("listen", "silent"))  # True


# Capitalize the First Letter of Each Word (Title Case)
def title_case(s):
    return s.title()


print(title_case("hello world"))  # Hello World


# Replace a Word in a String
def replace(s, old, new):
    return s.replace(old, new)


print(replace("I love you", "love", "like"))  # I like you

# Remove Spaces from a String
print("hello world".replace(" ", ""))  # helloworld


# Check if a String Contains Only Digits
def is_number(s):
    return s.isdigit()


print(is_number("123"))  # True
print(is_number("hello23"))  # False


# Convert a String to ASCII Values
def string_to_ascii(s):
    return [ord(ch) for ch in s]


print(string_to_ascii("hello"))


# Convert ASCII value to string
def ascii_to_string(values_list):
    return "".join(chr(value) for value in values_list)


print(ascii_to_string([104, 101, 108, 108, 111]))


# Count Vowels and Consonants in a String


def count_vowel(s: str):
    v_count = 0
    c_count = 0
    vowel = "aeiouAEIOU"
    for ch in s:
        if ch in vowel:
            v_count += 1
        elif ch not in vowel and ch.isalpha():
            c_count += 1
    return v_count, c_count


print(count_vowel("hello good morning"))


def count_vowel(s: str):
    vowel = "aeiouAEIOU"
    v_count = sum(1 for ch in s if ch in vowel)
    c_count = sum(1 for ch in s if ch not in vowel and ch.isalpha())
    return v_count, c_count


print(count_vowel("hello good morning"))


# Remove Special Characters from a String

def remove_spcl_characters(s: str):
    spcl_chr = "!@#$%^&*()_+{}|:,./?';"
    result_str = ""
    for ch in s:
        if ch not in spcl_chr:
            result_str += ch
    return result_str


print(remove_spcl_characters("hello @ good morning#"))


def remove_spcl(s):
    return re.sub(r"[^A-za-z0-9]", " ", s)


print(remove_spcl("hello @ good morning"))


#  Find the Longest Word in a Sentence
def long_word(s: str):
    split_list = s.split()
    max_len_str = ""
    for ch in split_list:
        if len(ch) > len(max_len_str):
            max_len_str = ch
    return max_len_str


print(long_word("hello shrikishna gowda heggar"))

# Swap Case of Each Letter in a String
print("hello world".swapcase())


# Print Each Character of a String Separately
def print_ch(s: str):
    for ch in s:
        print(ch)


print_ch("hello good morning")

# to Upper case
a = "Hello Good morning"
result = ""
for ch in a:
    if "a" <= ch <= "z":
        result += chr(ord(ch) + 32)
    result += result
print(result)

# to lower case
a = "HELLo Godd morniG"
result = ""
for ch in a:
    if "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    else:
        result += ch
print(result)

# swap case
a = "HELLo Godd morniG"
result = ""
for ch in a:
    if "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    elif "a" <= ch <="z":
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result)

# Find the length of a string without using len()
a = "HELLo Godd morniG"
count = 0
print(len(a))
for _ in a:
    count += 1
print(count)

# Replace all spaces in a string with hyphens
a = "Hai shrikrishna good morning"
print(a.replace(" ", "-"))
result = ""
for ch in a:
    if ch == " ":
        result += "-"
    else:
        result += ch
print(result)

# Count the frequency of characters in a string
word = "banana"
result = {}
for ch in word:
    if ch not in result.keys():
        result[ch] = 1
    else:
        result[ch] += 1
print(result)

# Remove duplicate characters in a string
word = "hello"
result = ""
for ch in word:
    if word.count(ch) == 1:
        result += ch
print(result)

# Find duplicate characters in a string
word = "hello"
freq = {}
result = {}
for ch in word:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
for ch, count in freq.items():
    if count > 1:
        result[ch] = count
print(result)

# make it unique
word = "hello"
freq = {}
for ch in word:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
print("".join(freq.keys()))

# Find the first non-repeating character in a string
a = "swiss"
for ch in a:
    if a.count(ch) == 1:
        print(ch)
        break

# Capitalize the first letter of each word in a string
a = "Hello good morning"
print(a.capitalize())
words = a.split()
result = ""
for word in words:
    if not "A" <=word[0]<= "Z":
        result += chr(ord(word[0]) -32) + word[1:] + " "
    else:
        result += word + " "
print(result)

# Check if a string contains only digits
a = "123r"
print(a.isdigit())
for ch in a:
    if not "0" <= ch <= "9":
        print("string not contains only digits")
        break
else:
    print("string contains only digits")

# Count words in a sentence
sentence = "Hai how are you, how is your leag now ?"
words = sentence.split()
result = {}
for word in words:
    if word not in result.keys():
        result[word] = 1
    else:
        result[word] += 1
print(result)



