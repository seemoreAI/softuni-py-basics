from math import floor
record_seconds = float(input())
rastoianie_metres = float(input())
seconds_za_edin_metar = float(input())

zabaviyane = floor(rastoianie_metres / 50) * 30
vreme = seconds_za_edin_metar * rastoianie_metres + zabaviyane

if vreme < record_seconds:
    print(f"Yes! The new record is {vreme:.2f} seconds.")
else:
    print(f"No! He was {vreme - record_seconds:.2f} seconds slower.")