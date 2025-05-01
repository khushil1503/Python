#Q.1 Count how many vowels are there in a string. Accept the string from the user.

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for c in s if c in vowels)
print(f"Vowel count: {count}")

#Q.2 Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.

def to_lower(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

def to_upper(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

def toggle_case(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        elif 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

s = input("Enter a string: ")
print("Lower case:", to_lower(s))
print("Upper case:", to_upper(s))
print("Toggle case:", toggle_case(s))

#Q.3 Accept two strings. Check whether one string is there in another string

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 in s2 or s2 in s1:
    print("One string is present in the other.")
else:
    print("No string is present in the other.")
    
#Q.4 Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”


def remove_substring(onestring, removestring):
    result = ""
    i = 0
    while i < len(onestring):
        if onestring[i:i+len(removestring)] == removestring:
            i += len(removestring)
        else:
            result += onestring[i]
            i += 1
    return result

onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")
print("Final string:", remove_substring(onestring, removestring))


