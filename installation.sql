CREATE TABLE "providers" (
    "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
    "title" VARCHAR NOT NULL ,
    "secret_code" VARCHAR NOT NULL  UNIQUE ,
    "image" TEXT NOT NULL
)