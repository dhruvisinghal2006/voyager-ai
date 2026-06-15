class CoordinatorAgent:

    def process_request(self, data):

        destination = data.get("destination")
        budget = data.get("budget")
        days = data.get("days")

        return {
            "status": "success",
            "message": f"Planning a {days}-day trip to {destination} with budget ₹{budget}",
            "trip_data": data
        }