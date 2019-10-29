# flask-demo

Description: 
This is a simple project to specifically test the interaction between Python 3 Flask, uWSGI & Nginx while deploying with docker-compose.

## Deploy

```bash
docker-compose -f docker-compose.yml up -d
```

## Test

```bash
curl http://localhost:8500
```
