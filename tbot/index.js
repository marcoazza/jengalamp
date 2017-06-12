const TelegramBot = require('node-telegram-bot-api');
const io = require('socket.io-client');
const led_client = io(`${process.env.LEDHOST}`);
const token = process.env.TOKEN;
const id = Number(process.env.ID);
const colors = {
    red: [255, 0, 0],
    violet: [148, 0, 211],
    indigo: [75, 0, 130],
    orange: [255, 69, 0],
    yellow: [255, 255, 0],
    blue: [0, 0, 255],
    white: [255, 255, 255],
}

const rgbColorReg = new RegExp(['^([Bb]link\\s+)?(([a-zA-Z]+)|',
    '(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\s+',
    '(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\s+',
    '(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]))$'].join(''));

if(!token){
    throw new Error('Bot TOKEN has to be specified as env variable.');
}

const bot = new TelegramBot(token, { polling: true });

function getDefault(color){
    let col = colors[color] || color.split(" ");
    if(col.length === 3){
        return col;
    }
    return undefined;
}

bot.onText(rgbColorReg, (msg, match) => {
    if (msg.from.id === id) {
        const style = match[1] || 'simple';
        const color = getDefault(match[2].toLowerCase());
        if(color){
            switch(style.toLowerCase().trim()){
                case 'simple':
                case 'blink':
                    console.log(`Style: ${style} with color: ${color}`);
                    led_client.emit('change', {color: color, style: style.toLowerCase().trim()});
                    break;
            }
        }
    }
});

bot.onText(/^[Rr]ainbow$/, (msg, match) => {
    if (msg.from.id === id) {
        const style = 'rainbow';
        const color = [0, 0, 0];
        led_client.emit('change', {color: color, style: style.trim()});
    }
});

bot.onText(/^([Oo]n|[Oo]ff)$/, (msg, match) => {
    if (msg.from.id === id) {
        const command = match[1].toLowerCase();
        led_client.emit('command', {command:command});
    }
});

bot.on('polling_error', (error) => {
  console.error(`Polling: ${error}`);
});
