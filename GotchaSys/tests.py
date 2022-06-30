from django.test import TestCase
from GotchaSys.views import MainPage
from GotchaSys.models import Feedback

class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mainpage.html')
        
    def test_responding_POST_request(self):
        resp = self.client.post('/', data={'user_name':'Test Name', 'user_email':'email@example.com', 'user_number': '09123123123', 'user_query': 'Test paragraph here.'})

        # self.assertIn('postName', resp.content.decode())
        # self.assertIn('postNumber', resp.content.decode())
        # self.assertIn('postParagraph', resp.content.decode())

        self.assertEqual(Feedback.objects.count(), 1)
        newItem = Feedback.objects.first()
        self.assertEqual(newItem.name, 'Test Name')
        self.assertEqual(newItem.email, 'email@example.com')
        self.assertEqual(newItem.number, 9123123123)
        self.assertEqual(newItem.query, 'Test paragraph here.')

        # self.assertTemplateUsed(resp, 'mainpage.html')

    def test_POST_redirect(self):
    	response = self.client.post('/', data={'user_name':'Test Name', 'user_email':'email@example.com', 'user_number': '09123123123', 'user_query': 'Test paragraph here.'})
    	self.assertEqual(response.status_code, 302)
    	self.assertEqual(response['location'], '/')

    def test_only_saves_items_if_necessary(self):
    	self.client.get('/')
    	self.assertEqual(Feedback.objects.count(), 0)

class ORMTest(TestCase):
    def test_saving_retrieving_list(self):
        txtItem1 = Feedback()
        txtItem1.name = 'Test Name1'
        txtItem1.email = 'email@example.com'
        txtItem1.number = '321321'
        txtItem1.query = 'Testing this.'
        txtItem1.save()
        txtItem2 = Feedback()
        txtItem2.name = 'Test Name2'
        txtItem2.email = 'emails@example.com'
        txtItem2.number = '123123'
        txtItem2.query = 'Testing here.'
        txtItem2.save()
        savedItems = Feedback.objects.all()
        self.assertEqual(savedItems.count(), 2)
        savedItem1 = savedItems[0]
        savedItem2 = savedItems[1]
        self.assertEqual(savedItem1.name, 'Test Name1')
        self.assertEqual(savedItem1.email, 'email@example.com')
        self.assertEqual(savedItem1.number, '321321')
        self.assertEqual(savedItem1.query, 'Testing this.')
        self.assertEqual(savedItem2.name, 'Test Name2')
        self.assertEqual(savedItem2.email, 'emails@example.com')
        self.assertEqual(savedItem2.number, '123123')
        self.assertEqual(savedItem2.query, 'Testing here.')

    def test_saving_retrieving_list(self):
    	Feedback.objects.create(name='Test Name',
            email='email@example.com',
            number='123123123',
            query='Testing here.')

    	Feedback.objects.create(name='Test Name2',
            email='email2@example.com',
            number='321321321',
            query='Testing this.')

    	response = self.client.get('/')
    	self.assertIn('1: Test Name, email@example.com, 123123123, Testing here.', response.content.decode())
    	self.assertIn('2: Test Name2, email2@example.com, 321321321, Testing this.', response.content.decode())




# Create your tests here.
