from agents.hotel_agent import HotelAgent
from agents.budget_agent import BudgetAgent
from agents.itinerary_agent import ItineraryAgent
from agents.weather_agent import WeatherAgent


class CoordinatorAgent:

    def __init__(self):

        self.hotel_agent = HotelAgent()
        self.budget_agent = BudgetAgent()
        self.itinerary_agent = ItineraryAgent()
        self.weather_agent = WeatherAgent()

    def process_request(self, data):

        destination = data.get("destination")
        budget = data.get("budget")
        days = data.get("days")

        hotel = self.hotel_agent.suggest_hotel(destination,budget)

        daily_budget = self.budget_agent.calculate_budget(
            budget,
            days
        )

        itinerary = self.itinerary_agent.create_itinerary(destination,days)
        weather = self.weather_agent.get_weather(
    destination
)
        return {
    "status":"success",

    "trip_summary": {
        "destination": destination,
        "weather": weather,
        "total_budget":budget
    },

    "recommendations":{
        "hotel":hotel,
        "weather":weather,
        "daily_budget":daily_budget
    },

    "itinerary":itinerary
}