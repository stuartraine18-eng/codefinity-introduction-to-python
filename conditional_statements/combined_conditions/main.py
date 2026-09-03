# The item's discount and stock status have been defined
discounted = True
lowStock = False

movingProduct = discounted or lowStock
promotion = not discounted and lowStock

print("is the item eligible for promotion?", promotion)