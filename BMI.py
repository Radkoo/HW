#weight_in_kilogram = W
#height_in_meters = H
W = int(input('Enter weight in kilograms: '))
#print(W)
H = float(input('Enter height in meters:  '))
#print(H)
BMI = (W/(H*H))
res = round(BMI,2)
print('Your body mass index is' , res )


