#! /usr/bin/python
# *-* conding:utf8 *-*

from math import sqrt
from rawdata import *
import sys

def manhattan(prefer,person1,person2):
    sharelist=[]
    for item in prefer[person1]:
        if item in prefer[person2]:
            sharelist.append(item)

    if len(sharelist)==0:
        return 0
    sumscores = sum([pow(prefer[person1][item]-prefer[person2][item],2) for item in sharelist])
    # return 1/(1+sqrt(sumscores))

def euclidean(prefer,person1,person2):
    sharelist=[]
    for item in prefer[person1]:
        if item in prefer[person2]:
            sharelist.append(item)

    if len(sharelist)==0:
        return 0
    sumscores = sum([pow(prefer[person1][item]-prefer[person2][item],2) for item in sharelist])
    return 1/(1+sqrt(sumscores))

def pearson(prefer,person1,person2):
    """" pearson distance function"""
    sharelist=[]
    for item in prefer[person1]:
        if item in prefer[person2]:
            sharelist.append(item)
    # print sharelist
    n = len(sharelist)
    if  n ==0:
        return 0
    # sum(person1) and sum(person2)
    sum1 = sum([prefer[person1][item] for item in sharelist])
    sum2 = sum([prefer[person2][item] for item in sharelist])

    # sum(person1**2)  and sum(person2 **)
    sum1Sq = sum([prefer[person1][item]**2 for item in sharelist])
    sum2Sq = sum([prefer[person2][item]**2 for item in sharelist])

    #sum(person1* person2)
    pSum = sum([prefer[person1][item] * prefer[person2][item] for item in sharelist])

    num = pSum - (sum1 * sum2/n)
    den =  sqrt((sum1Sq-sum1**2/n) * (sum2Sq-sum2**2/n))
    # return den
    if den==0 : return 0
    return num/den

def nearest(prefer,person,military=euclidean,n=3):
    nearestlist = [ (military(prefer,person,user),user)  for user in prefer if user!=person]
    nearestlist.sort()
    nearestlist.reverse()
    return nearestlist[0:n]
#print nearest(users,'Hailey',pearson)
dictmp = {}
for person in critics:
    tmpvalue = nearest(critics,person)
    dictmp[person] = tmpvalue
for key in dictmp:
    print key + ":" 
    print dictmp[key]