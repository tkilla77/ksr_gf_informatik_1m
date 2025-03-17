#!/usr/bin/python
# -*- coding: utf8 -*-
import sys, time
if sys.version_info.major == 3:
    from collections import UserList
else:
    from UserList import UserList

class SlowList(UserList):
    """A list that slows down each access to an element."""
    def __init__(self, lst, delay_ms=1):
        self._delay = delay_ms
        super(SlowList, self).__init__(lst)
    def __getitem__(self, item):
        time.sleep(self._delay / 1000.0)
        return super(SlowList, self).__getitem__(item)
