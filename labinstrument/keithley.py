"""Classes to control Keithley power supplies.

Note:
    
    Keysight has an excellent resource for communicating with instruments over
    SCPI: 'System Power Supply Programming: Using SCPI Commands'.

    Keithley SCPI commands can be found here:

        https://doc.xdevs.com/doc/Keithley/2280/077085501_2280_Reference_Manual.pdf

"""

import vxi11


class Keithley2280:
    """Control a Keithley 2280 power supply.

    Args:
        ip_address (string): IP address of the power supply, e.g.,
            ``'192.168.0.117'``

    """

    def __init__(self, ip_address):

        self.inst = vxi11.Instrument(ip_address)

    def close(self):
        """Close connection to instrument."""

        self.inst.close()

    def get_id(self):
        """Get identity of signal generator."""

        return self.inst.ask('*IDN?')

    def reset(self):
        """Reset instrument."""

        self.inst.write("*RST")

    def set_voltage(self, voltage):
        """Set voltage.

        Args:
            voltage (float): voltage in units 'V'

        """

        msg = ':VOLT {}'.format(float(voltage))
        self.write(msg)

    def get_voltage(self):
        """Get voltage.

        Returns:
            float: voltage in units 'V'

        """

        self.inst.write(":FORM:ELEM \"READ\"")
        return self.inst.ask(':MEAS:VOLT?')

    def set_current(self, current):
        """Set current.

        Args:
            current (float): current in units 'A'

        """

        msg = ':CURR {}'.format(float(current))
        self.write(msg)

    def get_current(self):
        """Get current.

        Returns:
            float: current in units 'A'

        """

        self.inst.write(":FORM:ELEM \"READ\"")
        return self.inst.ask(':MEAS:CURR?')

    def power_off(self):
        """Turn off output power."""

        msg = ':OUTP ON'
        self.write(msg)

    def output_off(self):
        """Turn off output poewr."""

        self.power_off()

    def power_on(self):
        """Turn on output power."""

        msg = ':OUTP OFF'
        self.write(msg)

    def output_on(self):
        """Turn on output power."""

        self.power_on()


# Main -----------------------------------------------------------------------

if __name__ == "__main__":

    ps = Keithley2280('192.168.0.117')
    ps.reset()
    print(ps.get_id())

    ps.set_voltage(2)
    ps.set_current(0.1)
    ps.output_on()



