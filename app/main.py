import openai
import requests

# Initialize the OpenAI API
openai.api_key = "your_openai_api_key_here"  # Replace with your API key
weather_api_key = "your_weather_api_key_here"  # Replace with your OpenWeather API key

def get_travel_suggestions(prompt):
    """
    Function to interact with OpenAI GPT for travel suggestions.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI travel agent."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def get_weather(destination):
    """
    Function to fetch current weather for a given destination.
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={destination}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The current weather in {destination} is {weather_desc} with a temperature of {temp}°C."
        else:
            return f"Unable to fetch weather for {destination}. Please check the city name."
    except Exception as e:
        return f"Error: {str(e)}"

def generate_booking_links(destination):
    """
    Generate booking links for flights and hotels.
    """
    flight_url = f"https://www.expedia.com/Flights-Search?destination={destination.replace(' ', '+')}"
    hotel_url = f"https://www.booking.com/searchresults.html?city={destination.replace(' ', '+')}"
    return f"- Flights: {flight_url}\n- Hotels: {hotel_url}"

def save_trip_plan(destination, suggestions):
    """
    Save the trip plan to a file.
    """
    filename = f"Trip_Plan_{destination.replace(' ', '_')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Destination: {destination}\n")
        f.write("Travel Suggestions:\n")
        f.write(suggestions)
        print(f"\nTrip plan saved as {filename}")

def main():
    print("Welcome to the Advanced AI Travel Agent App!")
    print("Plan your next adventure effortlessly with personalized suggestions, weather updates, and more.\n")

    while True:
        print("Enter your preferences (e.g., budget, location, activities) or type 'exit' to quit.")
        user_input = input("Your preferences: ")
        if user_input.lower() == 'exit':
            print("Thank you for using the AI Travel Agent App. Safe travels!")
            break

        print("Do you have specific destinations in mind? Separate multiple destinations with commas.")
        destinations = input("Destinations: ").strip().split(',')

        for destination in destinations:
            destination = destination.strip()
            if destination:
                print(f"\nFetching weather details for {destination}...")
                weather_info = get_weather(destination)
                print(weather_info)

                print("\nPlanning your trip...")
                prompt = f"Preferences: {user_input}. Destination: {destination}."
                suggestions = get_travel_suggestions(prompt)
                print("\nHere are the suggestions:")
                print(suggestions)

                print("\nBooking Links:")
                print(generate_booking_links(destination))

                save_option = input("\nWould you like to save this trip plan? (yes/no): ").lower()
                if save_option == 'yes':
                    save_trip_plan(destination, suggestions)

        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
