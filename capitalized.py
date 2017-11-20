#5) Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
class capitalized:
    def insert(self):
        first = raw_input('Enter the First String\n')
        self.upper(first)
    def upper(self,first):
        first = first.upper()
        print 'The first string are-',first

n = capitalized()
n.insert()