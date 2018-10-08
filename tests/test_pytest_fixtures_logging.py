#TODO remove - it's just for checkig out new features / testing puropses
import pytest
import logging

foo = logging.getLogger('foo')
bar = logging.getLogger('bar')
baz = logging.getLogger('baz')


@pytest.fixture(scope='session')
def session_thing():
    foo.debug('constructing session thing')
    yield
    foo.debug('destroying session thing\n')


@pytest.fixture(scope="function")
def testcase_thing():
    foo.debug('constructing testcase thing')
    yield
    foo.debug('destroying testcase thing\n')


def test_one(session_thing, testcase_thing):
    foo.info('one executes')
    bar.warning('this test does nothing aside from logging')
    baz.info('extra log, rarely read')
    baz.debug("My magic debug log")


def test_two(session_thing, testcase_thing):
    foo.info('two executes')
    bar.warning('neither does this')
    baz.info('extra log, not enabled by default')
    assert 1==0

