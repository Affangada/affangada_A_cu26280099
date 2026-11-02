"""Python Set Operations Lab Sheet 06 solution."""
s = {1, 2, 3}
elements = list(s)
power_set = [set()]
for item in elements:
    power_set += [subset | {item} for subset in power_set]
print("Set:", s)
print("Power set:", power_set)
print("Number of subsets:", len(power_set))
