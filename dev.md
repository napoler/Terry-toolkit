



## 正常执行
docker run -d --name toolkit -v /home/terry/pan/github/Terry-toolkit:/myapp -p 5005:5000 -it napoler/ubuntu-python-docker  bash



 


docker start toolkit

## 进入容器
docker exec -t -i toolkit  bash

## 安装依赖
pip3 install -r requirements.txt