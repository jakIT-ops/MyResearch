## Authorization Methods

The API calls made to any endpoint of Spotify API are validated based on whether the provided access token is valid or not. Spotify uses the OAuth 2.0 framework to provide these access tokens. In this lesson, we’ll discuss different types of flows Spotify API provides us to get access tokens.

### Types of flows

Spotify API provides the following four types of flows to get an access token:

* `Authorization code`: In this flow, the Spotify API server acts as an intermediary between the end user and us. We redirect the user to the Spotify API server, where the user logs in and grants us the required permissions. Once access has been granted, we get a code to give us the required permissions. We can use this code to get an access token, which can then be used while making the API calls.

* `Authorization code with` PKCE: This is the same flow as the authorization code but more secure. It has an extra parameter called code_verifier, which the API server authenticates before responding to the access code requests.

* `Client credentials:` This provides authentication rather than authorization because it doesn't require any permissions from the end user. We can request this access token by just using our credentials.

* `Implicit grant`: This is the same as the authorization code, but instead of getting an intermediary code, we directly get the access token using this flow. However, it has a very short lifespan and cannot be refreshed.


| Type of authorization flow | Requires user's permission | Can be refreshed | Is short-lived | Can be used to access or modify user's resources |
| :------------------------- | -------------------------- | ---------------- | -------------- | -------------------------------------------------|
| Authorization code 	     | 		Yes 		  | 	Yes	     |      No 	      | 		Yes				 |
| Authorization code with PKCE | Yes 			  |     Yes 	     |      No 	      | 		Yes				 |
| Client credentials 	     |       No			  |    No            |      No        |                 No 			         |
| Implicit grant  	     |    Yes 			  |   No   	     |      Yes       |                 Yes 			         |


## Authorization code

* First, we need to redirect the user to the Spotify API server by making a call to the base `URI https://accounts.spotify.com/authorize` with some query parameters. The user is asked to log in to Spotify using a dialog box.

* After the user has logged in, a dialog box will pop up asking the user to accept or deny our grant request.

* Once the user accepts our request, we'll receive a code.

* Then we’ll make an API call using the base URI `https://accounts.spotify.com/api/token` and some query parameters.

* Finally, we’ll receive an access token that we can use to access the user-specific endpoints.

<br>
<div align="center">
	<img src="img/authorizationCode.png">
	<br>
	<code>Authorization code workflow</code>
</div>
<br>


# 1. Search Spotify Resources

### Request parameters 

| Query parameter | Category | Type | Description |
| :-------------- | -------- | ---- | -----------:|
| `q` | Required | String | This is set to what we want to search using this endpoint. |
|`type`| Required| String | This is the category we want to search in. The possible options are: `album`, `artist`, `playlist`, `track`, `show`, `episode`. We can also use multiple categories by separating the using a comma(,). |
| `include_external` | Optional | String | This decides whether the user can play externally hosted audio or not. Its possible option is audio, which allows the user to play externally hosted audio. By default, the user is not allowed to do so. |
| `limit` | Optional | Integer | This limits the number of items to be returned in the response. Its value ranges from 0 to 50 and the default value is 20. |
| `market`| Optional | String | This is an ISO 3166-1 alpha-2 country code that we can use to fetch only the content available in a specific country. Some examples of country codes are us for the United States, es for Spain, and fr for France. If we send an auth code access token in the request header, the user's country will take priority over the country specified in this parameter. |
| `offset`| Optional | Integer | This parameter can be used to offset the first item we get in response. |

### Response fields

| Response field | Type | Description 			|
| :------------- | -----| -----------------------------:|
| `genres` 	 | String | This array contains the genres the artist has performed in. |
| `name`	 | String | This is the name of the artist. |
| `popularity`   | Integer| This index shows how popular an artist is on Spotify. It ranges from 0 to 100 with 100 being the most popular. |
| `images`       | Array of objects | This contains the information for the artist's images. Each object in this array contains three elements which give us the URL, height, and width of the image respectively. |
| `id` | String | This is the Spotify ID of the artist. |
| next | String | This is the link to the next page. |
| previous | String | This is the link to the previous page. |
| total | Integer | This tells us the total number of albums that we get in response. |

| Response field | Type | Description |
| :------------- | ---- | -----------:|
| `album_type` |String | This defines the albums type. |
| `spotify` | String | We can use this link to redirect the user to the requested item on Spotify.|
| `id`  | String | This is the Spotify ID of the requested item. |
| `name` | String | This is the name of the requested item. |
| `available_markets` | Array of objects | This is a list of countries where the album is available. |
| `images` |Array of objects | This array contains the links of images associated with the albums and their dimensions. |
| `release_date` |String | This is the release date of the album. |
| `total_tracks` |Integer| This is the number of tracks the album contains.  |

# 1. Artists

## Artist Information

The Get Artist endpoint is used to get information about an artist using the artist’s Spotify ID. The base URL of this endpoint is `https://api.spotify.com/v1/artists/{id}`. The path parameter {id} is replaced with the artist’s ID whose information we want. Let’s assume that we want to get details of an artist with Spotify ID `sample_id`. Our URL in this case will be `https://api.spotify.com/v1/artists/sample_id`.

### Response fields

| Response field | Type | Description |
| :------------- | ---- | ----------: |
| `spotify` | String | This is the Spotify URL of the artist. |
| `followers` | Object | This object contains objects which provide information about the followers of the artist. It contains two elements: href which will always be NULL and total which shows the number of followers.
| `genres` |String array | This array contains the genres the artist has performed in. |
| `href` | String | This is a link to the endpoint which provides full details of the artist. |
| `id` |  String | This is the Spotify ID of the artist. |
| `images` | Array of objects | This contains the information for the artist's images. Each object in this array contains three elements which give us the URL, height, and width of the image respectively. |
| `name` | String | This is the name of the artist. |
| `popularity` | Integer | This is the artist's popularity rating based on the rating of the artist's tracks. This ranges between 0 and 100, with 100 being the most popular. |

## Multiple artists' details

Imagine running the above endpoint for each artist ID to get the details of multiple artists. It’s not very scalable. However, the Spotify API itself provides the solution. We can use the Get Several Artists endpoint that fetches details of multiple artists, using their Spotify IDs with only one API call. The base URI of this endpoint is `https://api.spotify.com/v1/artists`.

## Artis's albums

Everyone has a favorite musician to whom they can listen endlessly. No matter which valley we wander off to, we do always end up circling back to the same artist. The Get Artist’s Albums endpoint can help us get our favorite artists’ albums.

The base URL `https://api.spotify.com/v1/artists/{id}/albums` is used to get information about the albums of an artist. The path parameter {id} is replaced with the artist’s ID whose albums we want to fetch. So if we’re going to fetch albums of an artist whose Spotify ID is `sample_id`, the URL will be `https://api.spotify.com/v1/artists/sample_id/albums.`

### Request parameters 


| Query parameter | Category |Type | Description |
| :-------------- | -------- |---- | ----------: |
| `include_groups`| Optional | String | This can be used to filter the albums based on the artist's involvement in the album. The possible options are album, single, appear_on, compilation We can also assign multiple values to this parameter by separating those values using a comma(,). |
| `limit` | Optional | Integer | This limits the number of items to be returned in the response. Its value ranges from 0 to 50 and the default value is 20. |
| `market` | Optional| String | This is an ISO 3166-1 alpha-2 country code that we can use to fetch only the content available in a specific country. Some examples of country codes are us for the United States, es for Spain, and fr for France. If we send an auth code access token in the request header, the user's country will take priority over the country specified in this parameter. |
| `offset` | Optional | Integer | This parameter can be used to offset the first item we get in response. |


### Response fields

Some important response fields are given in the table below:

| Response field | Type | Description |
| :------------- | ---- | -----------:|
| name | String | name in the items array is the name of the album. |
| spotify | Array | This is an external link which can be used to open this album on Spotify. |
| release_date | String | This is the release date of the album. |
| artists | Array of objects | This array contains information about the artist. |
| images | Array of objects | This array contains cover images of the albums. |
| id | String | This is the Spotify ID of the album. |
| `available_markets` |  Array of objects | This array contains the ISO 3166-1 alpha-2 country code of the countries in which this album is available. |
| `total` | Integer | This tells us the total number of albums that we get in response. |


## Artist's Top Tracks

In this lesson, we'll discuss the Get Artist's Top Tracks endpoint, which we can use to get the top tracks of an artist. The top tracks are the ones that have the most number of recent plays. If a track was played frequently in the past, it would be lower in the ranking than the tracks frequently played now.

The base URL https://api.spotify.com/v1/artists/{id}/top-tracks is used to get the top tracks of an artist. The path parameter {id} is replaced with the artist’s ID whose top tracks we want to fetch. So if we want the top tracks of an artist whose Spotify ID is sample_id, the URL will be https://api.spotify.com/v1/artists/sample_id/tracks.

### Request parameters 

| Query parameter |Category | Type | Description| 
| :-------------- |-------- | ---- | ----------:|
| `market` | Optional | String | This is an ISO 3166-1 alpha-2 country code that we can use to fetch only the content available in a specific country. Some examples of country codes are us for the United States, es for Spain, and fr for France. If we send an auth code access token in the request header, the user's country will take priority over the country specified in this parameter. |

### Response fields

`albim`, `artists`, `name`, `spotify`, `popularity`, `preview_url`, `duratiom_ms`, `id`, `total`


# 2. Albums

We can manage the albums saved in a user profile using the Spotify API. In this lesson, we’ll discuss two types of HTTP requests. One is used to save an album to the current user profile whereas the other is used to remove an album from a user profile.

We can use the base URL https://api.spotify.com/v1/me/albums to save or delete an album to the current user's profile. A PUT request to this endpoint saves the album whereas a DELETE request deletes the specified album.

### Save an album to a suer profile 

Let's look at how this endpoint is used to save albums with the authorization code access token. We're providing the IDs of Pitbull's album Can't Stop Us Now, and Bruno Mars' albums Doo-Wops & Hooligans as the values for the query parameter ids.

```py
url = ('https://api.spotify.com/v1/me/albums?'
       'ids=4aawyAB9vmqN3uQ7FjRGTy,1uyf3l2d4XYwiEqAb7t7fX')
      #4aawyAB9vmqN3uQ7FjRGTy is the ID of Pitbull's album Can't Stop Us Now
      #1uyf3l2d4XYwiEqAb7t7fX is the ID of Bruno Mars's album Doo-Wops And Hooligans
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer AUTHORIZATION_CODE_ACCESS_TOKEN'
}

response = requests.request("PUT", url, headers=headers,params={})
if response.status_code==200:
  print(response.status_code)
else:
  print(json.dumps(response.json(), indent=4))
```

### Remove an album from the user profile

```py
url = ('https://api.spotify.com/v1/me/albums')
data={"ids":"4aawyAB9vmqN3uQ7FjRGTy"}
      #4aawyAB9vmqN3uQ7FjRGTy is the ID of Pitbull's album Can't Stop Us Now
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer AUTHORIZATION_CODE_ACCESS_TOKEN'
}

response = requests.request("DELETE", url, headers=headers,params=data)
if response.status_code==200:
  print(response.status_code)
else:
  print(json.dumps(response.json(), indent=4))
```

### Response fields

The content of the response is empty for a successful request, and the value of `status_code` is `200`. For an unsuccessful request, we get a `message` in response that tells us about the error.

## User’s saved albums

The base URL https://api.spotify.com/v1/me/albums is used to get information about the albums saved in the current user’s profile. We used this endpoint to save and remove albums from a user profile using PUT and DELETE requests respectively. Now, we’ll send a GET request to this endpoint to get a list of the albums saved in the user’s profile.

### Request parameters

`limit`, `market`, `offset`

### Response fields 

`name`, `spotify`, `release_date`, `popularity`, `tracks`, `images`, `id`, `copyrights`, `artists`

# 3. Playlist 

## Create Playlist and Add Items to a Playlist

### New playlist

The Create Playlist endpoint of the Spotify API creates a playlist using our current user's Spotify account. The base URI of this endpoint is `https://api.spotify.com/v1/users/{user_id}/playlists`. We'll need the Spotify ID of the user to create the playlist. The {user_id} in the base URI is replaced with the Spotify ID of the user while calling the API. A POST request is used to create a playlist. The playlist created will be empty.

#### Request parameters

`name`, `pulic`, `collaborative`, `description`

#### Response fields

`description`, `owner`, `tracks`, `images`, `id`, `name`

### Add tracks to a playlist

The playlist we've just created using the user's profile is empty.  Let’s learn how to add tracks to that playlist or in any user playlists using Add Items to Playlist endpoint.

The base URI of this endpoint is https://api.spotify.com/v1/playlists/{playlist_id}/tracks. The {playlist_id} in the base URI is replaced with the Spotify ID of the playlist when making an API call. So if we want to add tracks in a playlist whose ID is sample_id, our base URI will be https://api.spotify.com/v1/playlists/sample_id/tracks.

Request parameters

`position`, `uris`


## Featured Playlists and Playlist Items

Featured playlists are the most popular playlists among Spotify users. We can get a list of these playlists using the Get Featured Playlists endpoint. The base URI of this endpoint is `https://api.spotify.com/v1/browse/featured-playlists`.

### Request parameters

`limit`, `country`, `locale`, `offset`, `timestamp`

### Response fields

`description`, `owner`, `tracks`, `images`, `id`, `name`

## Playlist items

Each playlist has its number of tracks which we get in response to the API call to the endpoint we discussed above. We can get more information about these tracks using the Playlist Items endpoint. The base URL for this endpoint is https://api.spotify.com/v1/playlists/{id}/tracks. The path parameter {id} will be replaced with the playlist ID when we want to make an API call. Let's assume that we want to fetch a playlist with Spotify ID sample_id. Our URL, in this case, will be https://api.spotify.com/v1/artists/sample_id.

### Request parameters

`additional_types`, `fields`, `limit`, `market`, `offset`

### Response fields

`album`, `episode`, `name`, `popularity`, `preview_url`, `artists`, `duration_ms`, `id`, `available_markets`

# 4. Tracks 

The base URL `https://api.spotify.com/v1/me/tracks` is used to save or delete tracks to the current user's profile. The PUT request saves the track, whereas a DELETE request removes the specified track from the user profile.




	

































































