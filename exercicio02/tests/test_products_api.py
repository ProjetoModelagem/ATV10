import requests

BASE_URL = "https://fakestoreapi.com/products"

def test_listar_produtos():
    r = requests.get(BASE_URL)
    assert r.status_code == 200
    produtos = r.json()
    assert len(produtos) > 0
    assert "title" in produtos[0]

def test_buscar_produto_por_id():
    r = requests.get(f"{BASE_URL}/1")
    assert r.status_code == 200
    produto = r.json()
    assert "title" in produto
    assert produto["id"] == 1

def test_filtrar_por_categoria():
    categoria = "electronics"
    r = requests.get(f"{BASE_URL}/category/{categoria}")
    assert r.status_code == 200
    assert all(p["category"] == categoria for p in r.json())
