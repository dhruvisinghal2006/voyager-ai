class HotelAgent:
    def suggest_hotel(self,destination):

        hotels={
            "Goa":"Taj Resort Goa",
            "Delhi":"The Leela Palace",
            "Jaipur":"Rambagh Palace"
        }

        return hotels.get(destination,"Hotel not found")