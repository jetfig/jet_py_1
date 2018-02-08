import re
import time

#print('hello current time is: {0}'.format(time.ctime()))

#s = 'a\tb'
#sr = r'a\tb'

#print(s)
#print(sr)


def validation_example_one():
    # Purpose: Verify if the given text is made up of digits
    pattern = r"\d+"

    # successful match
    text = "1234"
    match = re.match(pattern, text)

    print('Pattern {0}'.format(pattern))

    if match:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            text, match.start(), len(match.group(0))))
    else:
        print('***No Match. Text {0}'.format(text))

    # no match
    text = "ABCD1234"
    match = re.match(pattern, text)

    if match:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            text, match.start(), len(match.group(0))))
    else:
        print('***No Match. Text {0}'.format(text))

#validation_example_one()

def validation_example_two():
    # Purpose: Verify if the given text is made up of digits
    pattern = r"\d+"

    # successful match
    text = "1234"
    match = re.search(pattern, text)

    print('Pattern {0}'.format(pattern))

    if match:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            text, match.start(), len(match.group(0))))
    else:
        print('***No Match. Text {0}'.format(text))

    # successful match
    text = "ABCD1234"
    match = re.search(pattern, text)

    if match:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            text, match.start(), len(match.group(0))))
    else:
        print('***No Match. Text {0}'.format(text))

    # no match
    text = "Hello World!"
    match = re.search(pattern, text)

    if match:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            text, match.start(), len(match.group(0))))
    else:
        print('***No Match. Text {0}'.format(text))

#validation_example_two()

def validation_example_three():
    # Purpose: Verify if the given text is made up of digits
    pattern = r"^\d+$"
    positiveTest = ["123456", "456", "321082", "0820102"]
    negativeTest = ["ABCD", "A1234", "1234AB", "  123", "321  ", "  111   ", "123 4567", "123\n456"]

    print('Pattern {0}'.format(pattern))

    for text in positiveTest:
        match = re.search(pattern, text)
        if match:
            print('***Match. Text: {0} Index: {1} Length: {2}'.format(
                text, match.start(), len(match.group(0))))
        else:
            print('***No Match. Text {0}'.format(text))
            raise ValueError('Positive Test. Expected successful match but failed {0}'.format(text))

    for text in negativeTest:
        match = re.search(pattern, text)
        if match:
            print('***Match. Text: {0} Index: {1} Length: {2}'.format(
                text, match.start(), len(match.group(0))))
            raise ValueError('Negative Test. Expected a failed match but succeeded. {0}'.format(text))
        else:
            print('***No Match. Text {0}'.format(text))

#validation_example_three()

def find_all_example():
    # Purpose: Extract 5 digit postal codes
    pattern = r"\b\d{5}\b"
    text = "NY Postal Codes are 10001, 10002, 10003, 10004"

    print('Pattern {0}'.format(pattern))
    # successful match
    match = re.findall(pattern, text)

    print(match)

#find_all_example()

def find_iter_example():
    pattern = r"\b\d{5}\b"
    text = "NY Postal Codes are 10001, 10002, 10003, 10004"

    print('Pattern {0}'.format(pattern))
    print('Text {0}'.format(text))
    # successful match
    match_iter = re.finditer(pattern, text)
    for match in match_iter:
        print('***Match. Text: {0} Index: {1} Length: {2}'.format(
            match.group(0), match.start(), len(match.group(0))))

#find_iter_example()

def group_by_name_example():
    pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<hour>\d{2})?"
    text = "Timestamp=20160502"

    print('Pattern {0}'.format(pattern))
    print('Text {0}'.format(text))
    # successful match
    match_iter = re.finditer(pattern, text)

    for match in match_iter:
        print('Match. Text: {0} Index: {1} Length: {2}'.format(
            match.group(0), match.start(), len(match.group(0))))
        print('Access group by name')
        print('  Year:  {0}'.format(match.group('year')))
        print('  Month: {0}'.format(match.group('month')))
        print('  Day:   {0}'.format(match.group('day')))
        print('  Hour:  {0}'.format(match.group('hour')))
        print('Access all named groups as a dictionary')
        print('   {0}'.format(match.groupdict()))

group_by_name_example()

def group_by_number_example():
    # Optional last two digits
    pattern = r"(\d{4})(\d{2})(\d{2})(\d{2})?"
    text = "Timestamp=20160502"

    print('Pattern {0}'.format(pattern))
    print('Text {0}'.format(text))
    # successful match
    match_iter = re.finditer(pattern, text)

    for match in match_iter:
        print('Match. Text: {0} Index: {1} Length: {2}'.format(
            match.group(0), match.start(), len(match.group(0))))

        for i, value in enumerate(match.groups()):
            print('  Group: {0}, Value: {1}'.format(i + 1, value))

#group_by_number_example()

def substitution_example():
    pattern = r"(?P<value>\d+(,\d{3})*(\.\d{2})?)\s+dollar(s)?"

    replacement_pattern = r'**USD \g<value>**'

    text = \
        '''Widget Unit cost: 12,000.56 dollars
        Taxes: 234.00 dollars
        Total: 12,234.56 dollars'''

    print('Pattern: {0}'.format(pattern))
    print('---Text:\n{0}'.format(text))
    # successful match
    new_text = re.sub(pattern, replacement_pattern, text)

    print('---New Text:\n{0}'.format(new_text))

#substitution_example()
