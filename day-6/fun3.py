def dis_price(price, discount):
    dis = price * (discount / 100)
    return price - dis


# a상품: 10000원, 10% 할인
price_a = dis_price(10000, 10)
print(f"a 상품: {int(price_a)}원")

# b 상품: 50000원, 20% 할인
price_b = dis_price(50000, 20)
print(f"b 상품: {int(price_b)}원")