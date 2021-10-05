# Fake RDP
Simple program to emulate the handshake of an RDP server with python.

Sends an init packet with the fingerprint emulated from an NLA-enabled RDP server.
This will make it so that clients trying to connect to this server via RDP will be prompted for credentials, then get an error when trying to authenticate.

## Usage
This will run on both python 2 and 3

`./fake_rdp.py`

## Fork
- Added an email alert for each login attempt
- Added wrapper shell script
- Added service file - recommended to run this as a service for continuous support
- Email support requires addition of email.json file. 
- Also recommend putting everything in a common run directory (/usr/local/bin/ would be good or a service account such as 'bot')
