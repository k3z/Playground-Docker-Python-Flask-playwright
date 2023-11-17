FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=api:create_app()
ENV FLASK_ENV=development

RUN apt-get -y update \
    && apt-get install -y \
      libnss3\
      libasound2\
      libgbm-dev\
    && apt-get -y clean

RUN pip install playwright
RUN playwright install-deps
RUN playwright install


RUN mkdir /api
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /api/

CMD ["flask", "run", "--host=0.0.0.0"]
