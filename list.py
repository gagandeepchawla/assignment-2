# 1) Write a python program to find the maximum consecutive sum of integers in a list.
class maxnumber():
    def checkmax(self):
        count = int(raw_input('Enter the list you'))
        check = True
        list2 = []
        while check:
            print ('The Remaining Counts are-{}'.format(count))
            number1 = int(raw_input('Enter the First number'))
            number2 = int(raw_input('Enter the Second number'))
            list = [number1, number2]
            total = 0
            for i in list:
                total = total + i
            list2.append(total)
            count = count - 1
            if count == 0:
                check = False
        self.listmax(list2)

    def listmax(self,list=[]):
        print 'the maximum number are',max(list)


n = maxnumber()
n.checkmax()
