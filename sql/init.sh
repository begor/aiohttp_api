psql -U postgres -c   "DROP DATABASE IF EXISTS aiohttp;"
psql -U postgres -c "DROP ROLE IF EXISTS aiohttp;"
psql -U postgres -c  "CREATE USER aiohttp WITH PASSWORD 'qwerty';"
psql -U postgres -c "CREATE DATABASE aiohttp ENCODING 'UTF8';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE aiohttp TO aiohttp;"

cat schema.sql | psql -U postgres -d aiohttp -a
