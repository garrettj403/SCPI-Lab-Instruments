from setuptools import setup, find_packages

setup(
    name = "LabInstruments",
    version = "0.0.1",
    author = "John Garrett",
    author_email = "garrettj403@gmail.com",
    description = ("Communicate over Ethernet + SCPI with lab instruments (signal generators, etc.)"),
    license = "MIT",
    keywords = "SCPI, Ethernet, Lab equipment, Signal generators",
    url = "https://github.com/garrettj403/SCPI-Lab-Instruments",
    packages=find_packages(),
    install_requires=[
        'sockets',
    ],
    # long_description="Communicate over Ethernet+SCPI with lab instruments (signal generators, etc.)",
    # classifiers=[
    #     "Development Status :: 5 - Production/Stable",
    #     "Intended Audience :: Science/Research",
    #     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    #     "Natural Language :: English",
    #     "Programming Language :: Python :: 3.5",
    #     "Programming Language :: Python :: 3.6",
    #     "Programming Language :: Python :: 3.7",
    #     "Topic :: Scientific/Engineering",
    # ],
)
