Clans REST API
==============

Simple API using Falcon web framework.

Requirements
============
This project uses [virtualenv](https://virtualenv.pypa.io/en/stable/) as isolated Python environment for installation and running. Therefore, [virtualenv](https://virtualenv.pypa.io/en/stable/) must be installed. And you may need a related dependency library for a PostgreSQL database. See *install.sh* for details.


Installation
============

At first write database config file in
```
    app/etc/config/settings.conf
```

Install all the python module dependencies in requirements.txt

```
  ./install.sh
```

Start server

```
  ./bin/run.sh start
```

For populate random data launch (*need request package or venv activate*)
```shell
   python3 post_players.py  

```

Usage
=====

Create an user
- Request
```shell
curl -XPOST http://localhost:5050/users/ -H "Content-Type: application/json" -d '{
 "name": "player1",
 "battles_total": 1,
 "wins_total": 1
}'
```

- Response
```json
{
    "meta": {
        "code": 200,
        "message": "OK"
    },
    "data": null
}
```

Get all users and their stats:

- Request
```shell
curl -XGET http://localhost:5050/users/
```

You can use query params limit

- Response
```json
{ "meta": {
    "code": 200,
    "message": "OK"
    },
"data": [
    {"created_at": "2017-03-24 12:33:24.610819",
    "id": 1,
    "name": "player1",
    "battles_total": 1,
    "wins_total": 1,
    "vehicles_x": 0,
    "exp_total": 0,
    "is_hidden": false,
    "days_total": 0,
    "rating": 1.0,
    "exp_avg": 0.0
    }
}
```

Update profile
- Request

```shell
curl -XPUT http://localhost:5050/users/1/ -H "Content-Type: application/json" -d '{
 "name": "new_player",
 "exp_total": 500,
 "battles_total": 3
}'
```


Delete profile
- Request

```shell
curl -XDELETE http://localhost:5050/users/1/
```

