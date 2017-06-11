FROM ind3x/rpi-alpine-node
RUN mkdir /bot
WORKDIR /bot
COPY package.json index.js /bot/
RUN npm install
CMD ["node", "."]
