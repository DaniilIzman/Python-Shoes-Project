class ShoeCollectionClass:
    def __init__(self):
        self.data = []
    def add(self,item):
        self.data.append(item)
    def get(self,index):
        if 0 <= index < len(self.data):
            return self.data[index]
    def size(self):
        return len(self.data)
    def printCollection(self):
        for i in range(self.size()):
            print("Instance(Collection)",i + 1,"in Sport Shoe: ")
            self.get(i).display()
