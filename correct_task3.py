from typing import List, Any

def average_valid_measurements(measurements: List[Any]) -> float:
    # Input validation: ensure measurements is a list
    if not isinstance(measurements, list):
        return 0.0

    total_sum = 0.0           # Sum of valid measurements
    valid_count = 0           # Number of valid measurements

    for measurement in measurements:
        if measurement is None:
            continue
        try:
            numeric_value = float(measurement)
            total_sum += numeric_value
            valid_count += 1
        except (TypeError, ValueError):
            continue

    # Avoid division by zero
    return total_sum / valid_count if valid_count > 0 else 0.0
