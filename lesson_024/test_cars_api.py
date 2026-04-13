import pytest
import requests
import logging

BASE_URL = "http://127.0.0.1:8080"

# Logging
logger = logging.getLogger("api_tests")
logger.setLevel(logging.INFO)

# Format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Fail
file_handler = logging.FileHandler("lesson_024/test_search.log" , encoding="utf-8")
file_handler.setFormatter(formatter)

# Consol
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Fixture
@pytest.fixture(scope="class")
def auth_token():
    logger.info("Auth...")

    response = requests.post(
        f"{BASE_URL}/auth",
        auth=("test_user", "test_pass")
    )

    assert response.status_code == 200, "Auth failed"

    token = response.json()["access_token"]
    logger.info(f"Got token: {token}")

    return token


# 🔹 Tests class
@pytest.mark.usefixtures("auth_token")
class TestCarsSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 4),
        ("price", 10),
        ("year", None),
    ])
    def test_get_cars(self, auth_token, sort_by, limit):
        logger.info(f"Тест: sort_by={sort_by}, limit={limit}")

        headers = {"Authorization": f"Bearer {auth_token}"}

        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = requests.get(f"{BASE_URL}/cars", headers=headers, params=params)

        logger.info(f"Status code: {response.status_code}")
        assert response.status_code == 200
        data = response.json()
        logger.info(f"Auto numbers: {len(data)}")

        # 🔹 Check limit
        if limit:
            assert len(data) <= limit

        # 🔹 Check sorting
        if sort_by:
            values = [car.get(sort_by, 0) for car in data]
            assert values == sorted(values), "Sorting failed"

        logger.info("TEST DONE SUCCESSFUL")
