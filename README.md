# create prometheus-grafana stack for monitoring
*This project is created to monitor services in prometheus and grafana stack.*

## Requirement
*It is highly recommended to create a separeted partition for /var/lib/docker for better storage management.*
*If we assume that the name of the disk assigned to this partition is sdb, we will proceed as follows:*
```
pvcreate /dev/sdb
vgcreate dockerSpaceVG /dev/sdb
lvcreate -n dockervol -l 100%FREE dockerSpaceVG
```

```
docker compose up -d
```

*If you wish to run the prometheus TSDB with grafana dashboards, You can easily run compose.yml with this command:*

```
docker compose up -d
```
*it is important to know that in prometheus configuration (prometheus.yml) the job name of node discovery has been created for file service discovery. You can use targets.yml to find new nodes from prometheus!*
