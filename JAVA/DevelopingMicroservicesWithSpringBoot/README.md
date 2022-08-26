## `@RequestMapping` attributes


| Attribute | Return Type | Description | Sample Usage |
| :-------- | ----------- | ----------- | -----------: |
| value() or path () |	String[] | endpoint  | `@RequestMapping(value = { "/playlist" })` or `@RequestMapping(path = { "/playlist" })` |
| method() | RequestMethod[] | request method type |	`@RequestMapping(method = { RequestMethod.GET, RequestMethod.POST })` |
| params() | String[] |	request parameters |	`@RequestMapping(params = { "key1=value1", "key2=value2" })` |
| headers()| String[] |	request headers|  `@RequestMapping(headers = { "content-type=application/json", "accept=application/json" })` |
| consumes() |	String[] | request content-type |	`@RequestMapping(consumes = { "text/plain", "application/*" })` | 
| produces() |	String[] | response content-type |	`@RequestMapping(produces = { "text/plain", "application/*" })` |


## Over-ridable configurations

The below table shows a few of the over-ridable configurations that can be changed as per the application. The following properties need to be matched with the appropriate values in either application.properties or application.yml placed under src/main/resources or they can be overridden by passing as a JVM argument when launching the application.

| Property |	Default Value	| Description |
| :------- | ------------------ | ----------: |
| `spring.h2.console.enabled` | false |	Tells whether to enable the console |
| `spring.h2.console.path` |	/h2-console |	Defines the path at which the console is available |
| `spring.h2.console.settings.trace` |	false	| Tells whether to enable trace output |
| `spring.h2.console.settings.web-allow-others` | false | Tells whether to enable remote access |
| `spring.jpa.show-sql`	| false | Tells whether to enable logging of SQL statements |


# Project EndPoints

| HTTP Method |	Endpoint | Request Handling Method | Description  |
| :---------- | -------- | ----------------------- | -----------: |
| GET |	/playlist/	| root() |	returns “application is working!” when called |
| GET |	/playlist/all	| getAllPlaylists() |	returns Iterable<Playlist> when called |
| GET |	/playlist/{id}	| getPlaylistById(BigInteger)	 |returns the Playlist with the given id when called |
| POST|	/playlist/{name} |	createPlaylist(String)| 	for creating a new Playlist with the given name and returns the same after creation |
| DELETE |	/playlist/{id} |	deletePlaylist(BigInteger) |	for deleting a Playlist by id |
| GET |	/playlist/{id}/songs |	getSongsInPlaylist(BigInteger)	| for fetching all the songs inside the Playlist with the given id |
| DELETE |	/playlist/{id}/songs |	deleteAllSongsInPlaylist(BigInteger) |	for deleting all the songs in the Playlist with the given id |
| POST |	/playlist/{id}/add |	addSongToPlaylist(BigInteger, Song) |	for adding the given Song to the Playlist with the given id and returns the created song |
| GET |	/playlist/songs	getAllSongs() |	returns List<Songs> | that fetches all the songs from all the playlists |
| PUT |	/playlist/songs/{id}/move |	moveSongToDifferentPlaylist(BigInteger, BigInteger) |	for moving a song from one playlist to another |
| DELETE |	/playlist/{id}/songs/{song_id} | deleteFromPlaylist(BigInteger, BigInteger) |	for deleting a song from a playlist |













