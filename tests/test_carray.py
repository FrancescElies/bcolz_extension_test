import tempfile
import numpy as np
import bcolz
from bcolz.tests.common import MayBeDiskTest
import my_extension
from my_extension import CarrayOnSteroids, ctable

import sys
if sys.version[0:3] >= '3.3':
    from unittest.mock import Mock, patch
else:
    from mock import Mock, patch


class HelperCarray(MayBeDiskTest):

    def test_01(self):
        a = CarrayOnSteroids([1, 2, 3, 4])
        a.factorize()


class TestCarrayMemory(HelperCarray):
    disk = False


class TestCarrayDisk(HelperCarray):
    disk = True


class HelperCtable(MayBeDiskTest):
    pass


class TestCtableDisk(HelperCtable):
    disk = True

    def test_01(self):
        a = ctable(np.array([(1, 2.0), (3, 4.0)], dtype="i4,f8"), 
                rootdir=self.rootdir)
        
        a.factorize()
