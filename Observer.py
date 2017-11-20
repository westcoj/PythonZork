'''
Created on Nov 8, 2017

@author: Cody
'''
from abc import ABCMeta, abstractmethod

class Observer(object):
    '''
    Abstract class for observing anything that is observable
    '''


    __metaclass__ = ABCMeta

    
    @abstractmethod
    def update(self):
        """
        Abstract method for Observer classes
        """
        pass
    


class Observable(object):
    '''
    Abstract class for anything that needs to update an observer
    '''
    def __init__(self):
        """
        Default constructer that sets up list of observers
        """
        self.observers = []
        
    def add_observer(self,observer):
        """Adds observer to list

        Args:
            observer: class that will be observing

        """
        if not observer in self.observers:
            self.observers.append(observer)
            
    def remove_observer(self, observer):
        """Removes observer in list

        Args:
            observer: class that will no longer be observing

        """
        if observer in self.observers:
            self.observers.remove(observer)
            
    def remove_all_observers(self):
        """Removes all observers in list

        """
        self.observers = []