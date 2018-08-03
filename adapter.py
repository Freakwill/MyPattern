#-*- coding: utf-8 -*-
# adapter pattern
# 

class Adapter(object):
    '''Adapter class for adapter pattern
    adaptee: adapted object
    adaptedMethods: dict{known method: adapted method}

    known method ---[adapter]---> adapted method [adaptee] 

    run adpater.known_method to call adaptee.adapted_method
    '''
    def __init__(self, adaptee, adaptedMethods={}):
        self.adaptee = adaptee
        self.adaptedMethods = adaptedMethods

    @staticmethod
    def adapt(adaptee, **adaptedMethods):
        return Adapter(adaptee, adaptedMethods)

    def __getattr__(self, method):
        # method calls am of adaptee
        am = self.adaptedMethods[method]
        return getattr(self.adaptee, am)

    def __getitem__(self, method):
        # which method is adapted by 'method'
        return self.adaptedMethods[method]

    def lookup(self, method):
        # which method of adapter adapts 'method'
        for k, v in self.adaptedMethods.items():
            if v == method:
                return k


class Adaptee:
    def __init__(self, v=1):
        self.v=1

    def get(self):
        return self.v

if __name__ == '__main__':
    adaptee = Adaptee(1)
    adapter = Adapter(adaptee, {'exec':'get'})
    print(adapter.exec())
    print(adapter.lookup('get'))