#! /usr/bin/python
import random

# mylist = random.sample(xrange(100),30)
mylist=(52, 45, 42, 5, 32, 16, 17, 67, 20, 57, 88, 95, 58, 84, 54, 78, 8, 31, 99, 33, 53, 12, 61, 94, 87, 97, 44, 26, 76, 15)
def k_means(testlist,k):
    kdic = {}
    # klist =  random.sample(mylist,k)
    klist = [16,58,87,15]
    classlist = []
    for i in klist:
        classlist.append[KeyMeans(i)]
    for item in mylist:
        if item not in klist:
            result  =  instance(item,klist)
            kdic[result[1]].append(item)
    for item in kdic:
        kdic[item] =float(sum(kdic[item])/len(kdic[item]))
    print kdic 
def instance(key,alist):
    resutltlist = [(abs(item-key),item) for item in alist]
    resutltlist.sort()
    return resutltlist[0]

k_means(mylist,4)
class KeyMeans(object):
    self.keyvalue = 0
    self.keylist=[self.key]
    self.keymid = self.keyvalue