POSTGRES DB:

docker run -itd -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=16zomole -e POSTGRES_DB=vpn-dion -p 45046:5432 postgres:13.3


docker build -f docker/local/frontend/Dockerfile -t vpn-front ./frontend/ --network="host" 
docker run -t vpn-front



Подготовка VPN сервера:

Установить gunicorn, virtualenv, python3-pip(pip3), nginx:
Установить wireguard через скрипт wireguard-install.sh
Создать виртуальное окружение
Установить пакеты в requirements.txt
Установить sudo apt-get install python3-tk
Создать vpn.service в /etc/systemd/system/
[Unit]
Description=Vpn rest server
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/vpn_server/vpn_server_rest_api/
Environment="PATH=/root/vpn_server/vpn_server_rest_api/venv/bin:/usr/bin/"
ExecStart=/root/vpn_server/vpn_server_rest_api/venv/bin/gunicorn \
    --workers 3 --bind 0.0.0.0:5000 \
     --chdir /root/vpn_server/vpn_server_rest_api/  -m 007 wsgi:app

[Install]
WantedBy=multi-user.target

Выполнить:
systemctl start vpn
journalctl -i vpn

Изменить конфигурацию nginx default
server {
    listen 55055 default_server;
    listen [::]:55055 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        proxy_pass http://localhost:5000/;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwared-For $proxy_add_x_forwarded_for;
    }
}


Выполнить:
systemctl restart nginx

Выполнить и получить ответ в видет JSON: {cpu: ..., networkUpload: ..., и т.д.}:
curl -X GET http://localhost:5000/collect-statistics
curl -X GET http://<PUBLIC_HTTP_IP>:5000/collect-statistics



Дополнительная информация:

1. Подключение к PG admin:

psql -U userName


2. Не забыть выбрать дефолтный протокол и страну.