# Using Array
class hashMap:

    def __init__(self, size=11):
        self.size = size
        self.buckets = [[] for i in range(self.size)]
    def __len__(self):
        return self.size
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        ndx = self.hash_function(key)
        bucket = self.buckets[ndx]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value)) 
    
    def get(self, key):
        ndx = self.hash_function(key)
        bucket = self.buckets[ndx]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                return v
        return None
    
    def remove(self, key):
        ndx = self.hash_function(key)
        bucket = self.buckets[ndx]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
        return None

hm = hashMap(5)
print(len(hm))    
hm.put(5, 56)
print(hm.get(5))
hm.remove(5)
print(hm.get(5))