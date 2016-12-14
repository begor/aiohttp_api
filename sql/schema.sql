SET ROLE 'aiohttp';


BEGIN;

CREATE TABLE notes ("id" serial NOT NULL PRIMARY KEY, "created_at" timestamp NOT NULL, "updated_at" timestamp NOT NULL, "content" TEXT NOT NULL);

COMMIT;
