class HotelAgent:

    def suggest_hotel(self,destination,budget):
        hotels={
            "Goa": [
                "Taj Resort Goa",
                "W Goa",
                "Grand Hyatt Goa"
            ],

            "Manali":[
                "The Himalayan",
                "Snow Valley Resort",
                "Manu Allaya Resort"
            ],

            "Jaipur":[
                "Rambagh Palace",
                "ITC Rajputana",
                "Holiday Inn Jaipur"
            ]
        }

        destination_hotels=hotels.get(
            destination,
            ["Hotel information not available"]
        )

        if budget >50000:
            return destination_hotels[0]
        
        elif budget>25000:
            return destination_hotels[1]
        
        else:
            return destination_hotels[2]