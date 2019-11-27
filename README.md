SCPI Lab Instruments
====================

Communicate with various instruments in the lab over Ethernet+SCPI.

Installation
------------

To install via pip:

```bash
python3 -m pip install git+https://github.com/garrettj403/SCPI-Lab-Instruments.git
```

Example
-------

```python
from labinstrument import *

sg = Hittite('192.168.0.159')
sg.set_power(-40, 'dBm')
sg.set_frequency(5, 'GHz')
sg.power_on()
```
