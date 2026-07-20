import pytest
from app import app, BASE_DIR
from services.data_service import load_metric_api_data

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

# 1. /health 返回200
def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["ok"] == True

# 2. 未登录访问 /api/metrics 被拦截
def test_metrics_no_login(client):
    resp = client.get("/api/metrics")
    # 未登录跳转到登录页，302重定向
    assert resp.status_code == 302

# 3. 登录后 /api/metrics 返回ok、metrics
def test_metrics_login(client):
    # 模拟登录
    client.post("/login", data={"username":"student", "password":"day07"})
    resp = client.get("/api/metrics")
    data = resp.get_json()
    assert data["ok"] == True
    assert "metrics" in data
    assert len(data["metrics"]) > 0

# 4. /api/categories?category=Fashion 返回筛选数据
def test_categories_fashion(client):
    client.post("/login", data={"username":"student", "password":"day07"})
    resp = client.get("/api/categories?category=Fashion")
    data = resp.get_json()
    assert data["ok"] == True
    assert data["category"] == "Fashion"
    assert isinstance(data["rows"], list)