def main():

    num_sides = int(input("Enter number of sides:"))

    EA = 360 // num_sides
    IA = 180 - EA

    print("The exterior angles are", EA , "and the interior angles are", IA)

    
    return

if __name__ == '__main__':
    main()