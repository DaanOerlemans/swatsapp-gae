swatsapp-gae
============

Google App Engine project for SwatsApp.

## API calls

Here i will explain what calls can be made to the backend. This document will be supplemented while programming.

**base url**

`http://swatsapp-gae.appspot.com`

### Create user - POST

Create a new user.

`/users`

The request should be an *application/json* containing at least the real name and the unique device id of the user.

**Input**

| Name      | Type    | Description                       |
| --------- | ------- | --------------------------------- |
| name      | String  | The real name of the user         |
| device_id | String  | The unique id of the users device |

**Request**

```
POST /users HTTP/1.1
Content-Type: application/json

{
    "name": "Hans de Vries",
    "device_id": "fe161d7d6c2532241f1e840ce57a5b77"
}
```

**Response**

If the user was successfully created the response contains the created user.
```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "name": "Hans de Vries",
    "device_id": "fe161d7d6c2532241f1e840ce57a5b77",
    "photos": []
}
```
### Create news item - GET

Create a new news item.

`/news_item`

**Request**

```
GET /news_item HTTP/1.1
```

**Response**

```
<html>
  <body >
    <form action="/news_item" method="post">
      <div><textarea name="content" rows="4" cols="60"></textarea></div>
      Controleer goed op spelling, het bericht kun je niet meer verwijderen.
      <div><input type="submit" value="Nieuwtje toevoegen"></div>
    </form>
  </body>
</html>
```
Whatever you enter in this form will be added as an news item in the backend.

### Get news - GET

Get al news from the backend.

`/news_items`

**Request**

```
GET /news_items HTTP/1.1
```

**Response**

```
HTTP/1.1 200 Ok
Content-Type: application/json

[
	{
		"poster": "guus_cloo",
		"message": "RT @guus_cloo: Vanavond afterparty carnaval van @VcdeSwatsers #opemake",
		"poster_profile_picture": "http://pbs.twimg.com/profile_images/378800000245307233/f0afc6e7cd43ccc841921a989013220c_normal.jpeg",
		"image_url": "http://pbs.twimg.com/media/BhqzNYdIMAAXS7W.jpg"
	}
]
```

