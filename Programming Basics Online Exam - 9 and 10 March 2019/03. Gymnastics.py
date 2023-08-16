country = input()
tool = input()
mark = 0

if country == "Russia":
    if tool == "ribbon":
        mark = 9.100 + 9.400
    elif tool == "hoop":
        mark = 9.300 + 9.800
    elif tool == "rope":
        mark = 9.600 + 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        mark = 9.600 + 9.400
    elif tool == "hoop":
        mark = 9.550 + 9.750
    elif tool == "rope":
        mark = 9.500 + 9.400
elif country == "Italy":
    if tool == "ribbon":
        mark = 9.200 + 9.500
    elif tool == "hoop":
        mark = 9.450 + 9.350
    elif tool == "rope":
        mark = 9.700 + 9.150

print(f"The team of {country} get {mark:.3f} on {tool}.")
print(f"{(20-mark)*5:.2f}%")
