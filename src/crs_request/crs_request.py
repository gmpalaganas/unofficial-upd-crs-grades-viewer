import utils
import requests
import re
import string
import json
from bs4 import BeautifulSoup

# URLs
LOGIN_URL = 'https://crs.upd.edu.ph/auth'
GRADES_URL = 'https://crs.upd.edu.ph/viewgrades'

# Request Header
#     For the uninitiated, this basically is additional 'info' being sent
#     to the server. It contains info like the User-Agent which tells
#     the server what 'app' is being used to send the request, in our case
#     we are telling the server that we are sending the request from a 
#     Mozilla Browser
REQ_HEADER = {
            'User-Agent': 'Mozilla/5.0',
        }

# Login form names
LOGIN_USERNAME_FORM = 'txt_login'
LOGIN_PASSWORD_FORM = 'pwd_password'

# This is how we find the tables containing the grades
GRADE_TABLE_CLASS_NAME = 'tbl_grade-info'

class CRSHandler:
    
    # A different request header can be used by adding it to the constructor
    def __init__(self,request_header=None):
        self.session = requests.session()

        self.grades_soup = None

        if request_header != None:
            self.request_header = REQ_HEADER
        else:
            self.request_header = request_header
    
    # Login into crs using the given username and password
    # Returns the status code of the request i.e. 200 (OK), 302 (Authentication)
    def login(self,username,password):
        form_data = {
                    LOGIN_USERNAME_FORM : username,
                    LOGIN_PASSWORD_FORM : password,
                }

        login_request = self.session.post(LOGIN_URL, data=form_data, 
                headers=self.request_header, allow_redirects=False)

        return login_request.status_code

    # Request the 'View Grades' page of CRS then saves it to a soup (See BeautifulSoup)
    # Returns the status code of the request
    def request_grades(self):
        grades_request = self.session.get(GRADES_URL)
        self.grades_soup = BeautifulSoup(grades_request.text, 'html.parser')

        return grades_request.status_code
    
    # Converts the requested 'View Grades' page into a list of tuples defined as
    # ( SEMESTER, GRADES_DICTIONARY_LIST)
    def get_grades(self):
        # If 'View Grades' hasn't been requested yet, send a request for it
        if self.grades_soup == None:
            # If request fails, exit function
            if request_grades() != 200:
                raise RequestFailedException

        grades = []
        tables = self.grades_soup.find_all('table')
        
        # Generate a list of the grades tables
        grade_tables = [ grade for grade in tables
        if grade.get('class') != None and GRADE_TABLE_CLASS_NAME in grade.get('class') ]
        
        # The last two table are the current sem and the RGEP taken and we don't need that
        for grade_table in grade_tables[0: len(grade_tables) - 2]:
            subjects = []
            head = grade_table.thead.find_all('tr')
            sem = head[0].th.string
            col_names = [ th.string for th in head[1].find_all('th') ] 
            rows = grade_table.tbody.find_all('tr')

            for row in rows:
                try:
                    cols = [ utils.format_grade_string(col.string) for col in row.find_all('td') ]
                    subject = {
                            'tag'        : cols[0],
                            'code'       : cols[1],
                            'name'       : cols[2],
                            'instructor' : cols[3],
                            'units'      : cols[4],
                            'grade'      : cols[5],
                            'completion' : cols[6],
                            'remarks'    : cols[7],
                            }
                    subjects.append(subject)
                except IndexError:
                    pass

            sem_grade =  ( sem, subjects )
            grades.append(sem_grade)

        return grades

    # Given the list of grades, count the total number of units passed 
    def count_total_units_passed(self,grades):
        unit_count = 0

        for grade in grades:
            sem, subjects = grade
            for subject in subjects:
                if utils.is_subject_pass(subject):
                    unit_count += utils.units_string_to_float(subject['units']) 

        return unit_count

    # Given a grades list, convert it to JSON fomrat (compact)
    def grades_to_json(self,grades,pretty=False):
        grades_dict = dict(grades)
        grades_json = ''

        if pretty:
            grades_json = json.dumps(grades_dict, indent=4, separators=(',', ': '))
        else:
            grades_json = json.dumps(grades_dict, separators=(',',':'))

        return grades_json
   
# An exception meant when the requests fails
class RequestFailedException(Exception):
    # Constructor takes the response code
    def __init__(self, reponse_code):
        self.response_code = response_code

    def __str__(self):
        return 'Response code : ' + repr(self.response_code)

