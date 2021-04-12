def sqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

print(sqrt(25.0))
# print(sqrt(49.0))
# print(sqrt(81.0))