FROM ind3x/rpi-alpine-node
RUN mkdir /bot
WORKDIR /bot
COPY package.json /bot/
RUN npm install
COPY index.js /bot/
CMD ["node", "."]
