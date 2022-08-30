docker build -f docker/local/frontend/Dockerfile -t vpn-front ./frontend/ --network="host" 
docker run -t vpn-front