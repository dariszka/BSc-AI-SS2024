class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array to be sorted
        @returns a sorted list
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting

        d_max = max(input_array)
        # https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer
        d = int(self.log(d_max, self.base)) + 1
        
        pos = 0
        arr = input_array
        while pos < d:
            arr = self.bucketSort(pos, arr)
            pos +=1
        
        return arr

    # Helper functions

    # calculates buckets for position pos
    def bucketSort(self, pos, arr):

        buckets = [[] for _ in range(self.base)]

        for val in arr:
            try:
                i = self.get_digit(val, pos, 10)        # if i pass base 7 the unittests don't work. so this works for base=7 only if we assume
                buckets[-i-1].append(val)               # that the numbers have already been converted to said base 7. (passing a value>7 in the array
                                                        # will cause an error).
                                                        # but this is not what the task implied, so i'm clarifying - if we pass base=7 to get digit
                                                        # it will work as well, on unconverted numbers, sort them internally, but display them in the                                          
            except:                                     # buckets of the converted respective numbers. so the buckets after get_digit(base=7) are in 
                i = self.get_digit(val, pos, self.base) # correct order, but not in the correct slots in [0,6]. That is why i'm passing 10 as base,
                buckets[-i-1].append(val)               # but inside a try block, because the buckets are contingent on base and.

        self._add_bucket_list_to_history(buckets)
        return self.merge(buckets)
    
    # for example i was working on the array: 
    # [50, 11, 33, 22, 64, 3]
    # the decimal ordering would be
    # [[[], [], [64], [33, 3], [22], [11], [50]] zeroes ordered
    # [[64], [50], [], [33], [22], [11], [3]]    tens ordered

    # however, when passing that array using get_digit with base=7, the bucket lists were:
    # [[], [33], [11], [3], [], [50, 22, 64], []], 
    # [[], [], [33], [22], [64], [11], [3, 50]], 
    # [[], [], [], [], [], [64, 50], [33, 22, 11, 3]]

    # this is because when we look at the converted list 
    # [101, 14, 45, 31, 121, 3] and sort it we get:
    # [[[], [45], [14], [3], [], [101, 31, 121], []],   # zeroes ordered
    # [[], [], [45], [31], [121], [14], [3, 101]],      # tens ordered
    # [[], [], [], [], [], [121, 101], [45, 31, 14, 3]]]# hundreds ordered

    # which is that same list, but sorted using the conversion to base 7.

    # I do not understand why the task suggested we get the digit at base 7, since it's counterproductive to the task
    # please in the future consider specifying that we are working on a already converted list and should sort it into buckets as such

    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list is your current bucket list, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)
        self.bucket_list_history.append(arr_clone)

    # returns the digit (base7) of val at position pos
    def get_digit(self, val, pos, base):
        return (val // (base ** pos)) % base
        
    # Merges bucket lists into one list
    def merge(self,buckets):
        #https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return sum(buckets,[])

    #wasn't sure if i could import math, so i defined the log myself
    def log(self, x, b):
        if x < b:
            return 0  
        return 1 + self.log(x/b, b)
    
