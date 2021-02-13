from .models import Product


def get_length():
    number = Product.objects.raw('SELECT 1 as id, product_type_name, count(*) as num from shoppinghome_product group by product_type_name')

    return number