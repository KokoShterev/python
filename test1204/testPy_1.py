def calculate(build_price, sell_price, volume):
    return (sell_price - build_price) * volume

build_price, sell_price, volume = map(float, input().split())
print(f'{calculate(build_price, sell_price, volume):.0f}')