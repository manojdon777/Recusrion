arr = [0,1,5,2]
arr = [2, 3, 5, 4, 10, 3, 4, 5, 2, 1, -10, 0]
class Sorting:
    def insert(self, arr, num):
        length = len(arr)
        if len(arr) == 0 or arr[ len(arr)-1 ] <= num:
            arr.append(num)
            return   
        temp = arr.pop()
        self.insert(arr, num)
        arr.append(temp)

    def sort(self, arr):        
        if len(arr) == 1:
            return
        temp = arr.pop()
        self.sort(arr)
        self.insert(arr, temp)
        return arr

obj = Sorting()
print(obj.sort(arr))

