from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    query = """
        mutation MyMutation {
            addUser(
                userData: {
                name: "Silvia Armah", 
                email: "sarmah@mail.com", 
                address: "POB1", 
                phoneNumber: "0249", 
                sex: "female"
            }) {
                id
                name
                address
            }
        }
    """
    response = client.post("/graphql", json={"query": query})
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert result["data"]["addUser"]["name"] == "Silvia Armah"
    assert result["data"]["addUser"]["address"] == "POB1"


def test_get_user_list(user):
    query = """
        query {
            users {
                name 
                email
                address
            }
        }
    """
    response = client.post("/graphql", json={"query": query})
    print("Response", response)
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert type(result["data"]["users"]) == list
    assert result["data"]["users"][0]["name"] == user.name


def test_get_single_user(user):
    query = """
        query {
            getSingleUser(userId: %s) {
                name 
                email
                address
            }
        }
    """ % user.id
    response = client.post("/graphql", json={"query": query})
    print("Response", response)
    assert response is not None
    assert response.status_code == 200

    result = response.json()
    assert type(result["data"]["getSingleUser"]) == dict
    assert result["data"]["getSingleUser"]["name"] == user.name
