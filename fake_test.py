"""
Nosetest that will produce a nice pattern
To be used as test data input to test-result-ingester
"""

import os
import logging
import random
import unittest

log = logging.getLogger(__name__)


def get_build_number():
    value = int(os.environ.get("BUILD_NUMBER", -1))
    if value == -1:
        raise Exception("Failed to read build number from environment variable BUILD_NUMBER")
    return value


def is_even():
    value = get_build_number()
    even = (value % 2) == 0
    return even


def test_always_OK():
    pass


def test_always_FAIL():
    assert False


def test_always_ERROR():
    raise Exception()


def test_even_OK_odd_FAIL():
    if is_even():
        pass
    else:
        assert False


def test_even_FAIL_odd_ERROR():
    if is_even():
        assert False
    else:
        raise Exception()


def test_even_ERROR_odd_OK():
    if is_even():
        raise Exception()
    else:
        pass


def test_random_OK_FAIL_10_percent():
    if random.random() < 0.1:
        assert False
    else:
        assert True


def test_random_OK_FAIL_30_percent():
    if random.random() < 0.3:
        assert False
    else:
        assert True

def test_random_OK_FAIL_70_percent():
    if random.random() < 0.7:
        assert False
    else:
        assert True


def test_random_OK_ERROR_30_percent():
    random_number = random.random()
    if random_number < 0.3:
        # If this message is either in the exception or printed to stdout
        # it will end up in the "reason" field.
        # That will mess up term queries on that field, so for
        # now I just silenced it.
        # msg = "Failed since %s is less than 0.3" % random_number
        # print msg
        raise Exception("Value is below threshold")

@unittest.skip("intentionally skipped")
def test_always_SKIP():
    pass



def test_missing_then_ok_after_build_number():
    #
    # So, the idea here is to make a generator that creates tests
    # up to the current build number.
    #
    # That way we can get missing results in our example data.
    #
    buildnumber = get_build_number()
    for i in range(buildnumber):
        # We need to trick nosetest into setting a sane name of
        # the function we yield, so that the output of nose and
        # the XML report contains this name instead of the
        # real function name
        name = "test_missing_then_ok_after_%s" % i
        # This is for the XML output
        test_missing_then_ok_after_build_number.__name__ = name
        yield function_to_yield_ok_result

def function_to_yield_ok_result():
    # This is just a helper function to be yielded above
    pass
