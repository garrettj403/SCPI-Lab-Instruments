SCPI Lab Instruments
====================

Communicate with various instruments in the lab over Ethernet+SCPI.

Installation
------------

To install via pip:

```bash
python3 -m pip install git+https://github.com/garrettj403/SCPI-Lab-Instruments.git
```

Also, install the ``vxi11`` library:

```bash
python3 -m pip install git+https://github.com/alexforencich/python-vxi11.git
```

Example
-------

```python
from labinstrument import *

# Connect to Hittite signal generator
sg = Hittite('192.168.0.159')
sg.set_power(-40, 'dBm')
sg.set_frequency(5, 'GHz')
sg.power_on()

# Connect to Keithley power supply
ps = Keithley2280('192.168.0.117')
ps.reset()
ps.set_voltage(2)
ps.set_current(0.1)
ps.output_on()
```
