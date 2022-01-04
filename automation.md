# This contains the instructions for using the .service files to automate the running of commands at boot

- Run
```
 sudo -H pip install zmq && sudo -H pip3 install zmq
 ```
- Make the required service files
```
[Unit]
After=network.target
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 

[Install]
WantedBy=multi-user.target
```
- Make these service files using
```
sudo nano /etc/systemd/system/<servicename>.service
```
- Run 
```
sudo systemctl daemon-reload
sudo systemctl enable <servicename>.service
```
- You can use the following commands to check whether the files work as expected or not
```
sudo systemctl start <servicename>.service
sudo systemctl stop <servicename>.service
sudo systemctl restart <servicename>.service
sudo systemctl status <servicename>.service
```
- By default, the files will run by themselves as soon as the Pi is rebooted