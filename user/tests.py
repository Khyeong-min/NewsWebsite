from django.test import TestCase, Client
import json

client = Client()


# unittest
class UnitTest(TestCase):
    # start
    def setUp(self):
        print("setUp")
        self.test_user_data1 = {
            'email': 'sksksk@naver.com',
            'password': 'sksksk',
            'nickname': 'sksksk',
            'user_id': 'sksksk'
        }
        self.test_login_data1 = {
            'email': 'sksksk@naver.com',
            'password': 'sksksk',
            'user_id': 'sksksk'
        }
        self.test_user_data2 = {
            'email': 'sksk',
            'password': 'alsdk',
            'nickname': 'alsdk',
            'user_id': 'alsdk'
        }

        self.test_login_data2 = {
            'email': 'sksksk@naver.com',
            'password': 'sksksk',
            'user_id': 'sksksk'
        }

    # finish : delete testcase data
    def tearDown(self):
        print("tearDown")

    # Signup Case1 : Success(200)
    def test_SignupView1(self):
        response = client.post('/user/Signup', json.dumps(self.test_user_data1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Login Case : Success(200)
    def test_LoginView1(self):
        client.post('/user/Signup', json.dumps(self.test_user_data1), content_type='application/json')

        response = client.post('/user/Login', json.dumps(self.test_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Signup Case2 : Fail(400)
    def test_SignupView1(self):
        response = client.post('/user/Signup', json.dumps(self.test_user_data3), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Login Case : Fail(400)
    def test_LoginView1(self):
        client.post('/user/Signup', json.dumps(self.test_user_data2), content_type='application/json')

        response = client.post('/user/Login', json.dumps(self.test_login_data2), content_type='application/json')
        self.assertEqual(response.status_code, 400)