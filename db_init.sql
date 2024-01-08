create table "user" (
    id uuid primary key,
    name varchar unique,
    role uuid,
    email varchar unique,
    hashed_password varchar
);

create table "player" (
    id uuid primary key,
    user_id uuid references "user"(id),
    name varchar,
    gamertag varchar,
    region varchar,
    avatar_path varchar
);

create table "slp" (
    id uuid primary key,
    filepath varchar,
    description varchar,
    event_id uuid references "event"(id),
    player1_id uuid references "player"(id),
    player1_char varchar,
    player2_id uuid references "player"(id),
    player2_char varchar
);

create table "event" (
    id uuid primary key,
    name varchar,
    date timestamp,
    bracket varchar,
    stream varchar,
    location varchar
);
