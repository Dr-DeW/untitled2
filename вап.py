import time


class TumbIter:
    def __init__(self, obj):
        self.obj = obj
        self.cur = 0

    def __iter__(self):
        return self

    def to_start(self):
        self.cur = 0

    def to_curret(self, val):
        if val >= len(self.obj) or val < 0:
            print('Nelzya')
        else:
            self.cur = val

    def __next__(self):
        if self.cur < len(self.obj):
            res = self.obj[self.cur]
            self.cur += 1
            return res
        raise StopIteration

class Tumbo:
    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }
    def __len__(self):
        return len(self.ret_list_tumb())
    def __iter__(self):
        return TumbIter(self.ret_list_tumb())
    def ret_list_tumb(self):
        li = []
        for i in self.boxes:
            for o in self.boxes[i]:
                li.append(o)
        return li
    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print('nepravilno')
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print('nepravilno')
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ', '.join(boxes_items)


tumb = Tumbo()
tumb.add_to_box('noj', 1)
tumb.add_to_box('karandash', 2)
tumb.add_to_box('kniga', 3)
tumb.add_to_box('apple', 1)
it = iter(tumb)
print(next(it))
print(next(it))
if next(it) == 'karandash': it.to_start()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
