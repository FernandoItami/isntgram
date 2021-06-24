FROM node:16.3.0-alpine

# make the 'app' folder the current working directory
WORKDIR /app/

COPY package.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

WORKDIR /app/frontend

EXPOSE 8080

CMD ["npm", "run", "serve"]
