from python:3.7-slim
#run apt update && apt install -y build-essential
run pip3 install gunicorn falcon pymongo
workdir /opt/torque
copy ./torque-server.py /opt/torque
copy ./torquedb.py /opt/torque
expose 30000/tcp
#entrypoint uwsgi -http :30000 --wsgi-file torque-server
entrypoint gunicorn -b 0.0.0.0:30000 torque-server:application
