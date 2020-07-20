# Nose tests

# With correct project implementation the outputs would be isoformatted
# With correct implementation the acp_times functions would return

import arrow
from acp_times import *

def test_times_zero():
    assert(acp_times.open_time(1000, 0, 00H:00M), 00H:00M)
    assert(acp_times.close_time(1000, 0, 00H:00M), 01H:00M)

def test_times_200():
    assert(acp_times.open_time(1000, 200, 00H:00M), 05H:53M)
    assert(acp_times.close_time(1000, 200, 00H:00M), 13H:20M)

def test_times_300():
    assert(acp_times.open_time(1000, 300, 00H:00M), 09H:00M)
    assert(acp_times.close_time(1000, 300, 00H:00M), 20H:00M)

def test_times_400():
    assert(acp_times.open_time(1000, 400, 00H:00M), 12H:08M)
    assert(acp_times.close_time(1000, 400, 00H:00M), 2H:40M) # Next day

def test_times_600():
    assert(acp_times.open_time(1000, 600, 00H:00M), 18H:48M)
    assert(acp_times.close_time(1000, 600, 00H:00M), 16H:00M) # Next day

def test_times_1000():
    assert(acp_times.open_time(1000, 1000, 00H:00M), 09H:05M) # Next day
    assert(acp_times.close_time(1000, 1000, 00H:00M), 03H:00M) # Day after next

def test_all():
    test_times_zero()
    test_times_200()
    test_times_300()
    test_times_400()
    test_times_600()
    test_times_1000()

test_all()
