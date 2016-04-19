#-*- coding: UTF-8 -*-

from math import sqrt
from rawdata import users,critics
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

def topMatches(prefer,person,similarity=euclidean,n=3):
    nearestlist = [ (similarity(prefer,person,user),user)  for user in prefer if user!=person]
    nearestlist.sort()
    nearestlist.reverse()
    return nearestlist[0:n]
#print topMatches(users,'Hailey',pearson)
# dictmp = {}
# for person in critics:
#     tmpvalue = topMatches(critics,person)
#     dictmp[person] = tmpvalue
# for key in dictmp:
#     print key + ":" 
#     print dictmp[key]

#利用所有人他人评价值的加权平均，为某人提供推荐
def getRecommendations(prefer,person,similarity=pearson):
    totals = {}
    simsum = {}
    for other in prefer:
        #不能和自己比较
        if other == person: continue
        # 计算出2个人的相似度
        sim = similarity(prefer,person,other)
        if sim <= 0:continue
        for item in prefer[other]:
            if item not in prefer[person] or prefer[person][item]==0:
                totals.setdefault(item,0)
                totals[item] += sim*prefer[other][item]
                simsum.setdefault(item,0)
                simsum[item] += sim

    rankings = [(totals[item]/simsum[item],item) for item in totals]
    rankings.sort
    rankings.reverse()
    return rankings
# print getRecommendations(critics,'Toby')


"""
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}}
"""
def transformPrefers(prefer):
    resuslt = {}
    for person in prefer:
        for  item in prefer[person]:
            resuslt.setdefault(item,{})
            resuslt[item][person]= prefer[person][item]

    return resuslt
books = transformPrefers(critics)
print topMatches(books,"Superman Returns",pearson)