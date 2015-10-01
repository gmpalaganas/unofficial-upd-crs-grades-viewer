import re
import string

# Removes 'tab', 'newline', and unicode characters in the given string
def to_ascii(s):
    return re.sub('[\t\n]+','',filter(lambda x: x in string.printable, s))

# Formats the grade string
def format_grade_string(grade_string):
    if grade_string == None:
        return ''
    else:
        return to_ascii(grade_string)

# Converts the units string to float
def units_string_to_float(units_string):
    if units_string == None:
        return 0.0 
    else:
        return float(re.sub('\(\d\.\d\)','0.0',to_ascii(units_string)))

# Converts the grade string into a float 
def grade_string_to_float(grade_string):
    grade_string = re.sub('\s+','',grade_string)
    if grade_string == None:
        return 0.0
    else:
        if re.match(r'(INC\()?\s*P\s*\)?',grade_string):
            return 3.0
        elif grade_string == 'INC':
            return 4.0
        elif grade_string == 'DRP':
            return 5.0
        elif re.match(r'\s+',grade_string):
            return float(to_ascii(grade_string))
        else:
            return 0.0

 # Checks if the grade garnered in the given class is passing
def is_subject_pass(subject):
    grade_float = grade_string_to_float(subject['grade'])
    return grade_float <= 3.0
