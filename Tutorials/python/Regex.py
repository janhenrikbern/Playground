import re # regex python standard library module 

string = 'It is a nice day in New Jersey. Time to go for a walk!'

# create a list of chars sorted by frequency in descending order
s = re.sub(r'[^a-zA-Z\s]+', '', string)
print('Filter non-letter, non-whitespace chars:\n {}\n'.format(s))
s = s.lower()
print('All lowercase:\n {}\n'.format(s))
s = re.sub(r'\s+', '', s)
print('Remove whitespace:\n {}\n'.format(s))

unique_chars = set(s)
chars = {}
for c in unique_chars:
    occurances = re.findall(c, s)
    chars[c] = len(occurances)

# create a sorted 
from Heaps import SimpleBinaryHeapTree as Heap

heapCondition = lambda kv_1, kv_2: kv_1[1] > kv_2[1]
heap = Heap(heapCondition)
for kv in chars.items():
    heap.add(kv)

for i in range(len(heap)):
    print(heap.pop())



