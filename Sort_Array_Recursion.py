arr = [2, 3, 5, 4, 10, 3, 4, 5, 2, 1, -10, 0]
class Sorting:

    def insert(self, arr, temp):
        if len(arr) == 0 or arr[len(arr) - 1] <= temp:
            arr.append(temp)
            return
        
        val = arr[len(arr) - 1]
        arr.pop()
        self.insert(arr, temp)
        arr.append(val)
        

    def sort(self, arr):
        if len(arr) == 1:
            return
        temp = arr[len(arr) - 1]
        arr.pop()
        self.sort(arr)
        self.insert(arr, temp)
        return arr
    

obj = Sorting()
print(obj.sort(arr))
