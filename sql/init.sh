psql -c "DROP DATABASE IF EXISTS aiohttp;"
psql -c "DROP ROLE IF EXISTS aiohttp;"
psql -c "CREATE USER aiohttp WITH PASSWORD 'qwerty';"
psql -c "CREATE DATABASE aiohttp ENCODING 'UTF8';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE aiohttp TO aiohttp;"

cat schema.sql | psql -d aiohttp -a
