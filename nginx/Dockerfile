FROM nginx:1.19-alpine
RUN echo 'server_tokens off;' > /etc/nginx/conf.d/server_tokens.conf

WORKDIR /etc/nginx

RUN mkdir -p /etc/nginx/templates/
COPY ./templates /etc/nginx/templates

RUN mkdir -p /static/
COPY ./static /static

ADD start.sh start.sh

# ENTRYPOINT ['/etc/nginx/start.sh']
CMD ./start.sh && nginx -g 'daemon off;'
