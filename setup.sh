
rm -rf stock-market-prediction
git rm --cached stock-market-prediction
git submodule add https://github.com/intermezzio/stock-market-prediction
mkdir config
echo "API_KEY = 'your-api-key'\nSECRET_KEY = 'your-secret-key'\nIEX_API_TOKEN = 'your-iex-token'" >> config/config.py