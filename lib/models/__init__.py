import sqlite3
from .course import Course
from .enrollment import Enrollment
from .students import Student

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
