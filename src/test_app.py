import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Actors, Movies

class CastingAgencyTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test.client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    #can do a teardown if necessary

    
# Tests:
# One test for success behavior of each endpoint
# One test for error behavior of each endpoint
# At least two tests of RBAC for each role
