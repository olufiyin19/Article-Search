from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        expected_search_results = ['USC Trojans volleyball', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(search('ball'), expected_search_results)
        self.assertEqual(search('BALL'), expected_search_results)
        self.assertEqual(search('Ball'), expected_search_results)
        self.assertEqual(search(''), [])
        self.assertEqual(search('.'), [])

    def test_title_length(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)']
        expected_title_length_results = []
        self.assertEqual(title_length(10, titles), expected_title_length_results)
        self.assertEqual(title_length(0, titles), expected_title_length_results)
        self.assertEqual(title_length(14, titles), ['Edogawa, Tokyo', 'Kevin Cadogan'])
        self.assertEqual(title_length(14, []), [])
        self.assertEqual(title_length(-1, titles), [])


    def test_article_count(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)']
        self.assertEqual(article_count(3, titles), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid'])
        self.assertEqual(article_count(5, titles), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season'])
        self.assertEqual(article_count(100, titles), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)'])
        self.assertEqual(article_count(0, []), [])
        self.assertEqual(article_count(-1, []), [])

    def test_random_article(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)']
        self.assertEqual(random_article(0, titles), 'Edogawa, Tokyo')
        self.assertEqual(random_article(6, titles), 'Dalmatian (dog)')
        self.assertEqual(random_article(100, titles), '')
        self.assertEqual(random_article(1, []), '')
    
    def test_favorite_article(self):
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)']
        self.assertEqual(favorite_article('kevin cadogan', titles), True)
        self.assertEqual(favorite_article('KEVIN CADOGAN', titles), True)
        self.assertEqual(favorite_article('Kevin Cadogan', titles), True)
        self.assertEqual(favorite_article('2007', titles), False)
        self.assertEqual(favorite_article('', titles), False)
        self.assertEqual(favorite_article('Big Dogs', titles), False)

    def test_multiple_keywords(self):
        dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        ball_search_results = ['USC Trojans volleyball', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'Georgia Bulldogs football under Robert Winston']
                                
        boy_search_results = []
        expected_dog_and_ball_multiple_keywords_results = ['USC Trojans volleyball', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'Georgia Bulldogs football under Robert Winston', 'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        expected_ball_and_dog_multiple_keywords_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(multiple_keywords('', dog_search_results), dog_search_results)
        self.assertEqual(multiple_keywords('', ball_search_results), ball_search_results)
        self.assertEqual(multiple_keywords('', boy_search_results), boy_search_results)

        self.assertEqual(multiple_keywords('DOG', ball_search_results.copy()), expected_dog_and_ball_multiple_keywords_results)
        self.assertEqual(multiple_keywords('ball', dog_search_results.copy()), expected_ball_and_dog_multiple_keywords_results)

        self.assertEqual(multiple_keywords('boy', dog_search_results.copy()), dog_search_results)
        self.assertEqual(multiple_keywords('boy', ball_search_results.copy()), ball_search_results)

        self.assertEqual(multiple_keywords('BAll', boy_search_results.copy()), ball_search_results)
        self.assertEqual(multiple_keywords('Dog', boy_search_results.copy()), dog_search_results)

        self.assertEqual(multiple_keywords('Dog', dog_search_results.copy()), dog_search_results + dog_search_results)
        self.assertEqual(multiple_keywords('BalL', ball_search_results.copy()), ball_search_results + ball_search_results)

#python3 search_tests.py

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_1(self, input_mock):
        keyword = 'dog'
        advanced_option = 1

        output = get_print(input_mock, [keyword, advanced_option, 15])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +'\n' + print_advanced_option(advanced_option) + str(15) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_2(self, input_mock):
        keyword = 'dog'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option, 10])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +'\n' + print_advanced_option(advanced_option) + str(10) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_3(self, input_mock):
        keyword = 'dog'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option, 9])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +'\n' + print_advanced_option(advanced_option) + str(9) + "\n\nHere are your articles: Georgia Bulldogs football\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_4(self, input_mock):
        keyword = 'dog'
        advanced_option = 4

        output = get_print(input_mock, [keyword, advanced_option, 9])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +'\n' + print_advanced_option(advanced_option) + str(9) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\nYour favorite article is not in the returned articles!\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_5(self, input_mock):
        keyword = 'dog'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option, 'cat'])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) +'\n' + print_advanced_option(advanced_option) + str('cat') + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Voice classification in non-classical music']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_advanced_search_6(self, input_mock):
        keyword = 'cat'
        advanced_option = 6
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Voice classification in non-classical music']\n"
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
