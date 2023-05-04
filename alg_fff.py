class Tumb_Iterator:
    def __iter__(self):
        return self
    def __init__(self, some_obj):
        self.some_obj = some_obj
        self.cur = 0
    def __next__(self):
        if self.cur < len(self.some_obj):
            res = self.some_obj[self.cur]
            self.cur += 1
            return res
        raise StopIteration
    def to_start(self):
        self.cur = 0
    def to_cur(self,val):
        if val >= len(self.some_obj):
            print('Вышли из диапазона')
        else:
            self.cur = val


class Tumb:
    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def __iter__(self):
        return  Tumb_Iterator(self.boxes[1] + self.boxes[2] + self.boxes[3])

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print('Неправильный номер тумбочки')
        else:
            self.boxes[box_num].append(obj)

    def remove_to_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print('Неправильный номер тумбочки')
        else:
            self.boxes[box_num].pop()

    def __str__(self):
        boxes_item = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ', '.join(boxes_item)


tum = Tumb()
tum.add_to_box('apple', 1)
tum.add_to_box('coffe', 2)
tum.add_to_box('pen', 3)
tum.add_to_box('sam', 1)

for i in tum:
    print(i)