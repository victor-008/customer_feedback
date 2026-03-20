KB = {

    "internet": "Check router, check bandwidth, restart modem",

    "power": "Inspect feeder, check transformer, check breaker",

    "network": "Check switch, restart server",

    "water": "Check valve, inspect pipe"

}

def recommend(problem: str):

    if not problem:
        return None
    for key in KB:
        if key in problem:
            return KB[key]
        
    return "Further inspection required"