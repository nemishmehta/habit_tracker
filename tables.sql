CREATE EXTENSION IF NOT EXISTS "citext";

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS users (
    user_id UUID NOT NULL PRIMARY KEY,
    email_id CITEXT NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    date_of_birth DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS stay_fit(
    entry_id UUID NOT NULL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users (user_id),
    entry_date DATE NOT NULL,
    entry_val BOOL NOT NULL 
);