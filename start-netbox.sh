git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker
tee docker-compose.override.yml <<EOF
version: '3.7'
services:
  netbox:
    ports:
      - 8000:8080
  postgres:
    ports:
      - 5432:5432
  redis:
    ports:
      - 6379:6379
EOF
docker-compose pull
docker-compose up
