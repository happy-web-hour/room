db.createCollection("room");
db.room.insertMany([
    {
		"pin":"happy-hour-1",
		"rooms":[
			{
				"roomId": "f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
				"name": "sala 01",
				"users": []
			}
		]
	},
    {
		"pin":"happy-hour-2",
		"rooms":[]
	}
]);