import re
import os.path
import string


class Text:
    """A class that get file direction."""
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise OSError("no such direction")
        self.filename = filename

    def characters(self):
        """"Function that counting of characters in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            count_characters = len(data)
        myfile.close()
        return count_characters

    def words(self):
        """"Function that counting of word in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            for i in string.punctuation:
                data = data.replace(i, ' ')
            count_words =  len(data.split())
            myfile.close()
        return count_words

    def sentences(self):
        """"Function that counting of sentences in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            for i in data:
                if i == '\n':
                 data = data.replace(i, '')
            number_of_str = len(list(filter(None,re.split(r'[.!?]+', data))))
        myfile.close()
        return number_of_str
    def __str__(self):
        return f'Characters: {self.characters()}, Words: {self.words()}, Sentences: {self.sentences()}'

obj1 = Text('text.txt')
print(obj1)
