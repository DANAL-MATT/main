from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	# def tearDown(self):
	# 	self.browser.quit()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('GotchaNovelist', self.browser.title)

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Test Form', headerText)
		
		inputName = self.browser.find_element_by_id('for1Form')
		inputName.send_keys('TestName')
		#time.sleep(1)
		
		inputNumber = self.browser.find_element_by_id('for2Form')
		inputNumber.send_keys('1')
		#time.sleep(1)
		
		inputReview = self.browser.find_element_by_id('for3Form')
		inputReview.send_keys('TestParagraph')
		#time.sleep(1)
		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')

		self.assertEqual(inputName.get_attribute('placeholder'),'Enter name.')
		self.assertEqual(inputReview.get_attribute('placeholder'),'Sample paragraphs go here.')
		
		btnConfirm.click()
		time.sleep(1)
		
		table = self.browser.find_element_by_id('testTable')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: TestName 1 TestParagraph', [row.text for row in row_data])
		#self.assertTrue(any(row.text == '1: Test Name'), "No tables yet")

if __name__=='__main__':
	unittest.main(warnings='ignore')
