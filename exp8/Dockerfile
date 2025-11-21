FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

# git clone https://github.com/docker/getting-started-app.git
# cd getting-started-app
# docker build -t getting-started-app .
# docker run -dp 127.0.0.1:3000:3000 getting-started-app
# docker ps and docker images
# Open http://localhost:3000 in your browser
