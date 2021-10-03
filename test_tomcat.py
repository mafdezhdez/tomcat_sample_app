import pytest
import requests

def test_tomcat():
    r = requests.get('http://localhost:8080/sample', timeout=10)
    assert r.status_code == 200
