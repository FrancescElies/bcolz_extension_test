import bcolz
from my_extension import CarrayOnSteroids
import multiprocessing as mp
NUM_PROCESSORS = mp.cpu_count()


class ctable(bcolz.ctable):

    def is_on_disk(self):
        if self.rootdir:
            ret = True
        else:
            ret = False
        return ret

    def factorize_log_result(self, result):
        result_list.append(result)

    def factorize(self):
        ca_factorize = getattr(CarrayOnSteroids, 'factorize')
        result_list = []
        
        if self.is_on_disk():
            p = mp.Pool(NUM_PROCESSORS)
            for column in self.cols:
                ca = CarrayOnSteroids(rootdir=self[column].rootdir)
                p.apply_async(ca_factorize, (ca, ), {'id': column},
                        callback=self.factorize_log_result)
            p.close()
            p.join()
        else:
            raise Warning
       
        return result_list
