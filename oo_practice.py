class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """create a SerialGenerator with provided start value"""
        self.start = self.next = start

    def __repr__(self):
        return f"<Start Value: {self.start}, Next Serial Number: {self.next}>"

    def generate(self):
        """return a unique serial number when called"""
        self.next += 1
        return self.next -1

    def reset(self):
        """reset to original starting serial number"""
        self.next = self.start

class WordFinder:
    """Finds random words from a file that contains words, one per line"""

    def __init__(self, path):
        """initialize WordFinder with empty list and path to list of words, calls word_reader on self"""
        self.word_list = []
        self.path = path
        self.word_reader()

    def word_reader(self):
        """iterates through file on path, appends to word_list and returns # of words read"""
        self.word_file = open(self.path)
        for line in self.word_file:
            self.word_list.append(line)
        self.word_file.close()
        print(f"{len(self.word_list)} words read")
            
    
    def random(self):
        """picks a random word from word_list and returns it, without newline character"""
        from random import choice
        return choice(self.word_list)[:-1]
    
class SpecialWordFinder(WordFinder):
    """Finds random words from a file that contains words, one per line and ignores blank lines and comments"""

    def __init__(self, path):
        """initialize WordFinder with empty list and path to list of words, calls word_reader on self"""
        super().__init__(path)

    def word_reader(self):
        """iterates through file on path, appends to word_list and returns # of words read, ignores empty lines and comments"""
        self.word_file = open(self.path)
        for line in self.word_file:
            if "#" not in line and len(line) > 1:
                self.word_list.append(line)
        self.word_file.close()
        print(f"{len(self.word_list)} words read")