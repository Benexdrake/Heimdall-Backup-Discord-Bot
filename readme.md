Project Heimdall Backup

Admin aka Yggdrasil Server

Vom Admin Server wird alles verwaltet.

Heimdall hat die Funktion die Server vor eindringlingen zu schützen und alles per Backup zu speichern, für den Fall eines eindringlings der per Meldungen einen Server löschen lässt.

Per /Create_Bifröst wird ein Tor Server erstellt, mit einem Channel namens Midgard, so wie löschung aller anderen Channels.
Danach erstellt der Bot einen Block mit Regeln, einem Dropdown und einem Button.

Klickt der User auf den Button, so öffnet sich ein Modal mit Fragen.
Wird das Modal abgesendet, so wird eine Nachricht an den Admin Server gesendet, mit Informationen über den User, so wie 2 Buttons, Accept/Decline.

- Accept: User bekommt eine Nachricht vom Bot mit einem einmaligen Invite Link und wird danach vom Tor Server geworfen.
  Wenn der User auf den Server beitritt, bekommt er eine Rolle, so wie eine Welcome Benachrichtigung, so wie eine Benachrichtigung an die Admins.

- Decline: Modal öffnet sich und ein Admin kann dort eine Begründung eingeben, danach bekommt der User eine Nachricht vom Bot mit der Begründung und wird danach vom Server geworfen.

Yggdrasil Commands: - Create_Bifröst - Insert Server invite_link: - Recovery guild_name: - Servers

Alle Secret Servers Command: - backup

Funktionen:

Create Bifröst - Erstellt einen Tor Server und trägt die neue Guild ID so wie Invite Link in die DB, sollte es schon einen Tor Server geben, so wird dieser überschrieben. - Erstellt einen Channel namens Midgard und löscht alle anderen Channels. - Sendet eine Nachricht an den Channel Midgard mit Regeln, einem Dropdown für mehrere Server(holt sich die Servernamen aus der DB) und ein Invite request Button. - Passt den Channel an, so dass niemand schreiben darf.

Backup - Schaltet Backup für einen Channel aus oder ein, je nachdem was in der DB steht, beim erstellen eines Channels wird hasBackup auf True gesetzt, es ist vom Standard aus an.

Recovery - Wiederherstellung eines Discord Servers, funktioniert nur wenn der Server der wiedergestellt werden soll nicht mehr existiert.

Servers - Bot erzeugt eine Liste von allen Servern mit Invite Links als Embed

DB:

Guild: - id: ulong - name: string - inviteUrl: string

Blacklist: - userID: ulong

Channel: - id: ulong - guildID: ulong - hasBackup boolean

Message: - id: ulong - hasFiles:boolean - message:string - datetime:datetime - userId: ulong

Admin Server Yggdrasil: - Channels: - Invites - Hier sendet Heimdall die Invite Request von Midgard - Logs - Alle wichtigen Informationen werden hier als Log gesendet - Servers - Eine Liste alle vorhandenen Server, wird hinzugefügt sobald ein neuer Server eingetragen wird, mit Information zum Server, so wie einen Invite Link

Database Query:

create table Guilds
(
id bigint primary key,
guildName varchar(128),
inviteUrl varchar(128)
);

create table Channels
(
id bigint primary key,
guildId bigint,
hasBackup boolean,
constraint fk_Guild_Channel foreign key(guildId) references Guilds(id)
);

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

Aufgaben:

- Slash Commands:

  - create bifroest []
  - recovery []
  - show servers []

- Events:

  - error []
  - on guild join []
  - on member join []
  - on ready []
  - discord.on_guild_remove(guild) []
  - discord.on_guild_update(before, after) []
  - discord.on_guild_channel_create(channel) [<3]
  - discord.on_member_remove(member) []
  - discord.on_message(message) [<3]
  - discord.on_message_edit(before, after) []

- Logic:

  - Guild in DB [<3]
  - Channel in DB []
  - Message in DB []

Ideen:

- Events:

- Slash Commands:
