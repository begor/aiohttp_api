sudo -u postgres psql -c "DROP DATABASE IF EXISTS aiohttp;"
sudo -u postgres psql -c "DROP ROLE IF EXISTS aiohttp;"
sudo -u postgres psql -c "CREATE USER aiohttp WITH PASSWORD 'qwerty';"
sudo -u postgres psql -c "CREATE DATABASE aiohttp ENCODING 'UTF8';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE aiohttp TO aiohttp;"

cat schema.sql | sudo -u postgres psql -d aiohttp -a
