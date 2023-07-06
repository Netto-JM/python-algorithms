def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    result = 0
    if target_time is None or target_time <= 0:
        return None
    for period in permanence_period:
        if any(not isinstance(x, int) for x in period):
            return None
        if period[0] <= target_time <= period[1]:
            result += 1
    return result
