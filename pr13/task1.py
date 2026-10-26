import math

NAME = "Nazar"
SURNAME = "MIschuck"
GROUP = "IT-32"

LENGTH = 4.2   
WIDTH = 3.5    
HEIGHT = 2.7   
DOOR_W = 0.9
DOOR_H = 2.0
WINDOW_W = 1.4
WINDOW_H = 1.5
TILE_SIDE = 0.30      
TILE_PRICE = 42.30    


PAINT_PER_M2 = 0.1    
LAYERS = 2
CAN_VOLUME = 2.5      #
SPARE = 1.10          

print(f"{NAME} {SURNAME}, {GROUP}")


floor_area = LENGTH * WIDTH
walls_full = 2 * (LENGTH + WIDTH) * HEIGHT
wall_area = walls_full - DOOR_W * DOOR_H - WINDOW_W * WINDOW_H


floor_diag = math.hypot(LENGTH, WIDTH)
room_diag = math.dist((0, 0, 0), (LENGTH, WIDTH, HEIGHT))


tile_area = TILE_SIDE * TILE_SIDE
tiles_exact = floor_area / tile_area
tiles_to_buy = math.ceil(tiles_exact * SPARE)  


paint_liters = wall_area * PAINT_PER_M2 * LAYERS
cans = math.ceil(paint_liters / CAN_VOLUME)

cost_mul = tiles_to_buy * TILE_PRICE
cost_sum = 0.0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE
difference = abs(cost_sum - cost_mul)

print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")
print()
print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")
print(f"paint:         {paint_liters:.2f} l -> {cans} cans of {CAN_VOLUME} l")
print()
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {difference}")
