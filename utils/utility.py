import os
import sys
import datetime
import subprocess
import time
from database.testdatabase import TestsDatabase
from datetime import datetime
import logging
from common.constant import TEST_DESCRIPTION
__path__ = [os.path.dirname(os.path.abspath(__file__))]
logger = logging.getLogger(__name__)

test = TestsDatabase()


def read_test_case(ch, method, properties, body):
    logger.info('Inside: read_test_case')
    logger.debug('process_readTestcases: parameters - '
                 '{}, {}, {}, {}'.format(ch, method, properties, body))
    msg_dict = body.decode("utf-8")
    if ',' not in msg_dict:
        # time.sleep(10)
        update_pre_complition(msg_dict)
        update_post_compilation(msg_dict)
    else:
        msg_dict = msg_dict.split(',')
        for tc in msg_dict:
            update_pre_complition(tc)
            update_post_compilation(tc)


def update_pre_complition(testcase):
    current_now = datetime.now()
    environment = os.environ['VIRTUAL_ENV']
    print('testcase', testcase)
    fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
    print("'{}' is the TestCase TestRunner is going to run".format(testcase))
    started_at = fmttime
    created_at = time.ctime(os.path.getctime(testcase))

    print("Start time : {}".format(started_at))
    print("Creation time : {}".format(created_at))
    test.add_test_results(testcase, environment, TEST_DESCRIPTION, created_at, started_at,
                          finished_at='N/A', status='In Progress', logs='N/A')


def update_post_compilation(testcase):
    print("'{}' is the TestCase TestRunner is going to run".format(testcase))
    process = subprocess.Popen([sys.executable, testcase], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stdout:
        log = process.communicate()[0]
        log = log.decode("utf-8")
    current_now = datetime.now()
    fmt_time = current_now.strftime("%d/%m/%Y %H:%M:%S")
    finished_time = fmt_time
    completed = "Completed"
    print('finished time is ', finished_time)
    test.update_test_results(testcase, finished_time, completed, log)


def read_test_suite(args):
    print("I am in readCases")


def get_status_all(status):
    status = str(status[0])
    print(status)
    if status == 'all':
        print("I am inside")
        res = test.display()
        print(res)


def get_status_test(id):
    if id:
        print('getonestatus')
        res = test.get_status(id)
        print(res)
