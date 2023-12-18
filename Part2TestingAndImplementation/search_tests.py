from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)
    
    def test_search_unit_test(self):
        expected_search_canada_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        self.assertEqual(search('canada'), expected_search_canada_results)
        self.assertEqual(search('CANADA'), expected_search_canada_results)
        self.assertEqual(search('CaNaDa'), expected_search_canada_results)
        self.assertEqual(search(''), [])
        self.assertEqual(search('.'), [])
    
    def test_article_length_unit_test(self):
        metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        expected_article_length_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        self.assertEqual(article_length(100000, metadata), expected_article_length_results)
        self.assertEqual(article_length(7000, metadata), [['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]])
        self.assertEqual(article_length(5000, metadata), [['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]])
        self.assertEqual(article_length(0, metadata), [])
        self.assertEqual(article_length(-1, metadata), [])

    def test_unique_authors_unit_test(self):
        metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        expected_unique_authors_music_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]]
        self.assertEqual(unique_authors(9, metadata), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]])
        self.assertEqual(unique_authors(0, metadata), [])
        self.assertEqual(unique_authors(1, metadata), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023]])
        self.assertEqual(unique_authors(100, metadata), expected_unique_authors_music_results)
        self.assertEqual(unique_authors(-50, metadata), [])

    def test_most_recent_article_unit_test(self):
        canada_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        music_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842]]
        games_metadata = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]]
        playboy_metadata = []
        self.assertEqual(most_recent_article(canada_metadata), ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562])
        self.assertEqual(most_recent_article(music_metadata), ['Rock music', 'Mack Johnson', 1258069053, 119498])
        self.assertEqual(most_recent_article(games_metadata), ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413])
        self.assertEqual(most_recent_article(''), '')
        self.assertEqual(most_recent_article(playboy_metadata), '')

    def test_favorite_author_unit_test(self):
        canada_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        music_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842]]
        games_metadata = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]]
        self.assertEqual(favorite_author('Burna Boy', canada_metadata), True)
        self.assertEqual(favorite_author('Nihonjoe', music_metadata), True)
        self.assertEqual(favorite_author('Bearcat', games_metadata), True)
        self.assertEqual(favorite_author('Bearcat', []), False)
        self.assertEqual(favorite_author('', games_metadata), False)
        self.assertEqual(favorite_author('Bearcat', canada_metadata), False)
        self.assertEqual(favorite_author('', []), False)

    def test_title_and_author_unit_test(self):
        canada_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        canada_title_and_author = [('List of Canadian musicians', 'Jack Johnson'), ('Lights (musician)', 'Burna Boy'), ('Old-time music', 'Nihonjoe'), ('Will Johnson (soccer)', 'Burna Boy')]
        music_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842]]
        music_title_and_author = [('List of Canadian musicians', 'Jack Johnson'), ('French pop music', 'Mack Johnson'), ('Noise (music)', 'jack johnson'), ('1922 in music', 'Gary King'), ('1986 in music', 'jack johnson'), ('Kevin Cadogan', 'Mr Jake'), ('2009 in music', 'RussBot'), ('Rock music', 'Mack Johnson'), ('Lights (musician)', 'Burna Boy'), ('Tim Arnold (musician)', 'jack johnson'), ('Old-time music', 'Nihonjoe'), ('Arabic music', 'RussBot'), ('Joe Becker (musician)', 'Nihonjoe')]
        games_metadata = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]]
        games_title_and_author = [('List of dystopian music, TV programs, and games', 'Bearcat'), ('Georgia Bulldogs football', 'Burna Boy'), ('Spawning (computer gaming)', 'jack johnson')]
        self.assertEqual(title_and_author(canada_metadata), canada_title_and_author)
        self.assertEqual(title_and_author(music_metadata), music_title_and_author)
        self.assertEqual(title_and_author(games_metadata), games_title_and_author)
        self.assertEqual(title_and_author([]), [])
    
    def test_refine_search_unit_test(self):
        canada_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        music_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842]]
        games_metadata = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]]
        self.assertEqual(refine_search('canada', games_metadata), [])
        self.assertEqual(refine_search('canada', music_metadata), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755]])
        self.assertEqual(refine_search('games', music_metadata), [])
        self.assertEqual(refine_search('', canada_metadata), [])
        self.assertEqual(refine_search('music', []), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test2(self, input_mock):
        keyword = 'canada'
        advanced_option = 2
        advanced_response = 7000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test3(self, input_mock):
        keyword = 'canada'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test4(self, input_mock):
        keyword = 'canada'
        advanced_option = 4
        advanced_response = 'Burna Boy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]\nYour favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test5(self, input_mock):
        keyword = 'canada'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: [('List of Canadian musicians', 'Jack Johnson'), ('Lights (musician)', 'Burna Boy'), ('Old-time music', 'Nihonjoe'), ('Will Johnson (soccer)', 'Burna Boy')]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_example_integration_test6(self, input_mock):
        keyword = 'canada'
        advanced_option = 6
        advanced_response = 'music'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755]]\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_example_integration_test7(self, input_mock):
        keyword = 'canada'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]\n"

        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
