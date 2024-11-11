from datetime import datetime
import pytz

def get_time_in_timezone(country):
    try:
        # Get the timezone for the country
        timezone = pytz.timezone(country)
        # Get the current time in that timezone
        country_time = datetime.now(timezone)
        # Format the time
        formatted_time = country_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    except Exception as e:
        return f"Invalid timezone: {country}"

# List of some common time zones for reference
timezones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Nairobi": "Africa/Nairobi",
    "UTC": "UTC"
}

print("Available time zones:", ", ".join(timezones.keys()))
# Ask the user to input a timezone
user_input = input("Enter a city (e.g., New York, London, Tokyo): ")
country_timezone = timezones.get(user_input)

if country_timezone:
    print(f"Current time in {user_input}: {get_time_in_timezone(country_timezone)}")
else:
    print("Timezone not found. Please enter a valid city from the list.")
