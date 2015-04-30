 def forecast(days):
    result = []
    counter_sunshine = 0
    counter_snow = 0
    counter_rain = 0
    
    for day in days:
        if day == "sunshine":
            counter_sunshine += 1

        elif day == "rain":
            counter_rain += 1

        elif day == "snow":
            counter_snow += 1

    if counter_snow > counter_sunshine and counter_snow > counter_rain:
        result += ["snow"]

    elif counter_sunshine > counter_snow and counter_sunshine > counter_rain:
        result += ["sunshine"]

    elif counter_rain > counter_sunshine and counter_rain > counter_snow:
        result += ["rain"]

    elif counter_rain == counter_snow:
        result += ["sunshine"]
    elif counter_snow == counter_sunshine:
        result += ["rain"]

    elif counter_sunshine == counter_rain:
        result += ["snow"]

    elif counter_sunshine == counter_rain and counter_rain == counter_show:
        result += [len(days) - 1]
    


        



    return result
        
days = ["snow", "snow", "rain", "sunshine"]
print(forecast(days))

days = ["rain", "rain", "sunshine", "sunshine"]
print(forecast(days))

days = ["rain", "rain", "snow", "snow", "sunshine", "sunshine"]
print(forecast(days))

