#!/bin/bash

echo "============================="
echo "MySQL Server Resource Monitor"
echo "Time: $(date)"
echo "============================="

echo
echo "CPU Usage"
docker stats mysql --no-stream --format "CPU: {{.CPUPerc}}"

echo
echo "Memory Usage"
docker stats mysql --no-stream --format "Memory: {{.MemUsage}}"

echo
echo "Disk Usage"

MSYS_NO_PATHCONV=1 docker exec mysql df -h /var/lib/mysql


echo
echo "Database Size"

docker exec mysql mysql -uroot -prootpass -e "
SELECT
table_schema AS DatabaseName,
ROUND(SUM(data_length+index_length)/1024/1024,2) AS Size_MB
FROM information_schema.tables
GROUP BY table_schema;
"