# coding=utf8

class Sample:
        def __enter__(self):
                print "In __enter__()"
                return self

        #可以通过__exit__的返回值来指示with-block部分发生的异常是否需要reraise，如果返回false，则会reraise with block异常，如果返回ture，则就像什么也没发生。
        def __exit__(self, type, value, trace):
                print "In __exit__()"
                #可在__exit__中进行异常处理
                print "type:", type
                print "value:", value
                print "trace:", trace

                return isinstance(value, ZeroDivisionError) #跳过除数为0异常

        def divide(self):
                s = 1 / 0
                s += 1


def get_sample():
        return Sample()


try:
        # sample是get_sample()调用__enter__的返回值
        with Sample() as sample:
                print "sample:", sample
                sample.divide()
except ZeroDivisionError:
        print 'divide zero'
