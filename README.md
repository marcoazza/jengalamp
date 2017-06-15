# jengalamp

* Create Service
     - sudo vim /etc/systemd/system/jenga.service
     - put the following content into the jenga.service file:

[Unit]
Description=Jenga Lamp Container
Requires=docker.service
After=docker.service

[Service]
ExecStart=/usr/local/bin/docker-compose -f /home/pi/jenga.yml up -d
ExecStop=/usr/local/bin/docker-compose -f /home/pi/jenga.yml down

[Install]
WantedBy=default.target

