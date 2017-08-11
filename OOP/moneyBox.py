#! python3
# moneyBox.py - implementations class MoneyBox for working with virtual capacity


class MoneyBox:
    ''' constructor with argument - capacity of '''

    def __init__(self, capacity):
    	self.count = 0
    	self.capacity = capacity    
    

    def can_add(self, v):
        ''' True, if to add v coins in a counter is possible  '''

        if self.count + v <= self.capacity:
            return True


    def add(self, v):
        ''' To add v coins в in counter '''

        if self.can_add(v) == True:
            count = self.count + v
            print('You added {} coins. Thank you!'.format(count))
            return count
        else:
            print ('Sorry, you can add no more than {} coins :('.format(money.capacity))


money = MoneyBox(100)  
deposit = int(input('How many coins would you like to add to the capacity?'))
money.add(deposit)               
