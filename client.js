const wppconnect = require('@wppconnect-team/wppconnect');
const shell = require('shelljs');
const cron = require("node-cron");

wppconnect
  .create()
  .then((client) => start(client))
  .catch((erro) => {
    console.log(erro);
  });

function start(client) {
  client.onAnyMessage((message) => {
    if (message.body.startsWith('Programar mensagem') && message.fromMe) {
      client
        .sendText(message.from, 'Welcome Wppconnect')
        .then((result) => {
          var msg = message.body.split(';');
          let hora=msg.pop()
          let dia=msg.pop()
          diapath=dia.replaceAll("/",";")
          let text=msg.pop()
          let telnumber=msg.pop();
          const fs = require('fs');
          let path=diapath+hora;
          let arq= dia+"|"+hora+"|"+telnumber+"|"+text+"\n"
            fs.appendFile("envio.txt",arq, (err) => {
            if (err) {
                console.log(err);
            } else {
                console.log('Arquivo salvo com sucesso!');
            }
            console.log(telnumber)
          });
          fs.appendFile("programa.txt",arq, (err) => {
            if (err) {
                console.log(err);
            } else {
                console.log('Arquivo salvo com sucesso!');
            }
            console.log(telnumber)
          });
        })
        .catch((erro) => {
          console.error('Error when sending: ', erro); //return object error
        });
    }
  });
}