import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
from . import constants


class Cleaner:
    """
    Clean the user input

    """

    def __init__(self, message):
        """
        Init method for the Cleaner class

        Parameters
        ----------
        message : str
            Input from the user
        """
        self.message = message
        self.location_words = []
        for word in constants.LOCATION_WORDS:
            if word in self.message:
                self.location_words.append(word)

    def clean_message(self, location_word=True):
        """
        Clean the user input

        Params
        -------
        location_word: boolean

        Returns
        -------
        string: remaining keywords

        """
        self.__select_sentence(location_word)
        self.__delete_before_location_words(location_word)
        self.__lower_message(location_word)
        self.__remove_punctuation()
        self.__get_keywords()
        return self.__stringify_keywords()

    def __select_sentence(self, location_word):
        """
        Select sentences with location words

        Params
        -------
        location_word: boolean

        Returns
        -------
        list: list of sentences with location words

        """
        if location_word:
            sentences = nltk.sent_tokenize(self.message)
            self.selected_sentences = []
            for sentence in sentences:
                for word in self.location_words:
                    key_sentences = {}
                    if word in sentence:
                        key_sentences["sentence"] = sentence
                        key_sentences["word"] = word
                        self.selected_sentences.append(key_sentences)
            return self.selected_sentences
        else:
            pass

    def __delete_before_location_words(self, location_word):
        """
        In selected sentences, delete words before location words

        Params
        -------
        location_word: boolean

        Returns
        -------
        string: remaining words

        """

        if location_word:
            self.result_after_location_word = ""
            for key_sentence in self.selected_sentences:
                result_after_location_word = re.sub(
                    r"^.+?(?={})".format(key_sentence["word"]),
                    "",
                    key_sentence["sentence"],
                )
                result_after_location_word += " "
                self.result_after_location_word += result_after_location_word
            return self.result_after_location_word
        else:
            pass

    def __lower_message(self, location_word):
        """
        Lower letters

        Params
        -------
        location_word: boolean

        Returns
        -------
        string: remaining words with lowered letters

        """
        if location_word:
            self.lowered_message = self.result_after_location_word.lower()
        else:
            self.lowered_message = self.message.lower()
        return self.lowered_message

    def __remove_punctuation(self):
        """
        Remove punctuation

        Returns
        -------
        string: string without punctuation

        """
        self.no_punctuation_message = self.lowered_message.translate(
            str.maketrans("", "", string.punctuation)
        )
        return self.no_punctuation_message

    def __get_keywords(self):
        """
        Stop words

        Returns
        -------
        list: list of keywords

        """
        my_stop_words = set(
            constants.LOCATION_WORDS
            + constants.COURTESY_WORDS
            + stopwords.words("english")
        )
        words = word_tokenize(self.no_punctuation_message)
        self.list_of_keywords = [w for w in words if w not in my_stop_words]
        return self.list_of_keywords

    def __stringify_keywords(self):
        """
        Stringify list of keywords

        Returns
        -------
        string: keywords
        """
        if self.list_of_keywords == []:
            self.keywords = []
        else:
            separator = " "
            self.keywords = separator.join(self.list_of_keywords)
        return self.keywords
