api_requests = [
    {"id": 101, "status": "success", "tokens": 120},
    {"id": 102, "status": "failed", "tokens": 0},
    {"id": 103, "status": "success", "tokens": 350},
    {"id": 104, "status": "failed", "tokens": 0}
]
total_request_tokens = 0
for request in api_requests:
    if request["status"] == "success":
        total_request_tokens += request["tokens"]
    elif request["status"] == "failed":
        print(f"Alert: Request id: {request["id"]} is failed ")

print(f" Total successful token precess is ={total_request_tokens}")
