import HTMLTestRunner
import unittest

from tourscool_case import test_case
from reuse_method import now_time

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([test_case.ToursCoolCase('test_login'), test_case.ToursCoolCase('test_ll_search'),test_case.ToursCoolCase('test_create_order')])
    with open('../tourscool_report/%s.html' % now_time.get_times(), 'wb+') as f:
        run = HTMLTestRunner.HTMLTestRunner(stream=f,title='tourscool',description='tourscool app report',verbosity=2)
        run.run(suite)