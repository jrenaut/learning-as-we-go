FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY vufjuoz^xk_#zm^3wm46t$ev&vtwi_vk$@$s&a@3-z&5*+57yh
ENV SERVER_ENVIRONMENT DEV
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
