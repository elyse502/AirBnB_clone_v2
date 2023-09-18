#!/usr/bin/python3
''' module for file_storage tests '''

import unittest
from models.engine.db_storage import DBStorage
import MySQLdb
import sys
from models.user import User
from os import getenv

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                 'db_storage test not supported')
class TestDBStorage(unittest.TestCase):
    '''testing dbstorage engine'''
    def test_new_and_save(self):
        '''testing  the new and save methods'''
        db = MySQLdb.connect(user=getenv('HBNB_MYSQL_USER'),
                             host=getenv('HBNB_MYSQL_HOST'),
                             passwd=getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=getenv('HBNB_MYSQL_DB'))
        new_user = User(**{'first_name': 'jack',
                           'last_name': 'bond',
                           'email': 'jack@bond.com',
                           'password': 12345})
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=getenv('HBNB_MYSQL_USER'),
                             host=getenv('HBNB_MYSQL_HOST'),
                             passwd=getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()
