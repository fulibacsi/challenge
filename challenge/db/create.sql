PRAGMA foreign_keys = 1;


create table if not exists profile(
    user_id integer primary key,
    email text unique not null,
    username text not null,
    password text not null,
    pic text,
    description text default ""
);

create table if not exists team(
    team_id integer primary key,
    name text unique not null,
    description text default "",
    admin_id integer not null,
    constraint team_fk foreign key (admin_id)
     references profile(user_id)
);

alter table profile add column team_id integer
 references team(team_id);

 create table if not exists challenge_desc(
    ch_id integer primary key,
    name text unique not null,
    description text default "",
    winning_condition  text not null,
    award text,
    winner_id integer not null,
    constraint challenge_desc_fk foreign key (winner_id)
     references profile(user_id)
);

create table if not exists challenge(
    ch_id integer,
    user_id integer,
    constraint challenge_pk primary key (ch_id, user_id),
    constraint challenge_profile_fk foreign key (user_id)
     references profile(user_id),
    constraint challenge_ch_fk foreign key (ch_id)
     references challenge_desc(ch_id)
);
