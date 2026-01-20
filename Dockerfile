# Root Dockerfile - Railway fallback
# Actual builds use service-specific contexts from railway.toml
# This file ensures Railway can find a Dockerfile at the root level

FROM alpine:3.18

WORKDIR /app

# Placeholder - Railway should use ./backend/Dockerfile or ./frontend/Dockerfile
# based on the service build context in railway.toml or Railway dashboard

CMD ["echo", "Use service-specific Dockerfiles: ./backend/Dockerfile or ./frontend/Dockerfile"]
