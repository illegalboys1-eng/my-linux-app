# tests/test_app.py
import requests
import subprocess
import time
import pytest

def test_server_responds():
    """Test that the server returns 200 OK"""
    # Start the server in background
    proc = subprocess.Popen(["python3", "app.py"])
    time.sleep(1)    # Give it a second to start

    try:
        response = requests.get("http://localhost:5000")
        assert response.status_code == 200
        assert b"Hello" in response.content
    finally:
        proc.terminate()

def test_response_content():
    """Test that response contains expected text"""
    proc = subprocess.Popen(["python3", "app.py"])
    time.sleep(1)

    try:
        response = requests.get("http://localhost:5000")
        assert b"Docker" in response.content
    finally:
        proc.terminate()
