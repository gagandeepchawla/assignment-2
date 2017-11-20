    # Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
class twosum:
    def sum(self,number1, number2):
        add = number1 + number2
        return add

    def check(self,number1, number2):
        check1 = self.sum(number1, number2)
        if check1 in range(10, 19):
            print 20
        else:
            print check1

    def insert(self):
        first = int(raw_input("Enter the First Number\n"))
        second = int(raw_input("Enter the second Number\n"))
        self.check(first, second)

n = twosum()
n.insert()
