# Create prometheus-grafana stack for monitoring
*This project is created to monitor services in prometheus and grafana stack with dockercompose.*

## Requirement:
*If you didn't seperate dockervol when you installed OS, it is highly recommended to create a separeted partition for /var/lib/docker to have better storage management.*
*If we assume that the name of the disk assigned to this partition is sdb, we will proceed as follows:*
```
pvcreate /dev/sdb
vgcreate dockerSpaceVG /dev/sdb
lvcreate -n dockervol -l 100%FREE dockerSpaceVG
mkdir /tmp/docker && mv /var/lib/docker/* /tmp/docker/
mkfs -t ext4 /dev/mapper/dockerSpaceVG-dockervol
mount /dev/mapper/dockerSpaceVG-dockervol /var/lib/docker
mv /tmp/docker/* /var/lib/docker
```
*after this operation you Need to configure fstab file to mount dockervol after reboot:*
```
echo "dev/mapper/dockerSpaceVG-dockervol /var/lib/docker/ ext4 defaults 0 1" >> /etc/fstab
```
## Installation:
*If you wish to run the prometheus TSDB with grafana dashboards, You can easily set suitable variables in .env files and run compose.yml with this command:*
```
cp prometheus.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable prometheus
systemctl start prometheus
```
## Telegram Proxy
I assume that we don't have any internet access through the host, so my telegram proxy component uses an http proxy from the internal network that has free internet access.

## Notices

*1- It is important to know that in prometheus configuration (prometheus.yml) the job name of node discovery has been created for file service discovery. You can use targets.yml to find new nodes from prometheus!*
*2- Grafana provisioning is enabled in this project under grafana directory. If you like to transport your machine to another machine you can easily copy grafana contents and it will learn your prometheus and its dashboard from this path.*
*3- If you wish you add a new grafana dashboard, you can add it into dashboards (similar to NodeExporterFull.json) folder and it will be learned by grafana.*
*4- Note that port 8080 on the Telegram proxy container is currently open to the public and this could pose a security risk. To prevent this issue, you need to configure the host's firewall properly.*
