wget https://github.com/marcoazza/jengalamp/archive/v$1.tar.gz
tar xvzf v$1.tar.gz
cd jengalamp-$1
docker build -t jengalamp_led_manager led_manager/
docker build -t jengalamp_tbot tbot/
chmod -R +w .git
cp jenga.yml ..
cd ..
rm -r jengalamp-$1
