import functools
import subprocess
from test_files.testcase import SimpleTest
from collections import OrderedDict


def loadTestsFromTestCase(testCaseClass):
    # sortTestMethodsUsing = Callable[[str, str], bool]
    def filter_test_methods(attrname):
        testMethodPrefix = 'test'
        return attrname.startswith(testMethodPrefix) \
               and callable(getattr(testCaseClass, attrname))

    test_case_names = list(filter(filter_test_methods, dir(testCaseClass)))
    print("Test case names: {}".format(test_case_names))
    return test_case_names

def run_test_by_one(id):
    cmd = "nosetests" + " -v --with-id " + id
    print(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if process.stdout:
        log = process.communicate()[1]
        # log = log.decode("utf-8")
        print('loging', log)
        endlist = log.partition('\n')[-1]
        print('endlist', endlist)

def loadTargets(self, targets, file_pattern='test*.py'):
    # If a string was passed in, put it into a list.
    if type(targets) != list:
        targets = [targets]

    # Make sure there are no duplicate entries, preserving order
    target_dict = OrderedDict()
    for target in targets:
        target_dict[target] = True
    targets = target_dict.keys()

    suites = []
    for target in targets:
        suite = self.loadTarget(target, file_pattern)
        if not suite:
            print("Found 0 tests for target '{}'".format(target))
            continue
        suites.append(suite)
        num_tests = suite.countTestCases()
        print("Found {} test{} for target '{}'".format(
            num_tests, '' if (num_tests == 1) else 's', target))

    print(suites) if suites else None
res = loadTestsFromTestCase(SimpleTest)
n = len(res)
print(n)
for i in range(n):

    result = run_test_by_one(i)
    print(result)