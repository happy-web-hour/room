# room
## APIs
- GET /room/{pin} - retorna lista de salas

**Request**	

**Response**
200
```json 
[
	{
		"roomId": "string",
		"name": "string"
	}
]
```

- POST /room/{roomId}/{userId} - insere usuário na sala  

**Request**	

**Response**
200

- GET /room/{roomId} - retorna lista de usuários

**Request**	

**Response**
200
```json 
[
	{
		"userId": "string",
		"name": "string"
	}
]
```

- DELETE /room/{roomId}/{userId} - remove usuário na sala

**Request**	

**Response**
200

- POST /room/{pin} - cria um novo Happy Hour

**Request**	

**Response**
200

- DELETE /room/{pin} - apaga o Happy Hour

**Request**	

**Response**
200

## Database
```json
[
	{
		"pin":"string",
		"rooms":[
			{
				"roomId": "string",
				"name": "string",
				"users": [
					"string"
				]
			}	
		]
	}
]
```