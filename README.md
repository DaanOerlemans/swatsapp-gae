swatsapp-gae
============

Google App Engine project for SwatsApp.

## API calls

Here i will explain what calls can be made to the backend. This document will be supplemented while programming.

**base url**

`http://www.TBD.nl`

### Create user - POST

Create a new user.

`/users`

The request should be an *application/json* containing at least the real name, the username and the password of the user.

**Input**

| Name      | Type    | Description                       |
| --------- | ------- | --------------------------------- |
| name      | String  | The real name of the user         |
| device_id | String  | The unique id of the users device |

**Request**

```
POST /users
Content-Type: application/json

{
    "name": "Hans de Vries",
    "device_id": "fe161d7d6c2532241f1e840ce57a5b77"
}
```