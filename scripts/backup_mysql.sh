#!/bin/bash

BACKUP_DIR="/backups"

mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

docker exec mysql \
mysqldump \
-u root \
-prootpass \
source_db \
> "$BACKUP_DIR/source_db_$TIMESTAMP.sql"

echo "Backup created:"
echo "$BACKUP_DIR/source_db_$TIMESTAMP.sql"
