class node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self,value):
        temp = node()
        temp.value = value
        temp.next = None
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = temp

    def length(self):
        length = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            length += 1
        return length

    def delete(self,index):
        if index >= self.length():
            print("Index out of bound")
            return
        cur  = self.head
        cur_index = 0
        while True:
            prev = cur
            cur = cur.next
            if cur_index == index:
                prev.next = cur.next
                return
            cur_index +=1


    def display (self):
        cur= self.head.next
        elem = []
        l = self.length()
        while l:
            elem.append(cur.value)
            cur = cur.next
            l -= 1
        return elem

    def insert(self,value,index):
        cur = self.head
        cur_index = 0
        temp = node(value)
        while(cur.next != None):
            prev = cur
            cur = cur.next
            if cur_index == index:
                prev.next = temp
                temp.next = cur
                return


mylist = linkedlist()
print(mylist.display())
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist.display())
mylist.delete(0)
print(mylist.display())
mylist.insert(10,0)
print(mylist.display())



