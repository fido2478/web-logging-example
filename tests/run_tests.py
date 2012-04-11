#!/usr/bin/env python
import unittest

TEST_MODULES = [
    'tests.test_records',
    'tests.test_visualization',
]

def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    import tornado.testing
    tornado.testing.main()
