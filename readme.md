Project Heimdall Backup


# Admin Server (Yggdrasil)
- Heimdall verwaltet die Server durch Backups und erstellt einen Tor Server, wo User vor per Dropdown Server auswählen und nach Eintritt verlangen
# Tor Server (Midgard)
- Der User muss ein Modal mit 3 Fragen auswählen, zusätzlich kann der User sein Twitter Profil angeben, vllt später noch zusätzlich einen Code, den der User auf Twitter oder anderen Websites per PN bekommt.
- Die Admins haben dann die Möglichkeit die Anfrage des User zu akzeptieren oder abzulehnen, wird akzeptiert, so bekommt der User einen Einmal Invite Link.

# Funktion Backup:
- Heimdall trägt jeden Server, Channel und Nachricht in die DB, ausgenommen sind Yggdrasil und Midgards Channel
- Heimdall speichert den Anhang einer Nachricht unter GuildID/ChannelID/MessageID ab und in der DB als hasFiles = True

# Funktion Server-List:
- Löscht alle Nachrichten aus dem Channel server-list und fügt als Embed alle Server mit Infos über diesen hinzu, so wie einem Invite Link, falls ein Admin der nicht für diesen Server zuständig ist drauf möchte.

# Database:
## Guilds
```
create table Guilds
(
id bigint primary key,
name varchar(128),
inviteUrl varchar(128)
);
```

## Channels
```
create table Channels
(
id bigint primary key,
guildId bigint,
name string,
constraint fk_Guild_Channel foreign key(guildId) references Guilds(id)
);
```

## Messages
```
create table Messages
(
id bigint primary key,
channelId bigint,
hasFiles bool,
message text,
date_time datetime,
userId bigint,
constraint fk_Channel_Message foreign key(channelId) references Channels(id)
);
```