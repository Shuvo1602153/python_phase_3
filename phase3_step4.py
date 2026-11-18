def calculate_llm_cost(total_tokens,cost_per_1000_tokens=.002):
    return (total_tokens/1000)* cost_per_1000_tokens

api_requests = [
    {"id": 101, "status": "success", "tokens": 120},
    {"id": 102, "status": "failed", "tokens": 0},
    {"id": 103, "status": "success", "tokens": 350},
    {"id": 104, "status": "failed", "tokens": 0}
]

used_tokens = 0
for request in api_requests:
    if request["status"] == "success":
        used_tokens += request["tokens"]
    else:
        print(f" Alert: Your requested id : {request["id"]} is failed  and Used token is 0")

print(f"Your Total used token is: {used_tokens} and total cost = {calculate_llm_cost(used_tokens)}$ ")

