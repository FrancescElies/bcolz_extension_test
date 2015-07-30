import bcolz
from my_extension import carray
import multiprocessing as mp
NUM_PROCESSORS = mp.cpu_count()

class ctable(bcolz.ctable):
    def is_on_disk(self):
        if self.rootdir:
            ret = True        
        else:
            ret = False
        return ret

    def factorize(self):
        
        if self.is_on_disk():
            p = mp.Pool(NUM_PROCESSORS)
            for column in self.cols:
                ca = carray(rootdir=self[column].rootdir)
                ca.factorize()
        else:
            raise Warning
