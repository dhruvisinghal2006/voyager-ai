class ItineraryAgent:

    def create_itinerary(self, destination, days):

        itineraries = {

            "Goa": [
                "Visit Baga Beach",
                "Explore Fort Aguada",
                "Enjoy Water Sports",
                "Sunset Cruise"
            ],

            "Manali": [
                "Visit Hadimba Temple",
                "Explore Solang Valley",
                "Visit Rohtang Pass",
                "Shopping at Mall Road"
            ],

            "Jaipur": [
                "Visit Amer Fort",
                "Explore City Palace",
                "See Hawa Mahal",
                "Shopping at Johari Bazaar"
            ]
        }

        plan = itineraries.get(
            destination,
            ["Explore local attractions"]
        )

        return plan[:days]