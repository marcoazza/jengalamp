git clone https://github.com/marcoazza/jengalamp.git
cd jengalamp
docker build -t jengalamp_led_manager led_manager/
docker build -t jengalamp_tbot tbot/
chmod -R +w .git
cp jenga.yml ..
cd ..
rm -r jengalamp
