class CircularBuffer:
    def __init__(self, n):
        self.__max_size = n
        self.__list = []

    def add(self, item):
        if len(self.__list) < self.__max_size:
            self.__list.append(item)
        else:
            self.__list.pop(0)
            self.__list.append(item)

    def __getitem__(self, index):
        return self.__list[index]

    def __len__(self):
        return len(self.__list)