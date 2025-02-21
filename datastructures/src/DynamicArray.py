# Dynamic Array (even though python already treats all arrays as "dynamic")

class DynamicArray:
    def __init__(self, capacity:int=16):
        if capacity < 0: raise Exception("Capacity cannot be negative")

        self.len = capacity;
        self.capacity = capacity
    
        self.arr = [None] * self.capacity

        self._is_sorted = False

    def __str__(self):
        return str(self.arr[:self.len])

    def __grow_capacity(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.len):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def __iter__(self):
        return self

    def length(self) -> int:
        return self.len
    
    def get(self, idx):
        return self.arr[idx]
    
    def set(self, idx, val):
        self.arr[idx] = val

    def append(self, value):
        if self.len == self.capacity:
            self.__grow_capacity()

        self.arr[self.len] = value

        self.len += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Index must be greater than 0")
        elif idx > self.len:
            idx = self.len
        
        if self.len == self.capacity:
            self.__grow_capacity()

        tmp = self.arr.copy()
        for i in range(idx, self.len):
            self.arr[i+1] = tmp[i]

        self.arr[idx] = value

        self.len += 1

    def delete(self, idx):
        if idx < 0 or idx >= self.len:
            raise IndexError("Index out of range")
        
        val = self.arr.pop(idx)

        self.len -= 1
        self.capacity -= 1

        return val
    
    def sort(self):
        if self._is_sorted: # save time
            return

        self.arr = sorted(self.arr[:self.len]) + [None] * (self.capacity - self.len)

        self._is_sorted = True
    
    def binary_search(self, target):
        self.sort()

        l, r = 0, self.len-1

        while l < r:
            mid = (l + r) // 2

            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                r = mid - 1
            elif self.arr[mid] < target:
                l = mid + 1

        return -1

if __name__=="__main__":
    d = DynamicArray()
    d.set(0, 4)
    d.set(1, 3)
    d.set(2, 2)
    d.set(3, 1)
    d.set(4, 0)
    print(d, ":", d.length(), ":", d.capacity)

    d.sort()
    print(d, ":", d.length(), ":", d.capacity)
    
    assert d.binary_search(3) == 3

    # print(d)