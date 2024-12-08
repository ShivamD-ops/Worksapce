import re
# ^ (carrot) represents start of the pattern
# $ end of string
# . any charachter other than newline
# * zero or more occerences
# MetaCharachters -> [].$*+?{}()\|
# + one or more occerence
# ? Zero or 1 occerence
# {n} Exactly n occerences
# {n,m} between n and m occerences
# a{2,3} abc aabc pattern match
# a | b ade pattern matched
print('''
pattern = '^a...s$'
test_strings = ['abyss','abyss','abs','Alias']


for test_string in test_strings:
    result = re.match(pattern,test_string)

    if result:
        print('Search Successful')
    else:
        print('Search Unsuccessful')

''')
pattern = '^a...s$'
test_strings = ['abyss','abyss','abs','Alias']


for test_string in test_strings:
    result = re.match(pattern,test_string)

    if result:
        print('Search Successful')
    else:
        print('Search Unsuccessful')

print('''
string = 'hello 12 hi 89 Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)

print(result)

''')

string = 'hello 12 hi 89 Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)

print(result)


print('''
string1 = 'Twellwe:12 Eighty nine:89'

result1 = re.split(pattern,string)

print(result1)

''')

string1 = 'Twellwe:12 Eighty nine:89'
pattern1 = '\d+'
result1 = re.split(pattern1,string1)

print(result1)


print('''
string_match = "python is fun"
match = re.search('\APython', string)

if match:
    print(f"Pattern Found")
else:
    print("Pattern not Found")

''')

string_match = "Python is fun"
match = re.search('\APython', string_match)

if match:
    print(f"Pattern Found")
else:
    print("Pattern not Found")

string3 = '39801 256, 2102 1111'
pattern3 = '(\d{3}) (\d{2})'
match = re.search(pattern,string)

if match:
    print(match.group())
else:
    print("Pattern not found")

# Email Validation->
email = "abc@gmail.com"

valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$',email)
# r'abc' is raw string that is string in this must be considered as raw string without any intepretaton of special charachters

print("Valid emain address. " if valid else "Invalid emain address. ")
