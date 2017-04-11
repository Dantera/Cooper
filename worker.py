#!/usr/bin/env python2
#encoding: UTF-8

import time

class Worker:
    
    def __init__(self, title, task, data, interval = 0):
        self.title = title
        self.task = task
        self.data = data
        self.interval = interval
        self.quit = False
        
    def run(self):
        while not self.quit:
            self.data = self.task.read()
            time.sleep(self.interval)

    def getTitle(self):
        return self.title
