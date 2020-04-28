import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = {
            'name': 'John',
            'age': 21,
            'gender': 'Male'
        }
        self.new_movie = {
            'title': 'The Thing',
            'release': 'September 22nd, 2014'
        }

        self.casting_assistant_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWU3ZDZiNjliYzBjMTJkYzhiZjciLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYyMzUsImV4cCI6MTU4ODE0MjYzNSwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.a95TT00C2lqpbSyOSXCJpercfEHQov4-mSGcjkRjSIUNLDurjmIA2C8TEHWIVaLuk8fl5Q-DB4rjnogSsQUyAGxdLyTNAv6XDgyTk9KUWz0fWmey3iX9Pkghky_9cbk7-O-wCXJEWrNQEJ0xGJ0PuMDKSXbhIUZ-hnBX_ujfDohr2S-pJQqnEIvzOVriIEy_zyKjip3IRjyYyR7REUwNtQaEV7ZYoY0MCy52xqZzwGJM911MKoXq_aYegQldUSZ-oeO0zg1vjCv-BcAuHJXvFH-APzf5GfdJhtnifAotXcEIW5jwbND3IsaXB05DlpUmKRNe-q6MinsrXcKgg-dHdA'}

        self.casting_director_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWVhNzZiNjliYzBjMTJkYzhjNTgiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYyODIsImV4cCI6MTU4ODE0MjY4MiwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.F8QhFldNHU3xUVcleOb77EywK1alxsEDemT6OpfGO9otVVglogWYL3fqy8yJwyHNo-n44gzTmFErmLGgyGeRWp7KDEFDvmojD78RLOcYCZqcIfgVh9D3VtV1kvkV2c56jLbneCMI1lM523UhtlgugYsSSAuNa0QqoRj5PFZhp2YPBAitceVvVJ_j3fYBOifG1hSDF8yINt-UvuP09WcrfyYRVN2SYW7jpygg6-qd8sPl36hsdgvxAOJcD-_ZyuPN4MoNoki5mgcVQey2dShDazK9PU_c-T4bFoTCg5yxNIl0H0UIaa7FoWTLRdk4CKDV6sAv9n-GlKq8Hp94rOpqiA'}

        self.executive_producer_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWY5MzZiNjliYzBjMTJkYzhlOTQiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYzMzEsImV4cCI6MTU4ODE0MjczMSwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.k2Pu57G_8AaqFdudnePttx3FAqr16jTWV1pwgk_4sxVFuMmP7argCwqFHCkP6PdzGZgIrgUrm975_OhtXQIMWS5LvX8SOxSajfME0zlX8Rauec7p2VZ4mtvAX7vEIvfGJermu_wAA_CEsYYvRJXTVFDAjXkFddPz-Fmqj_5VBFo9kJaxwKsO7B1Q8nszv8M0FLQO7Aw5LV9SvFrjETfc7gCV_AkkAIM0V8u9XNsbKmnenowv231K0buOdi-G77d0WxGy8TSPnNu_o-F2Mo1DVjDV6MjZAKnRvZ3GMTHLAKslphmNM9i64onZAwPq-A7D4hzIdtHrinBDlw4A18Lerg'}

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_create_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_all_actors(self):
        res = self.client().get('/actors', headers=self.executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_get_all_movies(self):
        res = self.client().get('/movies', headers=self.executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_update_actor(self):
        res = self.client().patch('/actors/1', json={'name': 'Sally'},
                                  headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie(self):
        res = self.client().patch('/movies/1', json={'title': 'Thing'},
                                  headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_bad_request(self):
        res = self.client().post(
            '/actors', json={'title': 'Thing'}, headers=self.executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    def test_404_actor_id_not_found(self):
        res = self.client().patch('/actors/100',
                                  json={'name': 'Sally'}, headers=self.executive_producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_autherror(self):
        res = self.client().delete('/movies/1', headers=self.casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message']['code'], 'unauthorized')


if __name__ == "__main__":
    unittest.main()
