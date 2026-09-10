# =====================================================================
# DAY 21 REVIEW: COMPREHENSIONS & DYNAMIC ARGUMENTS
# =====================================================================

# 1. List & Dictionary Comprehensions
transactions = [
    {"id": 1, "amount": 250.0, "category": "Food"},
    {"id": 2, "amount": 1200.0, "category": "Tech"},
    {"id": 3, "amount": 450.0, "category": "Food"},
    {"id": 4, "amount": 80.0, "category": "Transport"}
]

# Extract food amounts
food_amounts = [t["amount"] for t in transactions if t["category"] == "Food"]

# Map transaction ID to amount for high-value transactions
high_value_map = {t["id"]: t["amount"] for t in transactions if t["amount"] > 200.0}

print(f"Food Amounts: {food_amounts}")
print(f"High Value Map: {high_value_map}\n")


# 2. Flexible Function Arguments (*args, **kwargs)
def log_event(event_name: str, *tags: str, **metadata: str) -> None:
    print(f"Event Name: {event_name}")
    print(f"Tags (Tuple): {tags}")
    print(f"Metadata (Dict): {metadata}")

if __name__ == "__main__":
    log_event("USER_LOGIN", "auth", "security", user_id="101", status="success")