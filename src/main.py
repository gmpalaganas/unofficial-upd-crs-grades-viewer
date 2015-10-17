import getpass
import sys
from crs_request.crs_request import CRSHandler

handler = CRSHandler()

username = raw_input('Enter username: ')
password = getpass.getpass('Enter Password: ')


print 'Logging in...'
login_status_code = handler.login(username,password)

if login_status_code == 302:
    print 'Login successful'
else:
    print 'Failed to login, exiting'
    sys.exit()

print 'Requesting grades...'
grades_status_code = handler.request_grades()

if grades_status_code == 200:
    print 'Request successful'
else:
    print 'Request failed, exiting'
    sys.exit()

grades = handler.get_grades()
unit_count = handler.count_total_units_passed(grades)

for grade in grades:
    sem = grade[0]
    subjects = grade[1]
    print '\n'
    print '-', sem 
    print '******'
    for subject in subjects:
        print subject['name']
        print 'Units: '
        print subject['units']
        print 'Instructor: '
        print subject['instructor']
        print 'Grade: '
        if subject['grade'] == '':
            print 'None given yet'
        else:
            print subject['grade']
        print '******'

print 'Total Units Passed: ', unit_count
