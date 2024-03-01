# mqp
MQP - OS Isolation

These experiments should be run while [Keylogger](https://github.com/jacobchlebowski/Keylogger) is running for UI data collection

Steps to run experiment 1, run 1.1 synthetic cryptolocker (this should be run within the windows 7 sandbox environment through cuckoo. You may need to install the dependencies first within the sandbox)

1) Install [Python 3.7](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)
- I believe 3.7 and up is fine, but try to stay closer to 3.7
- Ensure environment variables are correct
- check version with 'python --version'

2) Save [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

3) 'python get-pip.py'

4) Install pip dependencies (this might not be all of them so if there's another error when running then just pip install those)
- 'pip install cryptography'
- 'pip install requests'
- 'pip install urllib3==1.26.6'

5) Change the 'directory_to_encrypt' variabe to the desired directory
- ex: C:\Users\Administrator\Desktop\


5) 'python synthetic-cryptolocker.py'



Steps to run experiment 1, run 1.2 synthetic locky

1) Ensure LibreOffice is installed within the windows 7 sandbox environment

2) Open up LibreOffice and go to tools > macros security > and make sure that the security is on *low* so that any macros file can run

3) Run the .docm file through cuckoo


If you followed experiment 1 correctly, all of the benign scenarios in experiment 3 should be easily run with cuckoo