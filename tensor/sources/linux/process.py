from zope.interface import implements

from twisted.internet import defer, utils

from tensor.interfaces import ITensorSource
from tensor.objects import Source

class ProcessCount(Source):
    """Returns the ps count on the system

    **Metrics:**

    :(service name): Number of processes
    """
    implements(ITensorSource)

    @defer.inlineCallbacks
    def get(self):
        out, err, code = yield utils.getProcessOutputAndValue('/bin/ps',
            args=('-e',))

        count = len(out.strip('\n').split('\n'))

        defer.returnValue(
            self.createEvent('ok', 'Process count %s' % (count), count)
        )
