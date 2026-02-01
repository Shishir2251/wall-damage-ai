from cost_engine.country_rates import COUNTRY_RATES

def calculate_cost(detections, country):
    rates = COUNTRY_RATES.get(country, COUNTRY_RATES["Bangladesh"])
    total=0

    for d in detections:
        rate = rates.get(d["type"],2.0)
        total += d["area"]* rate

    return round(total,2)