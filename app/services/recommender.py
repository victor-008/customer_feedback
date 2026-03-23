def recommend(problem):

    if not problem:
        return None

    problem = problem.lower()

    rules = {

        "internet": "Check bandwidth allocation",

        "router": "Restart router and check firmware",

        "network": "Reset switch and check cables",

        "power": "Check transformer and supply line",

        "server": "Restart server service",

        "connection": "Check ISP link",

        "slow": "Increase bandwidth",

        "overload": "Reduce load or upgrade system",
    }

    for key in rules:

        if key in problem:

            return rules[key]

    return "Further investigation required"