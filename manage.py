#!/usr/bin/env python3
# importing the required modules
import os

__path__ = [os.path.dirname(os.path.abspath(__file__))]
from database.mysql_connector import TestDatabase as database
from utils import utility
import argparse
from rabbitmq import producer

TEST_DESCRIPTION = 'This Test is to validate functionality'


class Driver:
    def __init__(self):
        self.test = database()

    def main(self):
        # create parser object
        parser = argparse.ArgumentParser(description="A Test Runner!")

        # defining arguments for parser object
        parser.add_argument("-tc", "--testcase", type=str,
                            metavar="Test Case Names", default=None,
                            help="Specify the Testcase which needs to be executed.")
        #
        # parser.add_argument("-ts", "--testsuite", type=str, nargs=1,
        #                     metavar="path of the TestSuite", default=None,
        #                     help="Accepts the folder which has all the testcases")

        parser.add_argument("-a", "--getstatusall", type=str, nargs=1,
                            metavar="Status of the TestCases", default=None,
                            help="Status of all TestCases.")

        parser.add_argument("-s", "--status", type=str, nargs=1,
                            metavar="Status of the testCases using id", default=None,
                            help="Status of the testCases using id.")

        # parse the arguments from standard input
        args = parser.parse_args()

        # calling functions depending on type of argument
        if args.testcase is not None:
            producer.publish_test(args.testcase)
        elif args.getstatusall is not None:
            utility.get_status_all(args.getstatusall)
        elif args.status is not None:
            utility.get_status_from_id(args.status)


if __name__ == '__main__':
    obj = Driver()
    obj.main()
