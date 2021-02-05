# submission.py
# ----------------
# Attribution Information: This part of the project was adapted from CS221 and 
# the PacMan Projects. 
# For the PacMan Projects: 
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# 08-2019
 


import math 
import collections
import shop


############################################################
# Question 1 - addition 

def add(a, b): 
    "Return the sum of a and b"
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    c = a + b
    return c
    # END_YOUR_CODE


############################################################
# Question 2 - buyLotsOfFruit 
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order. If some fruit is not in list, print an error 
    message and return None.
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    sum = 0
    for i in orderList:
        if i[0] in fruitPrices.keys():
            item_net_cost = i[1] * fruitPrices.get(i[0])
            totalCost += item_net_cost
        else:
            return None

    return totalCost
    # END_YOUR_CODE


############################################################
# Question 3 - shopSmart 

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops

    Return the FruitShop where your order costs the least.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    costs = []

    for shop in fruitShops:
        mydict = shop.fruitPrices
        sum = 0
        for i in orderList:
            if i[0] in mydict.keys():
                item_net_cost = i[1] * mydict.get(i[0])
                sum += item_net_cost
            else:
                return None
        costs.append(sum)

    min_index = costs.index(min(costs))
    min_cost_shop = fruitShops[min_index]

    return min_cost_shop
    # END_YOUR_CODE


############################################################
# Question 4 - findAlphabetLastWord 

def findAlphabetLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    x =text
    x = x.strip().split()

    x = sorted(x)
    return x[-1]
    # END_YOUR_CODE


############################################################
# Question 5 - euclideanDistance 

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    dist = math.sqrt(pow(loc1[0] - loc2[0], 2) + pow(loc1[1] - loc2[1], 2))
    dist = round(dist, 11)
    return dist
    # END_YOUR_CODE


############################################################
# Question 6 - findSingletonWords

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    If no singleton words exist return the emptyset.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    text = text.strip().split()
    mappy = {}

    for x in text:
        if x in mappy:
            mappy[x] = mappy[x] + 1
        else:
            mappy[x] = 1

    single_word = set()

    for i in mappy:
        if mappy[i] == 1:
            single_word.add(i)

    return single_word
    # END_YOUR_CODE


############################################################
# Question 7 - lenLongestPalindrome

def lenLongestPalindrome(text): 
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana'). 
    Computer the length of the longest palindrome that can be obtained by 
    deleting letters from text. 
    Do not try a brute force approach on this function.  Your algorithm should 
    run in O(len(text)^2) time. 
    Consider defining a recurrence before you begin coding. 
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    if len(text) == 1:
        return 1

    if len(text) == 2 and text[0] == text[-1]:
        return 2
    if len(text) == 2 and text[0] != text[-1]:
        return 1

    sub_strings = []
    check_string = []

    def same_letter_substring(text):

        if text in check_string:
            return check_string

        if len(text) == 1 or len(text) == 0:
            return

        if text in sub_strings:
            return

        if text[0] == text[-1]:
            sub_strings.append(text)
            return sub_strings
        if text in check_string:
            return check_string

        same_letter_substring(text[1:-1]), same_letter_substring(text[1:]), same_letter_substring(text[:-1])

        check_string.append(text)

        return sub_strings

    sub_strings = same_letter_substring(text)

    def longpal(sub_strings):
        arr = []
        for i in sub_strings:
            sum = 3

            def func(i):
                if len(i) == 1:
                    return sum + 1
                if len(i) == 0:
                    return sum
                if i[1] == i[-2]:
                    func(i[2:-3])
                    return 2 + sum
                else:
                    func(i[2:-2])
                    func(i[1:-3])
                return sum

            x = func(i)
            arr.append(x)
        return arr

    x = longpal(sub_strings)
    x = max(x)
    return x


    #END_YOUR_CODE    


############################################################
#  Extra Functions you may want to define