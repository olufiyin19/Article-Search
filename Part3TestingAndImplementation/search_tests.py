from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        my_metadata_1 = [['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138, ['the', 'dog', 'faced', 'bat', 'and']], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917, ['cadogan', 'record', 'and', 'the', 'band', 'third', 'eye', 'blind', 'with', 'from', 'their', 'album', 'his', 'jenkins', 'recording', 'elektra', 'records', 'was', 'for', 'california', 'two', 'music', 'that', 'have', 'were']]]
        my_metadata_2 = [['1922 in music', 'Gary King', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']], ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]]
        expected_keyword_to_titles_results_1 = {'the': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'dog': ['Mexican dog-faced bat'], 'faced': ['Mexican dog-faced bat'], 'bat': ['Mexican dog-faced bat'], 'and': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']}
        expected_keyword_to_titles_results_2 = {'music': ['1922 in music'], 'the': ['1922 in music', 'Ken Kennedy (computer scientist)'], '1922': ['1922 in music'], 'january': ['1922 in music'], 'first': ['1922 in music'], 'may': ['1922 in music'], 'orchestra': ['1922 in music'], 'radio': ['1922 in music'], 'october': ['1922 in music'], 'and': ['1922 in music', 'Ken Kennedy (computer scientist)'], 'for': ['1922 in music', 'Ken Kennedy (computer scientist)'], 'paul': ['1922 in music'], 'walter': ['1922 in music'], 'george': ['1922 in music'], 'billy': ['1922 in music'], 'harry': ['1922 in music'], 'you': ['1922 in music'], 'march': ['1922 in music'], 'april': ['1922 in music'], 'production': ['1922 in music'], 'opened': ['1922 in music'], 'theatre': ['1922 in music'], 'september': ['1922 in music'], 'ran': ['1922 in music'], 'performances': ['1922 in music'], 'august': ['1922 in music'], 'american': ['1922 in music'], 'singer': ['1922 in music'], 'actress': ['1922 in music'], 'composer': ['1922 in music'], 'june': ['1922 in music'], 'kennedy': ['Ken Kennedy (computer scientist)'], 'was': ['Ken Kennedy (computer scientist)'], 'computer': ['Ken Kennedy (computer scientist)'], 'award': ['Ken Kennedy (computer scientist)']}
        self.assertEqual(keyword_to_titles(my_metadata_1), expected_keyword_to_titles_results_1)
        self.assertEqual(keyword_to_titles([]), {})
        self.assertEqual(keyword_to_titles(my_metadata_2), expected_keyword_to_titles_results_2)

    def test_title_to_info(self):
        my_metadata_1 = [['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138, ['the', 'dog', 'faced', 'bat', 'and']], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917, ['cadogan', 'record', 'and', 'the', 'band', 'third', 'eye', 'blind', 'with', 'from', 'their', 'album', 'his', 'jenkins', 'recording', 'elektra', 'records', 'was', 'for', 'california', 'two', 'music', 'that', 'have', 'were']]]
        expected_title_to_info_results_1 = {'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}}
        my_metadata_2 = [['1922 in music', 'Gary King', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']], ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]]
        expected_title_to_info_results_2 = {'1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}}
        self.assertEqual(title_to_info(my_metadata_1), expected_title_to_info_results_1)
        self.assertEqual(title_to_info([]), {})
        self.assertEqual(title_to_info(my_metadata_2), expected_title_to_info_results_2)
    
    def test_search(self):
        keyword_to_titles = {'the': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'dog': ['Mexican dog-faced bat'], 'faced': ['Mexican dog-faced bat'], 'bat': ['Mexican dog-faced bat'], 'and': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']} 
        self.assertEqual(search('dog', keyword_to_titles), ['Mexican dog-faced bat'])
        self.assertEqual(search('the', keyword_to_titles), ['Mexican dog-faced bat', 'Kevin Cadogan'])
        self.assertEqual(search('THE', keyword_to_titles), [])
        self.assertEqual(search('', keyword_to_titles), [])
        self.assertEqual(search('great', keyword_to_titles), [])
        self.assertEqual(search('two', keyword_to_titles), ['Kevin Cadogan'])

    def test_article_length(self):
        article_titles_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Kevin Cadogan']
        title_to_info_1 = {'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}}
        self.assertEqual(article_length(2531, article_titles_1, title_to_info_1), ['Mexican dog-faced bat'])
        self.assertEqual(article_length(200, article_titles_1, title_to_info_1), [])
        self.assertEqual(article_length(-5000, article_titles_1, title_to_info_1), [])

    def test_key_by_author(self):
        article_titles_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Kevin Cadogan', '1922 in music', 'Ken Kennedy (computer scientist)']
        article_titles_2 = ['Black dog (ghost)', 'Sun dog', '1922 in music', 'Ken Kennedy (computer scientist)']
        title_to_info_1 = {'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, '1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}}
        expected_key_by_author_results_1 = {'Gary King': ['1922 in music'], 'Mack Johnson': ['Ken Kennedy (computer scientist)']}
        expected_key_by_author_results_2 = {'Mack Johnson': ['Mexican dog-faced bat', 'Ken Kennedy (computer scientist)'], 'Mr Jake': ['Kevin Cadogan'], 'Gary King': ['1922 in music']}
        self.assertEqual(key_by_author(article_titles_1, title_to_info_1), expected_key_by_author_results_2)
        self.assertEqual(key_by_author(['Black dog (ghost)'], title_to_info_1), {})
        self.assertEqual(key_by_author(article_titles_2, title_to_info_1), expected_key_by_author_results_1)
        self.assertEqual(key_by_author([], title_to_info_1), {})
        self.assertEqual(key_by_author(article_titles_1, {}), {})

    def test_filter_to_author(self):
        article_titles_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Kevin Cadogan', '1922 in music', 'Ken Kennedy (computer scientist)']
        title_to_info_1 = {'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, '1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}}
        self.assertEqual(filter_to_author('Mr.Jake', article_titles_1, title_to_info_1), [])
        self.assertEqual(filter_to_author('Mack Johnson', article_titles_1, title_to_info_1), ['Mexican dog-faced bat', 'Ken Kennedy (computer scientist)'])
        self.assertEqual(filter_to_author('MACK JOHNSON', article_titles_1, title_to_info_1), [])
        self.assertEqual(filter_to_author('Gary King', article_titles_1, title_to_info_1), ['1922 in music'])

    def test_filter_out(self):
        article_titles_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Kevin Cadogan', '1922 in music', 'Ken Kennedy (computer scientist)']
        keyword_to_titles_1 = {'the': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'dog': ['Mexican dog-faced bat'], 'faced': ['Mexican dog-faced bat'], 'bat': ['Mexican dog-faced bat'], 'and': ['Mexican dog-faced bat', 'Kevin Cadogan'], 'cadogan': ['Kevin Cadogan'], 'record': ['Kevin Cadogan'], 'band': ['Kevin Cadogan'], 'third': ['Kevin Cadogan'], 'eye': ['Kevin Cadogan'], 'blind': ['Kevin Cadogan'], 'with': ['Kevin Cadogan'], 'from': ['Kevin Cadogan'], 'their': ['Kevin Cadogan'], 'album': ['Kevin Cadogan'], 'his': ['Kevin Cadogan'], 'jenkins': ['Kevin Cadogan'], 'recording': ['Kevin Cadogan'], 'elektra': ['Kevin Cadogan'], 'records': ['Kevin Cadogan'], 'was': ['Kevin Cadogan'], 'for': ['Kevin Cadogan'], 'california': ['Kevin Cadogan'], 'two': ['Kevin Cadogan'], 'music': ['Kevin Cadogan'], 'that': ['Kevin Cadogan'], 'have': ['Kevin Cadogan'], 'were': ['Kevin Cadogan']}
        self.assertEqual(filter_out('were', article_titles_1, keyword_to_titles_1), ['Mexican dog-faced bat'])
        self.assertEqual(filter_out('and', article_titles_1, keyword_to_titles_1), [])
        self.assertEqual(filter_out('dog', article_titles_1, keyword_to_titles_1), ['Kevin Cadogan'])
        self.assertEqual(filter_out('see', article_titles_1, keyword_to_titles_1), ['Mexican dog-faced bat', 'Kevin Cadogan'])
        self.assertEqual(filter_out('', article_titles_1, keyword_to_titles_1), ['Mexican dog-faced bat', 'Kevin Cadogan'])
    
    def test_articles_from_year(self):
        article_titles_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Kevin Cadogan', '1922 in music', 'Ken Kennedy (computer scientist)']
        title_to_info_1 = {'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, '1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}}
        self.assertEqual(articles_from_year(2017, article_titles_1, title_to_info_1), [])
        self.assertEqual(articles_from_year(2009, article_titles_1, title_to_info_1), ['Mexican dog-faced bat', '1922 in music', 'Ken Kennedy (computer scientist)'])
        self.assertEqual(articles_from_year(2021, article_titles_1, title_to_info_1), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_article_length(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        advanced_response = 2000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_key_by_author(self, input_mock):
        keyword = 'dog'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Pegship': ['Black dog (ghost)'], 'Mack Johnson': ['Mexican dog-faced bat'], 'Mr Jake': ['Dalmatian (dog)', 'Sun dog'], 'Jack Johnson': ['Guide dog']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_filter_to_author(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        advanced_response = 'Mack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_filter_out(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        advanced_response = 'see'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_articles_from_year(self, input_mock):
        keyword = 'music'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['1922 in music', '2009 in music', 'Rock music', '1936 in music', '1962 in country music', 'Steve Perry (musician)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_none(self, input_mock):
        keyword = 'soccer'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
