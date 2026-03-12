from locust import HttpUser, task, between

class MLInferenceUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def predict(self):

        payload = {
            "features": [5.1, 3.5, 1.4, 0.2]
        }

        self.client.post(
            "/predict",
            json=payload
        )