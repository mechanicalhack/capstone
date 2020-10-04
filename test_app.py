import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

class CastingAgencyTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    #Bearer Tokens
    executive_producer_auth_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzAwNzgsImV4cCI6MTYwMTkxNjQ3NywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.e66hFqK3tPKvsBlCilB4CquQFCZJePelN1jzYPafYMVACa4ioLSt-b9-6mQ2qrOzESqWANTx2xH1ezRwkJCV264SA3XdORgWnXukMHRfX0LmrgPdG43L_ULeMTqofe4vjEmE9Aw9DsLmZAPVAjoFPz4K6cNDKp-z-Dy33KhosoqWx4K8PtnJtlnFbL8sxQY8beXNN_ynpoTnzqQkkKEJXlMqjySYQc3WRGvCTr46ceri_DRedJ-eIDefkAdGzfKQ-ax3CwI8njtOWqiFBX0h7E3v8NUsn_GLKfE8G4HBmZDocLhCEA0EfK3ZYHSAYN_Z-skf2nmO6S_Q9wy8HymDhw'
        }
    
    casting_director_auth_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyZmYxODc2OGRlOTkwMDM3NDZlYTA3IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzA2MjUsImV4cCI6MTYwMTkxNzAyNCwiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.jX5cJR1-qqdUFs13EtzPFmG_mCbKjxZHWmim4rOCpJc1Crz-5TCKX3T97CgMnXhpdi4Vo1tVGRE2cbp24dQCa1odgSkpLrYq50SFxBUyDc1syTSxGqpmGIcEgD1sdR57zyVWDH4m1XjzaHwNPVtWNT4ZRCfXLshSGvIjBbFJzBJTNyVJrQBWk9_RlesGDCAEOppklXurMKZhkruM-cPl0mrOLP5B0t8JvDbtDlVV52jTENn74Rf4HdnwCSgyl7pw4_VRhhYEOmHXdkiCcGka4rMadbBNNH3fyWeNNCddYWDjHz1yFKH2bOD5xrc094DcC1lZmo9MNRjxeHWkDdW7wg'
        }

    casting_assistant_auth_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3YTAwMzNkYzViMjMwMDc4YWQ3NmY1IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzEwMTQsImV4cCI6MTYwMTkxNzQxMywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.Z4NRab-vPpvCKQweVUVSoXnm9Jd-XCGrEM0B6xY7ScUtKXeiTTzN1QJnjp4339fNaWUZZ3IGKEv3WWAAIbf7Fo8a5QxkOXOXFQ2UosMjy9NzZYZq96-Ab5cP0cC82FDxzmh9ebu4FTCY44EGXWWc1bwe4kMF7vIOCwn3yplboRrLGFmd3UaRYIoCi6T_e09kQXaCo29r6risqftP0R_8vJ8CDmDFwtEa0S46knlS0klTmxUh8lBmTV9lelKxLIaYiSYnCI_wCABFQtxaztGLnjuapr0zuOFBYqdF81KNl6uLCgPxJ6pY3Mcea4BXroE5sr_-ieLjJeCQjTY6BhTbYA'
        }
    
    no_auth_header = {
            'Authorization': ''
        }

    def test_post_actor(self):

        res = self.client().post('/actors', headers=self.__class__.executive_producer_auth_header, json={'name': 'Randy Law', 'age': 29, 'gender': 'Male'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['actor']['name'], 'Randy Law')

    def test_post_movie(self):

        res = self.client().post('/movies', headers=self.__class__.executive_producer_auth_header, json={'title': 'The Land of Fire', 'releaseDate':'11-24-65'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['movie']['title'], 'The Land of Fire')

    def test_get_actors(self):

        res = self.client().get('/actors', headers=self.__class__.casting_assistant_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])

    def test_get_actors_without_access(self):

        res = self.client().get('/actors', headers=self.__class__.no_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_get_movies(self):

        res = self.client().get('/movies', headers=self.__class__.casting_assistant_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movies'])
    
    def test_patch_actor(self):

        res = self.client().patch('/actors/1', headers=self.__class__.casting_director_auth_header, json={'name': 'Randy Law', 'age': 30, 'gender': 'Male'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['actor']['age'], 30)

    def test_patch_movie(self):

        res = self.client().patch('/movies/2', headers=self.__class__.executive_producer_auth_header, json={'title': 'The Land of Fear'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['movie']['title'], 'The Land of Fear')
    
    def test_delete_actor(self):

        res = self.client().delete('/actors/3', headers=self.__class__.casting_director_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'], 3)

    def test_delete_movie(self):

        res = self.client().delete('/movies/1', headers=self.__class__.executive_producer_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'], 1)

# Tests:
# One test for success behavior of each endpoint
# One test for error behavior of each endpoint
# done # At least two tests of RBAC for each role

if __name__ == "__main__":
    unittest.main()