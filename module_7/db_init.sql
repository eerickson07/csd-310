DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Biggolfer07';

GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE player  (
    player_id    INT            NOT NULL        AUTO_INCREMENT,
    first_name   VARCHAR(75)    NOT NULL,
    last_name    VARCHAR(75)    NOT NULL,
    team_id      INT            NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot)
    VALUES('Team Red', 'Foxes');

INSERT INTO team(team_name, mascot)
    VALUES('Team Blue', 'Smurfs');

INSERT INTO player(first_name, last_name, team_id)
    VALUES('John', 'Smith', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Adam', 'Johnson', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Robert', 'White', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jake', 'Dell', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Steve', 'Erickson', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Harry', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Red'));