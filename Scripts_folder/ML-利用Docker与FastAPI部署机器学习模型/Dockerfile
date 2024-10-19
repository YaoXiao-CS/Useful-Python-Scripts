# 创建dockerfile.

# 使用Python 3.9作为基础镜像.
FROM python:3.9-slim

# 创建并设置一个工作目录.
RUN mkdir -p /Code

WORKDIR /Code

# 将项目requirements.txt复制到工作目录.
COPY requirements.txt /Code/requirements.txt

# 安装工具包.
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade -r /Code/requirements.txt

# 复制app目录到工作目录.
COPY ./app /Code/app

# 复制模型文件路径到工作目录.
COPY ./model /Code/model

# 暴露80端口.
EXPOSE 80

# 启动命令.
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]