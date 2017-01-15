#!/usr/bin/env python2
#encoding: UTF-8

class Worker:
    
    def __init__(self, title, task, data, interval = 0):
        self.title = title
        self.task = task
        self.data = data
        self.interval = interval
        self.quit = False
        
    def run(self):
        while not quit:
            self.data = self.task.read()

    def getTitle(self):
        return self.title