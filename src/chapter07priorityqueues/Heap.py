
class Heap:
    def __init__(self):
        self.heapList = [0]  # Elements in Heap
        self.size = 0  # Size of the heap

    def parent(self, index):
        """
        Parent will be at math.floor(index/2). Since integer division
        simulates the floor function, we don't explicitly use it
        """
        return index // 2

    def leftChildIndex(self, index):
        return 2 * index

    def rightChildIndex(self, index):
        return 2 * index + 1

    def leftChild(self, index):
        if 2 * index <= self.size:
            return self.heapList[2 * index]
        return -1

    def rightChild(self, index):
        if 2 * index + 1 <= self.size:
            return self.heapList[2 * index + 1]
        return -1

    def minChild(self, index):
        if 2 * index + 1 > self.size:
            return 2 * index
        if self.heapList[2 * index] < self.heapList[2 * index + 1]:
            return 2 * index
        return 2 * index + 1

    def percolateUp(self, i):
        # From Bottom to Top
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = (
                    self.heapList[i // 2],
                    self.heapList[i],
                )
            i = i // 2

    def percolateDown(self,i):
        # From Top to Bottom
        while 2*i < self.size:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def buildHeap(self, A):
        i = len(A) // 2
        self.size = len(A)
        self.heapList = [0] + A[:]

        while i > 0:
            self.percolateDown(i)
            i = i - 1

    def deleteMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percolateDown(1)
        return retval

# HOrig = Heap()
# # add some nonsense:
# HOrig.insert(1)
# HOrig.insert(20)
# HOrig.insert(5)
# HOrig.insert(100)
# HOrig.insert(1000)
# HOrig.insert(12)
# HOrig.insert(18)
# HOrig.insert(16)

l1 = [127, 220, 534, 565, 933]
l2 = [246, 277, 321, 454]

h1 = Heap()
h1.buildHeap(l1 + l2)
print(h1.heapList)

while h1.size:
    val = h1.deleteMin()
    print(val)