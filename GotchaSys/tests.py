from django.test import TestCase
from GotchaSys.views import MainPage
from GotchaSys.models import Item

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
		
	def test_responding_POST_request(self):
		resp = self.client.post('/', data={'for1Form': 'postName', 'for2Form': 'postNumber', 'for3Form': 'postParagraph'})
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text1, 'test')

		# self.assertIn('postName', resp.content.decode())
		# self.assertIn('postNumber', resp.content.decode())
		# self.assertIn('postParagraph', resp.content.decode())

		self.assertTemplateUsed(resp, 'mainpage.html')

	def test_only_Saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text1 = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text1 = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text1, 'Item one')
		self.assertEqual(savedItem2.text1, 'Item two')

# Create your tests here.
