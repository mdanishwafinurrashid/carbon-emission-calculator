from data.factors import Activities

def calculate_emission(Activity,value):
    factor = Activities[Activity]["Factors"]
    emission = factor * value
    return emission

#will get the input from calculate_emission function
def calculate_total_emission(data):
    
    total = 0

    for activity, value in data.items():
        emission = calculate_emission(activity, value)
        total += emission
    return total


def category_breakdown(data):

    breakdown = {
        "Transportation": 0,
        "Electricity": 0,
        "Digital": 0
    }

    for activity, value in data.items():

        emission = calculate_emission(activity, value)
        category = Activities[activity]["Category"]
        breakdown[category] += emission
    return breakdown

#Determine the level of severeness based on total
def severity_level(total):
    
    if total <= 5:
        return "Low"
    elif total <= 10 :
        return "Moderate"
    elif total <= 15 :
        return "High"
    else :
        return "Severe"

#Suggestion based on the highest factor
def get_suggestions(breakdown):

    highest_category = max(breakdown, key=breakdown.get)

    if highest_category == "Transportation":
        return [
            "Use public transport like bus or train",
            "Carpool with friends",
            "Walk or cycle for short distances"
        ]

    elif highest_category == "Electricity":
        return [
            "Reduce air conditioner usage",
            "Turn off unused appliances",
            "Use energy-efficient devices"
        ]

    elif highest_category == "Digital":
        return [
            "Reduce streaming time",
            "Lower screen brightness",
            "Enable power-saving mode"
        ]
