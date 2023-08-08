length=int(input())
width=int(input())
higth=int(input())
percent_sand=float(input())

volume=length*width*higth /1000
litres = volume - volume*percent_sand/100

print(litres)