import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class AIAgent:

    def generate_itinerary(self, destination, days, budget):

        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        prompt = f"""
        Create a {days}-day travel itinerary.

        Destination: {destination}
        Budget: ₹{budget}

        Include:
        - Attractions
        - Food recommendations
        - Activities

        Return a day-wise itinerary.
        """

        response = model.generate_content(prompt)

        return response.text.strip()