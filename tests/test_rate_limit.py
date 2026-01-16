import sys
import os
sys.path.append(os.getcwd())
from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)

def test_rate_limiting():
    # Helper to simulate many requests
    # Limit is 120/minute. We will try 122 requests.
    
    # Reset limiter for test client? 
    # TestClient shares the same app instance, but we need to ensure unique IP or just hit it hard.
    # TestClient uses "testclient" as host/ip usually.
    
    # We need to make sure we don't hit the limit from previous tests if any.
    # But since we are fresh, it should be 0.
    
    limit = 120
    # Hit it up to the limit
    for i in range(limit):
        response = client.get("/")
        assert response.status_code == 200, f"Request {i+1} failed with {response.status_code}"
    
    # The next one should fail
    response = client.get("/")
    assert response.status_code == 429, f"Rate limit not triggered on request {limit+1}"
    
    data = response.json()
    assert "error" in data
    # Standard slowapi response usually has {"error": "Rate limit exceeded: ..."}
    # But checking status code is most important.

if __name__ == "__main__":
    try:
        test_rate_limiting()
        print("Rate Limit Test: PASS")
    except AssertionError as e:
        print(f"Rate Limit Test: FAIL - {e}")
    except Exception as e:
        print(f"Rate Limit Test: ERROR - {e}")
