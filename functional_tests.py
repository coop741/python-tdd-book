from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Comments used to explain the User Story in our functional tests
        # by forcing us to make a coherent story out of the test, it makes 
        # sure we’re always testing from the point of view of the user.

        # Judith has heard about a cool new online to-do app.
        # She goes to check out its homepage. 
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # The page invites her to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # The text box still is inviting her to add another item.
        # she enters "Use peacock feathers to make a fly-fishing lure".

        # The page updates again, and now shows both items on her list.

        # Judith wonders whether the site will remember her list. She
        # sees that the site generated a unique URL for her.

        # She visits that URL, her to-do list is still there.

# Check if this Python script has been executed from command line, rather
# than imported by another script. unittest.main() launches unittest runner,
# finds test classes and methos in file to run.
if __name__ == '__main__':
    unittest.main()