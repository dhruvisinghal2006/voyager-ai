class ItineraryAgent:

    def create_itinerary(self, days):

        itinerary = []

        for day in range(1, days + 1):

            itinerary.append(
                f"Day {day}: Explore local attractions"
            )

        return itinerary