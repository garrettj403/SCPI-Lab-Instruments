"""Classes to control Hittite signal generators.

Note:
    
    Keysight has an excellent resource for communicating with instruments over
    SCPI: 'System Power Supply Programming: Using SCPI Commands'.

"""

import os
import socket
import sys
import time


class Hittite:
    """Control a Hittite signal generator.

    Args:
        ip_address (string): IP address of the Hittite signal generator, e.g.,
            ``ip_address='192.168.0.159'``
        port (int, optional, default is 5025): the port set for Ethernet
            communication on the Hittite signal generator

    """

    def __init__(self, ip_address, port=5025):

        # Create socket
        try:
            self._skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('Error creating socket: %s' % e)
            sys.exit(1)

        # Connect to signal generator
        try:
            self._skt.connect((ip_address, port))
        except socket.gaierror as e:
            print('Address-related error connecting to instrument: %s' % s)
            sys.exit(1)
        except socket.error as e:
            print('Error connecting to socket on instrument: %s' % s)
            sys.exit(1)

    def close(self):
        """Close connection to instrument."""

        self._skt.close()
        
    def set_frequency(self, freq, units='GHz'):
        """Set frequency.

        Args:
            freq (float): Frequency to set
            units (string, optional, default is 'GHz'): units for frequency

        """

        msg = 'FREQ {} {}'.format(float(freq), units)
        self._send(msg)

    def get_frequency(self, units='GHz'):
        """Get frequency of signal generator.

        Args:
            units (string, optional, default is 'GHz'): units for the returned
                frequency value

        Returns:
            float: frequency of signal generator

        """

        msg = 'FREQ?'
        self._send(msg)
        frequency = self._receive()

        return freq / _frequency_units(units)

    def set_power(self, power, units='dBm'):
        """Set power.

        Args:
            power (float): Power to set
            units (string, optional, default is 'dBm'): units for power

        """

        msg = 'POW {} {}'.format(float(power), units)
        self._send(msg)

    def get_power(self):
        """Get power from signal generator.

        Returns:
            float: output power from signal generator

        """

        msg = 'POW?'
        self._send(msg)
        power = self._receive()

        return power

    def power_off(self):
        """Turn off output power."""

        msg = 'OUTP 0'
        self._send(msg)

    def power_on(self):
        """Turn on output power."""

        msg = 'OUTP 1'
        self._send(msg)

    # Helper functions -------------------------------------------------------
    
    def _send(self, msg):
        """Send command to instrument.

        Args:
            msg (string): command to send

        """

        msg = msg + '\n'
        self._skt.send(msg.encode('ASCII'))

    def _receive(self):
        """Receive message from instrument.

        Returns:
            string: output from instrument

        """

        msg = self._skt.recv(1024).decode('ASCII')
        return msg.strip()


class SignalGenerator(Hittite):
    """For backwards compatibility with Bob's code...
    
    Bob uses camelCase for all of his method names (see below).

    """

    def setFreq(self, freq):
        """Set frequency in GHz.

        Args:
            freq (float): frequency in GHz

        """

        self.set_frequency(freq, units='GHz')

    def getFreq(self):
        """Get frequency in GHz.

        Returns:
            float: frequency in GHz

        """

        return self.get_frequency(units='GHz')

    def setPower(self, power):
        """Set power in dBm.

        Args:
            power (float): power in dBm

        """

        self.set_power(power, units='dBm')

    def getPower(self):
        """Get power in dBm.

        Returns:
            float: power in dBm

        """

        return self.get_power()

    def powerOff(self):
        """Turn off output power."""

        self.power_off()

    def powerOn(self):
        """Turn on output power."""

        self.power_on()


def _frequency_units(units):
    """Get frequency multiplier."""
    freq_units = {'ghz': 1e9, 'mhz': 1e6, 'khz': 1e3, 'hz': 1}
    try:
        units = freq_units[units.lower()]
    except KeyError as e:
        print('Error: Frequency units must be one of: GHz, MHz, kHz or Hz')
        raise e
    return units


if __name__ == "__main__":

    sg = Hittite('192.168.0.159')
    sg.set_frequency(5, 'GHz')
    sg.set_power(-38, 'dBm')
    sg.power_off()
