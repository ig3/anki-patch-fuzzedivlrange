# This Anki add-on makes the fuzzed ranges increase monotonically
#
# The original implementation has ranges that go up and down as the
# interval increases. This implementation is simpler and ensures monotonic
# increase of range as interval increases.
#

from anki.schedv2 import Scheduler as SchedulerV2
from typing import List
from math import log

def myFuzzIvlRange(self, ivl: int) -> List[int]:
    if ivl < 2:
        return [1, 1]
    elif ivl < 4:
        return [ivl, ivl+1]
    else:
        fuzz = int(log(ivl, 2)) - 1
        return [ivl-fuzz, ivl+fuzz]

SchedulerV2._fuzzIvlRange = myFuzzIvlRange
