'''
Created on 15 Feb 2021

@author: Francisco Dominguez
Default implementation is a priority queue
'''
from queue import PriorityQueue
class AISearchCollection(object):
    def __init__(self):
        self.nodes=PriorityQueue()
        '''
        Select a node and remove from the collection
        '''
    def selectNode(self):
        (_,n)=self.nodes.get()
        return n
    def isEmpty(self):
        return self.nodes.empty()
    def insert(self,node):
        priority=node.getF()
        self.nodes.put((priority,node))
    '''
    Is the node in the collection?
    '''
    def contains(self,node):
        for (_,n) in self.nodes.queue:
            if n==node:
                return True
        return False
            