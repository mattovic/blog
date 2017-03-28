#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print 'Resource [%s]' % tag

    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '[Exit %s]: Free resource.' % self.tag
        print exc_tb
        print exc_type
        print exc_val
        if exc_tb is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            return False

with DummyResource('Normal'):
    print '[with body] Run without exception!'

#with DummyResource('bug'):
#    print '[with-body] Run with exception.'
#    raise Exception
#    print '[with-body] Run with exception. Failed to finish statement-body!'