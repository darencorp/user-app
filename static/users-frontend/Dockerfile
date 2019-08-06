FROM node:10.16
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install nginx -y
RUN npm i
RUN npm i -g @angular/cli
RUN npm rebuild node-sass
RUN ng build --prod
CMD ["nginx", "-g", "daemon off;"]
