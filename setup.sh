
rm -rf stock-market-prediction
git rm --cached stock-market-prediction
rm .gitmodules
touch .gitmodules
git config -f .git/config --remove-section submodule.stock-market-prediction
git submodule add https://github.com/intermezzio/stock-market-prediction
cd ./stock-market-prediction
sh setup.sh
cd ..
mkdir config
printf "APCA_API_KEY_ID = 'your-api-key'\nAPCA_API_SECRET_KEY = 'your-secret-key'\nALPHAVANTAGE_API_KEY = 'your-alphavantage-token'\n\nAPCA_API_BASE_URL = 'https://paper-api.alpaca.markets'" >> config/config.py
