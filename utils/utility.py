import os
import datetime
import subprocess
import time
from database.mysql_connector import TestDatabase
from datetime import datetime
import logging
from common.constant import TEST_DESCRIPTION, TEST_FILES_PATH
from common.config import BASE_DIR

__path__ = [os.path.dirname(os.path.abspath(__file__))]
logger = logging.getLogger(__name__)

test = TestDatabase()


def read_test_case(ch, method, properties, body):
    abs_path = os.path.join(BASE_DIR, TEST_FILES_PATH)
    print(abs_path)
    logger.info('Inside: read_test_case')
    logger.debug('process_readTestcases: parameters - '
                 '{}, {}, {}, {}'.format(ch, method, properties, body))
    msg_dict = body.decode("utf-8")
    logger.info('msg_dict', msg_dict)
    file_extension = os.path.splitext(msg_dict)
    logger.info('type', file_extension)

    # if msg_dict is single file

    if ',' not in msg_dict:
        filename, file_extension = os.path.splitext(msg_dict)
        if file_extension == '.py':
            # time.sleep(10)
            update_pre_complition(msg_dict)
            update_post_compilation_python_test(msg_dict)
        elif file_extension == '.bats':
            update_pre_complition(msg_dict)
            update_post_compilation_bash_script(msg_dict)

    else:
        msg_dict = msg_dict.split(',')
        for tc in msg_dict:
            update_pre_complition(tc)
            update_post_compilation_bash_script(tc)


def update_pre_complition(testcase):
    current_now = datetime.now()
    environment = os.environ['VIRTUAL_ENV']
    fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
    logger.info("'{}' is the TestCase TestRunner is going to run".format(testcase))
    started_at = fmttime
    created_at = time.ctime(os.path.getctime(testcase))

    logger.info("Start time : {}".format(started_at))
    logger.info("Creation time : {}".format(created_at))
    test.insert_into_table(testcase, environment, TEST_DESCRIPTION, created_at, started_at,
                           finished_at='N/A', status='In Progress', logs='N/A')


def update_post_compilation_python_test(testcase):
    logger.info("'{}' is the TestCase TestRunner is going to run".format(testcase))
    cmd = "nosetests " + " -v " + testcase
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    # print('result =', process.stdout)
    # print('result2', process.communicate()[1])
    if process.stdout:
        log = process.communicate()[1]
        # log = log.decode("utf-8")
        endlist = log.partition('\n')[-1]

    current_now = datetime.now()
    fmt_time = current_now.strftime("%d/%m/%Y %H:%M:%S")
    finished_time = fmt_time
    completed = "Completed"
    logger.info('finished time is ', finished_time)
    test.update_into_table(testcase, finished_time, completed, log)


def update_post_compilation_bash_script(testcase):
    logger.info("'{}' is the TestCase TestRunner is going to run".format(testcase))
    cmd = "bats " + " --tap " + testcase
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    # print('communicate', process.stdout.read())
    log = process.stdout.read()
    current_now = datetime.now()
    fmt_time = current_now.strftime("%d/%m/%Y %H:%M:%S")
    finished_time = fmt_time
    completed = "Completed"
    logger.info('finished time is ', finished_time)
    test.update_into_table(testcase, finished_time, completed, log)


def read_test_suite(args):
    logger.info("I am in readCases")


def get_status_all(status):
    status = str(status[0])
    logger.info(status)
    if status == 'all':
        res = test.display()
        print(res)


def get_status_from_id(id):
    if id:
        res = test.status_from_id(id)
        print(res)
    else:
        logger.error('Enter the test case id to check the status')


def load_test_from_test_case(testCaseClass):
    # sortTestMethodsUsing = Callable[[str, str], bool]
    def filter_test_methods(attrname):
        testMethodPrefix = 'test'
        return attrname.startswith(testMethodPrefix) \
               and callable(getattr(testCaseClass, attrname))

    test_case_names = list(filter(filter_test_methods, dir(testCaseClass)))
    logger.info("Test case names: {}".format(test_case_names))
    return test_case_names


def run_test_by_one(id):
    cmd = "nosetests" + " -v --with-id " + id
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if process.stdout:
        log = process.communicate()[1]
        # log = log.decode("utf-8")
        endlist = log.partition('\n')[-1]
#
# file = os.path.join('test_python_scripts.py')
# print(file)
# res = read_test_case(testcase='test_python_scripts.py')
# print(res)
