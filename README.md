# OpenResty + Python DDoS Protection Sandbox

This is a sandbox demo showing how to limit requests per second (RPS) for users in a backend system using **OpenResty (Nginx + Lua)**

---

## Scenario / Motivation

- The system may have **compromised users**.  
- Even with correct login credentials, an attacker could **flood endpoints**.  
- Using a simple Lua **RPS throttling**, we can protect the system from overload.  
- This demo highlights **backend resilience**, not full security auditing.

---

## Architecture

- **Python backend**: Flask app exposing `/`, `/echo`, `/health`.  
- **OpenResty frontend**: Proxies requests to Python backend.  
- **Lua RPS limiter**:
  - Configured for a single location (`/`).
  - Limits requests per user login.
  - Memory reserved per key: **1MB**.
- **Load testing**: Demonstrated with `hey` tool to simulate `429 Too Many Requests` responses.

### Key files

- `python/Dockerfile` – Python backend image  
- `python/app.py` – Flask app  
- `openresty/nginx.conf` – main OpenResty config  
- `openresty/conf.d/default.conf` – server block with Lua RPS limiter  
- `docker-compose.yml` – sets up Python + OpenResty + network

---

## Quickstart / How to run

```bash
# Build and run containers
docker compose up -d --build

# Python backend on port 5000 (optional, direct access)
curl http://localhost:5000

# OpenResty on port 8080 with RPS limiting
curl -H "login: user1" http://localhost:8080/

# Simulate high load with hey
hey -z 10s -q 20 -H "login: user1" http://localhost:8080/