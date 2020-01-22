"""Classes to control the Micro Lambda Wireless, Inc. YIG filter.

Note:

    It communicates over Ethernet + Telnet

"""

import telnetlib


FREQ_UNIT = {'hz': 1e-6, 'khz': 1e-3, 'mhz': 1, 'ghz': 1e3}


class YigFilter:
    """Control the YIG filter from Micro Lambda Wireless (MLBF series).

    Note: 

        Uses Telnet.
        
        This has only been tested on an MLBF series bench test filter.

    Args:
        ip_address (string): IP address of the Yig filter, e.g.,
            ``ip_address='192.168.0.159'``

    """

    def __init__(self, ip_address):

        self._tn = telnetlib.Telnet(ip_address)

    def set_frequency(self, freq, units='GHz'):
        """Set frequency.

        Args:
            freq (float): Frequency to set
            units (string, optional, default is 'GHz'): units for frequency

        """

        freq = freq * FREQ_UNIT[units.lower()]
        msg = 'F{:.5f}'.format(float(freq))

        self._send(msg)

    def _write(self, msg):
        """Write via Telnet."""

        self._tn.write(msg + "\r\n".encode('ASCII'))
