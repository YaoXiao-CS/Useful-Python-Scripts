FROM python:3.9-slim


RUN mkdir -p /Code

COPY ./app /Code/app

COPY ./model /Code/model

WORKDIR /Code

COPY UseDockerAndFastAPIDeployML.txt /Code/UseDockerAndFastAPIDeployML.txt


RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade -r /Code/UseDockerAndFastAPIDeployML.txt



EXPOSE 80

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]