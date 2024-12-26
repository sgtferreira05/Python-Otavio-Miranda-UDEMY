# Implementing the Iterator protocol in Python.
# This is merely an introductory lesson on the collections.abc protocols. Any other protocol can be implemented following the same sctruture used in this class.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence
class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
    
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1
    
    def __len__(self) -> int:
        return self._index
        

    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    list = MyList()
    list.append('Mary', 'Helena')
    list[0] = 'Jhonn'
    list.append('Louis')
    # print(list._data)
    # print(len(list))
    for item in list:
        print(item)
    
    print('----')
    for item in list:
        print(item)