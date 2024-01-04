def is_triangle(measure):
    if  (measure[0]+measure[1]>measure[2] and 
         measure[0]+measure[2]>measure[1] and 
         measure[1]+measure[2]>measure[0]):
        return True
    return False

def inf_triang(measure):
    if (measure[0] == measure[1] and 
        measure[1] == measure[2]):
        return 'Equilateral'
    elif (measure[0] == measure[1] or 
         measure[0] == measure[2] or
         measure[1] == measure[2]):
        return 'Isosceles'
    return 'Scalene'

if __name__ == "__main__":
    tri_meas = []
    for i in range(1,4):
        tri_meas.append(float(input(f'Input the {i}° triangle side:')))

    if is_triangle(tri_meas):
        print(inf_triang(tri_meas))