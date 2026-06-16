from agents.hotel_agent import HotelAgent
from agents.budget_agent import BudgetAgent
from agents.itinerary_agent import ItineraryAgent


class CoordinatorAgent:

    def __init__(self):

        self.hotel_agent = HotelAgent()
        self.budget_agent = BudgetAgent()
        self.itinerary_agent = ItineraryAgent()

    def process_request(self, data):

        destination = data.get("destination")
        budget = data.get("budget")
        days = data.get("days")

        hotel = self.hotel_agent.suggest_hotel(destination)

        daily_budget = self.budget_agent.calculate_budget(
            budget,
            days
        )

        itinerary = self.itinerary_agent.create_itinerary(days)

        return {
            "status": "success",
            "hotel": hotel,
            "daily_budget": daily_budget,
            "itinerary": itinerary
        }