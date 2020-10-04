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
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUzNjgsImV4cCI6MTYwMTkyMTc2NywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Cij7tbfqc2SGCpIj24cbjJCwybqvosE8jUTG3Y2EYA2K08qQmp1G9v8WC9FUOEn0vaEPtTJcjpNXxbzx_QD5stln7UoCL5cfvTNKJBhijWW8TMEcOgqhp0jYxGrWW6FxF123Y9e30sRRRyDFtxKABsVOTiqGeuyWK1ytG01rEFSDgI-6nDDxeQd8W9RklKEWSLogbHsVOseaLoWuq8kmSl7zqgnv9kP_nRvBK03qbnxKo4Nfc5in9MXb6mhAHvtxSaQkr6y6JsIJpFA0zxB9PeSY6Vl6LVPr_fzMRutmEV2ku0f9ngIrvbQYpJxT8Brkl_ExcwVvP-cd7INavJV_cw'
        }
    
    casting_director_auth_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyZmYxODc2OGRlOTkwMDM3NDZlYTA3IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUyNDcsImV4cCI6MTYwMTkyMTY0NiwiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.g-jXlKuLsNDKgm3iK-d_vYwkzvXgQYA4yrN_PzufnFmsHpjYs_WSZkGmzm5z7WoO0eOXGMbdb7J-DzUldq771cBWD6amvSJCrgzbJafoUjJoPcqt-wIK8CG9ds6xcXuREJGHftIX1ug1ovPHVxtzZyH2QuRluPxhbdqKe7von5d2FQLeE3dgXDIUHJ3gC9WZ0WGz8BuOFfNUTHoNYTYl6fmvQjEFkomxa6mSVhOs4C1ua32niblvIyP8W144zNjp98OJBvjJ3wVPkumwmhgraAfoSw0iKGVRxvcL1lfehBQfVKSvnaegA2vlmVdZWrTfccyojAgXdiy7ppAnvA_'
        }

    casting_assistant_auth_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3YTAwMzNkYzViMjMwMDc4YWQ3NmY1IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUxMDQsImV4cCI6MTYwMTkyMTUwMywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.U4sUKNsYLJmg4tguefy8j3cboZyKBWbqKIlh4FG1SCWBHzPO0hkml1cp9MFgP_X215_IlCybiSybur1rLU2DAS95g1JmXR6kGHZxs_Ff4AflMHDJnLSR2yMFU3IweBbRu5VVTPmmiQOo1PuUy_NU1UIZybCRbwuggmcRcjm2VdjtgPr06baGh1qH7Lv6ijiydo5QHK7v9Jy3i9QT3-9ndcUFH6SJZQzjLTyj-gaJRNKK2LhW-Ky4KPCmk8yQHMfVI4EVF6VePOZZDDE97Diw3sae5Yp58cUzgzpMFWKsOy1DK_OAalu9fRx3JCLkXTCWLcbbR8nnVUUOmrxKVQIZaA'
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

    def test_post_actor_with_no_json(self):

        res = self.client().post('/actors', headers=self.__class__.executive_producer_auth_header)

        self.assertEqual(res.status_code, 422)

    def test_post_movie(self):

        res = self.client().post('/movies', headers=self.__class__.executive_producer_auth_header, json={'title': 'The Land of Fire', 'releaseDate':'11-24-65'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['movie']['title'], 'The Land of Fire')

    def test_post_movie_with_no_json(self):

        res = self.client().post('/movies', headers=self.__class__.executive_producer_auth_header)

        self.assertEqual(res.status_code, 422)

    def test_get_actors(self):

        res = self.client().get('/actors', headers=self.__class__.casting_assistant_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])

    def test_get_actors_without_access(self):

        res = self.client().get('/actors', headers=self.__class__.no_auth_header)

        self.assertEqual(res.status_code, 401)

    def test_get_movies(self):

        res = self.client().get('/movies', headers=self.__class__.casting_assistant_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movies'])

    def test_get_movies_without_access(self):

        res = self.client().get('/movies', headers=self.__class__.no_auth_header)

        self.assertEqual(res.status_code, 401)
    
    def test_patch_actor(self):

        res = self.client().patch('/actors/1', headers=self.__class__.casting_director_auth_header, json={'name': 'Randy Law', 'age': 30, 'gender': 'Male'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['actor']['age'], 30)

    def test_patch_actor_with_incorrect_id(self):

        res = self.client().patch('/actors/10', headers=self.__class__.casting_director_auth_header, json={'name': 'Randy Smith', 'age': 30, 'gender': 'Male'})

        self.assertEqual(res.status_code, 422)

    def test_patch_movie(self):

        res = self.client().patch('/movies/2', headers=self.__class__.executive_producer_auth_header, json={'title': 'The Land of Fear'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['movie']['title'], 'The Land of Fear')
    
    def test_patch_movie_with_incorrect_id(self):

        res = self.client().patch('/movies/10', headers=self.__class__.executive_producer_auth_header, json={'title': 'The Land of Joy'})
        
        self.assertEqual(res.status_code, 422)
    
    def test_delete_actor(self):

        res = self.client().delete('/actors/3', headers=self.__class__.casting_director_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'], 3)
    
    def test_delete_actor_with_incorrect_id(self):

        res = self.client().delete('/actors/10', headers=self.__class__.casting_director_auth_header)

        self.assertEqual(res.status_code, 422)

    def test_delete_movie(self):

        res = self.client().delete('/movies/1', headers=self.__class__.executive_producer_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'], 1)
    
    def test_delete_movie_with_incorrect_id(self):

        res = self.client().delete('/movies/10', headers=self.__class__.executive_producer_auth_header)

        self.assertEqual(res.status_code, 422)

if __name__ == "__main__":
    unittest.main()