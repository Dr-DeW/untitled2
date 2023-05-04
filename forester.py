class node:
    def __init__(self,val):
        self.value = val
        self.children = []
    def __str__(self):
        return f'{self.value}'
root = node('A')
root.children.append(node('B'))
root.children.append(node('C'))
root.children[0].children.append(node('D'))
root.children[0].children.append(node('E'))
root.children[1].children.append(node('F'))
root.children[1].children[0].children.append(node('j'))
print(root.children[1].children[0].children[0])
# for i in root.children:
#     print(i.value)
#     for c in i.children:
#         print(c.value)
#         for h in c.children:
#             print(h.value)