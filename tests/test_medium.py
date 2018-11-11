def test_get_medium(client):
    data = {"url": "https://medium.com/s/story/rules-for-resters-809e368c0fdb"}
    resp = client.post('api/v1/medium/articles', json=data)
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'm4a' in data['mp4']