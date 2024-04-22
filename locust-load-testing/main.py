from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)


    @task
    def addNewPet(self):
        payload = {
            "id": 1,
             "category": {
            "id": 1,
             "name": "Golden"
             },
             "name": "Doggie",
            "photoUrls": [
            "https://images.app.goo.gl/G31j2FeZJNUkPXTC8"
            ],
            "tags": [
            {
            "id": 1,
             "name": "Old"
            }
             ],
             "status": "available"
            }
        self.client.post("/v2/pet", json=payload)

    @task
    def findByID(self):
        self.client.get("/v2/pet/1")

    @task
    def updatePet(self):
        payload = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "Golden"
            },
            "name": "Doggie",
            "photoUrls": [
                "https://images.app.goo.gl/G31j2FeZJNUkPXTC8"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "Old"
                }
            ],
            "status": "unavailable"
        }
        self.client.put("/v2/pet", json=payload)


    @task
    def deletePet(self):
        payload = {
            "id": 2,
             "category": {
            "id": 2,
             "name": "Golden"
             },
             "name": "Doggie",
            "photoUrls": [
            "https://images.app.goo.gl/G31j2FeZJNUkPXTC8"
            ],
            "tags": [
            {
            "id": 2,
             "name": "Baby"
            }
             ],
             "status": "available"
            }
        self.client.post("/v2/pet", json=payload)
        self.client.delete("/v2/pet/2")



