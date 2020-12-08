# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        integerList = []
        while start <= stop:
            integerList.append(start)
            start += stop
        return integerList

    def get_even_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        evenList = []
        while start <= stop:
            if start % 2 == 0:
                evenList.append(start)
                start += step
            else:
                start += step
        return evenList

    def get_odd_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        oddList = []
        while start <= stop:
            if start % 2 != 0:
                oddList.append(start)
                start += stop
            else:
                start += stop
        return oddList
