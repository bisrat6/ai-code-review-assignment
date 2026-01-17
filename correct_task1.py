from typing import List, Dict, Any

def calculate_average_order_value(orders: List[Dict[str, Any]]) -> float:
    if not isinstance(orders, list):
        return 0.0
    
    total = 0
    count = 0

    for order in orders:
        # Skip invalid items
        if not isinstance(order, dict):
            continue
        # We only care about orders that aren't cancelled
        if order.get('status') == 'cancelled':
            continue
            
        try:
            # If 'amount' is missing or not a number, float() will raise an error
            total += float(order['amount'])
            count += 1
        except (KeyError, ValueError, TypeError):
            # Skip missing keys or invalid data types
            continue

    return total / count if count > 0 else 0.0