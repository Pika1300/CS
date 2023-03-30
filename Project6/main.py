'''
Project:
Author: d
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    bst=BST()
    file = open('CS/Project6/around-the-world-in-80-days-3.txt', 'r')
    for l in file:
        for x in l:
            if x.isalpha()==True:
                bst.add(Pair(x.lower()))
            elif x.isnumeric()==True:
                bst.add(Pair(x))
            else:
                pass
    return(bst)

def main():
    tree=make_tree()
    print(tree.inorder())
    print(tree.size())
    tree.remove(Pair("c"))
    print(tree.inorder())
    print(tree.size())
if __name__ == "__main__":
    main()
