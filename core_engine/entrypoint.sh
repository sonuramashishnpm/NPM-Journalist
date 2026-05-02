#!/bin/bash
set -e

echo "Starting Process"
exec python3 -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-7860}
