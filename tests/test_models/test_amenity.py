#!/usr/bin/python3
"""
Unit Test for Amenity Class
"""
import unittest
from datetime import datetime
import models
import json
from os import environ
from models.engine.db_storage import DBStorage

Amenity = models.amenity.Amenity
BaseModel = models.base_model.BaseModel


class TestAmenityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Amenity  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new amenity'
        actual = Amenity.__init__.__doc__
        self.assertEqual(expected, actual)


class TestAmenityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Amenity  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new amenity for testing"""
        if (environ(HBNB_TYPE_STORAGE) == "db"):
            DBStorage.__init__()
            amenityA = Amenity(name = "wifi")
            DBStorage.new(amenityA)
            DBStorage.save()
        else:
            self.amenity = Amenity()

    @unittest.skipIf(environ(HBNH_TYPE_STORAGE) == "file",
                     "Tear down only for DB engine testing")
    def tearDown(self):
        """tear down engine and session of testing for db"""
        DBStorage.__session.close()
        DBStorage.__engine.close()

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
                self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.amenity)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
            self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.amenity.save()
        actual = type(self.amenity.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE)=="db",
                             "If DBstorage is used vs File Storage engine")
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.amenity_json = self.amenity.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.amenity_json)
        except:
            actual = 0
            self.assertTrue(1 == actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE)=="db",
                             "If DBstorage is used vs File Storage engine")
    def test_json_class(self):
        """... to_json should include class key with value Amenity"""
        self.amenity_json = self.amenity.to_json()
        actual = None
        if self.amenity_json['__class__']:
            actual = self.amenity_json['__class__']
            expected = 'Amenity'
            self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.amenity.name = "greatWifi"
        if hasattr(self.amenity, 'name'):
            actual = self.amenity.name
        else:
            actual = ''
            expected = "greatWifi"
            self.assertEqual(expected, actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE)=="file",
                    "File doesn't necessitate ID check in MYSQLDB")
    def test_amenity_id(self):
        expected = self.amenityA.id
        actual = DBStorage.__session.query(Amenity).filter\
                 (Amenity.id==expected).one()
        self.assertTrue(expected==actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE)=='file',
                     "File doesn't necessiate check in DB")
    def test_name_attribute(self):
        expected = "wifi"
        amenity_name = session.query(Amenity).filter(
            Amenity.id==self.amenityA.id).one()
        amenity_name.name = "wifi"
        DBStorage.save(amenity_name)
        actual = DBStorage.__session.query(Amenity.name).filter(
            Amenity.id==self.amenityA.id).one()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
                     unittest.main
