score_map = {
    "AUTH": 10,
    "CHANNEL": 10,
    "MODE": 10,
    "DISCONNECT": 10
}

results = {}

def set_result(section, status, reason=""):
    results[section] = {score_map = {
    "AUTH": 10,
    "CHANNEL": 10,
    "MODE": 10,
    "DISCONNECT": 10
}

results = {}

def set_result(section, status, reason=""):
    results[section] = {
        "status": status,
        "reason": reason
    }

def compute_score():
    total = 0
    for k, v in results.items():
        if v["status"] == "PASS":
            total += score_map[k]
        elif v["status"] == "PARTIAL":
            total += score_map[k] // 2
    return total
        "status": status,
        "reason": reason
    }

def compute_score():
    total = 0
    for k, v in results.items():
        if v["status"] == "PASS":
            total += score_map[k]
        elif v["status"] == "PARTIAL":
            total += score_map[k] // 2
    return total