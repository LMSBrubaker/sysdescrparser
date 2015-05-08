# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_serveriron."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class BrocadeNetworkOS(SysDescr):

    """Class BrocadeNetworkOS.

    SNMP sysDescr for Brocade NetworkOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'brocade'
        os = 'nos'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'^Brocade (.*) Switch.$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            model = res.group(1)
            return self._store(vendor=vendor,
                               os=os,
                               model=model,
                               version=version)
        return False
