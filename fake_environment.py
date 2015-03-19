
def _(msg):
    return msg

class log(object):
    def error(self, *msg):
        print ("dneutronERROR ", msg[0] % tuple(msg[1:]))
    def debug(self, *msg):
        print ("dneutronDEBUG ", msg[0] % tuple(msg[1:]))
    def info(self, *msg):
        print ("dneutronINFO ", msg[0] % tuple(msg[1:]))

