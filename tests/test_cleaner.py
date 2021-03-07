from grandpy.cleaner import Cleaner

def test_select_the_sentence_with_the_unique_location_word_of_the_text():
	cleaner = Cleaner("Hello Grandpy ! How was your evening with Grandma yesterday? By the way, as i am here, can you tell where is the museum of Art and History of Fribourg please? My deer salutations.")
	expected_result = 'museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result

def test_select_all_sentences_with_location_words():
	cleaner = Cleaner("I would like to go to Switzerland! Can you tell where is the museum of Art and History of Fribourg please?")
	expected_result = 'switzerland museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result	

def test_delete_all_words_before_the_unique_location_word():
	cleaner = Cleaner("There is the Eiffel Tower, the Arc de Triomphe, but tell me where the museum of Art and History of Fribourg is.")
	expected_result = 'museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result

def test_delete_all_words_before_location_words_in_concerned_sentences():
	cleaner = Cleaner("Do you know where La Sarine is? You know Grandpy, i really want to go to Switzerland. Can you tell me the address of the museum of Art and History of Fribourg.")
	expected_result = 'la sarine switzerland museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result

def test_lower_the_text():
	cleaner = Cleaner("I would like to go to the Eiffel Tower")
	expected_result = 'eiffel tower'
	result = cleaner.clean_message()
	assert result == expected_result

# def test_lower_the_text_without_location_words():
# 	cleaner = Cleaner("Eiffel Tower please")
# 	expected_result = "eiffel tower"
# 	result = cleaner.clean_message()
# 	assert result == expected_result		

def test_remove_punctuation():
	cleaner = Cleaner("Do you want to go to the Eiffel Tower???")
	expected_result = 'eiffel tower'
	result = cleaner.clean_message()
	assert result == expected_result

def test_get_keywords():
	cleaner = Cleaner("I want to go to the museum of art and history of fribourg")
	expected_result = 'museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result

def test_stringify_keywords():
	cleaner = Cleaner("where is the museum of art and history of fribourg please?")
	expected_result = 'museum art history fribourg'
	result = cleaner.clean_message()
	assert result == expected_result


# pytest --cov=grandpy  --cov-report html test_*.py