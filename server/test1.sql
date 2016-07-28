drop table if exists Applications;
create table Applications(ID integer primary key autoincrement, AppID integer, State varchar(100) not null, Description varchar(500) not null, Version integer, Origin varchar(300) not null, URL varchar(200) not null, File sql_variant);
INSERT INTO Applications(AppID, State, Description, Version, Origin, URL) VALUES ('90', 'Installed', 'Test App 1', '1.0.0', 'ON.Lab', 'google.com');
INSERT INTO Applications(AppID, State, Description, Version, Origin, URL) VALUES ('45', 'Downloaded', 'Test App 2', '1.0.1', 'AT&T', 'facebook.com');
INSERT INTO Applications(AppID, State, Description, Version, Origin, URL) VALUES ('2', 'Installed', 'Test App 3', '1.1.0', 'Verizon', 'yahoo.com');