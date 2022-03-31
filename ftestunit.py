from selenium import webdriver
import unittest

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_browser_title(self):
		self.browser.get('http://127.0.0.1:8000')
		self.assertIn('Contact Tracing List', self.browser.title)
		self.fail('Finish the test!')
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')
