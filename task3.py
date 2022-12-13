class MyList(list):
    def __getitem__(self, lst):
        print('Работает магический метод')
        return super().__getitem__(lst)

    def __init__(self, lst):
        print('Работает магический метод')
        return super().__init__(lst)
    

    def __len__(self):
        print('Работает магический метод')
        return super().__len__()

    def __str__(self):
        print('Работает магический метод')
        return super().__str__()

    def __repr__(self):
        print('Работает магический метод')
        return super().__repr__()






lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
        lst[2] = 'Python'

        print(lst)
        print(len(lst))
