
def main():
    print("-------Weekly Temperature Analyzer")

    temperatures = []

    days = int(input("How many days of Data do you have? "))

    for i in range (days):
        temp = float(input(f"Enter temperatur of Day {i + 1} : "))
        temperatures.append(temp)

    total_temp = sum(temperatures)
    avg_temp = total_temp / days

    if avg_temp > 30:
        weather_status = "Hot"
    elif avg_temp > 20:
        weather_status = "Moderate"
    else:
        weather_status = "Cold"


    print("\n--- Summary Report ---")
    print(f"Data Points Recorded: {days}")
    print(f"Highest Temperature: {max(temperatures)}°C")
    print(f"Lowest Temperature: {min(temperatures)}°C")
    print(f"Average Temperature: {avg_temp:.2f}°C") # .2f formats to 2 decimal places
    print(f"Weather Verdict: {weather_status}")


if __name__ == "__main__":
    main()