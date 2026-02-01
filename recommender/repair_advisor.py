def recommend_repairs(detections):
    advice = set()

    for d in detections:
        t = d["type"]
        if t == "crack":
            advice.add("Apply crack filler and repaint")
        elif  t == "hole":
            advice.add("Use wall putty and sanding")
        elif t == "damp":
            advice.add("Fix leakage and waterproof")
        elif t == "mold":
            advice.add("Use anti-fungal treatment")
        elif t == "peeling":
            advice.add("Scrape and repaint")
        else:
            advice.add("General inspection recommended")
    return list(advice)
