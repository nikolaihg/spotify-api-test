# spotify-api-test

## Prequisites

Spotify Developer Account: Sign up at the Spotify Developer Dashboard if you haven't already.
Create a Spotify Application: In the Spotify Developer Dashboard, create a new app. This will provide you with the Client ID and Client Secret, which are needed for authentication.

## Notes
To get listener data for an artist from the Spotify API, you can use the Get Artist endpoint (GET https://api.spotify.com/v1/artists/{id}). This endpoint provides information about the artist, including the total follower count, but it doesn’t provide real-time "listener" data such as monthly listeners directly. Instead, it provides:

    - Total followers: A static count of how many users follow the artist on Spotify.
    - Popularity: A numeric rating (0 to 100) indicating how popular the artist is on Spotify, based on various factors, including recent listening activity.