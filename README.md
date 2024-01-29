# mqp
MQP - OS Isolation

Steps to run experiment 1, run 1.1 cryptolocker

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