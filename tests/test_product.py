def test_product_init(first_product):
    assert first_product.name == 'Oppo'
    assert first_product.description == 'Быстрый флагман'
    assert first_product.price == 34.999
    assert first_product.quantity == 4