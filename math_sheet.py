import math

import sympy

header = '\n******** Welcome to the math sheet *********.'
print(header)
print('~' * len(header))


def math_sheet():
    '''A simple volume calculator for practice in dealing with exceptions'''
    print('\nChoose your calculation...\n'
          '\n1. circle area \n2. pyramid volume \n3. prism volume \n4. cylinder volume '
          '\n5. cone volume \n6. sphere volume\n')

    def circle_area():
        while True:
            try:
                radius = float(input('\nTo calculate the area of a circle enter the radius: '))
                circle_area = math.pi * radius ** 2
                print(f'\nThe area of a circle with a radius of {radius} = {circle_area.__round__(2)}²')
                math_sheet()
            except ValueError:
                print('Invalid input. Try again')

    def pyramid_vol():
        print \
            (
                '\nA pyramid is a polyhedron formed by connecting a polygonal base and an apex. The basic formula for pyramid '
                '\nvolume is the same as for a cone: volume = (1/3) * base_area * height, where height is the height from'
                '\nthe base to the apex. '
                '\n\nThat formula is working for any type of base polygon and oblique and right pyramids. All you need to '
                '\nknow are those two values - base area and height. However, there are other useful formulas, in case you '
                '\ndon\'t know the base area. For any pyramid with a regular base, you can use the equation: '
                '\nvolume = (n/12) * height * side_length² * cot(π/n), where n is number of sides of the base for regular polygon')
        base_shape()

    def base_shape():
        pyramid_base_shape = ''
        while True:
            try:
                pyramid_base_shape = int (input(
                    '\nDoes the base of the pyramid have even sides (press 1), is it a rectangle (press 2) or an '
                    'isocelies triangle (press 3): ').upper())
            except ValueError:
                print('Invalid input. Try again')

            if pyramid_base_shape == 1:
                while True:
                    try:
                        pyramid_num_sides = int(input('\nHow many sides does the pyramid have?: '))
                        pyramid_side_length = float(input('Enter the side length: '))
                        pyramid_height = float(input('Enter the height of the pyramid: '))
                        pyramid_vol = (pyramid_num_sides / 12) * pyramid_height * pyramid_side_length ** 2 * sympy.cot(
                            math.pi / pyramid_num_sides)
                        print(f'\nThe volume of the pyramid is {pyramid_vol.__round__(2)} cu')
                        math_sheet()
                    except ValueError:
                        print('Invalid input. Try again')

            elif pyramid_base_shape == 2:
                while True:
                    try:
                        base_len = int(input('Enter the length of the base: '))
                        base_width = int(input('Enter the width of the base: '))
                        area_of_base = base_len * base_width
                        height = (int(input('Enter the height of the pyramid: ')))
                        vol_pyramid = (area_of_base * height) / 3
                        print(f'\nThe volume of the pyramid is {vol_pyramid.__round__(2)}²')
                        math_sheet()
                    except ValueError:
                        print('Invalid input. Try again.')

            elif pyramid_base_shape == 3:
                while True:
                    try:
                        base_len = int(input('\nEnter the length of one long side of the triangle base: '))
                        base_width = int(input('Enter the length of one short side of the triangle base: '))
                        area_of_base = (base_len * base_width) / 2
                        height = (int(input('Enter the height of the pyramid: ')))
                        vol_pyramid = (area_of_base * height) / 3
                        print(f'\nThe volume of the pyramid is {vol_pyramid.__round__(2)} cu')
                        math_sheet()
                    except ValueError:
                        print('Invalid input. Try again.')

    def prism_vol():
        while True:
            try:
                prism_base_area = int(input('\nEnter the area of one end of the prism: '))
                prism_len = int(input('Enter the length of the prism: '))
                prism_vol = prism_base_area * prism_len
                print(f'\nThe volume of the prism is {prism_vol.__round__(2)} cu')
                math_sheet()
            except ValueError:
                print('Invalid input. Try again')

    def cylinder_vol():
        while True:
            try:
                print('''\ncylinder_volume = π * cylinder_radius² * cylinder_height''')
                cylinder_radius = int(input('\nEnter the cylinder radius: '))
                cylinder_height = int(input('Enter the cylinder height: '))
                cylinder_vol = math.pi * cylinder_radius ** 2 * cylinder_height
                print(f'\nThe volume of the cylinder is {cylinder_vol.__round__(2)} cu')
                math_sheet()
            except ValueError:
                print('Invalid input. Try again')

    def cone_vol():
        print('\nA cone is a solid that has a circular base and a single vertex. To calculate its volume you need to '
              '\nmultiply the base area (area of a circle: π * r²) by height and by 1/3: volume = (1/3) * π * r² * h')
        while True:
            try:
                cone_radius = int(input('\nEnter the radius of the cone base: '))
                cone_height = int(input('Enter the height of the cone: '))
                cba = math.pi * cone_radius ** 2
                cone_vol = cba * cone_height / 3
                print(f'\nThe volume of the cone is {cone_vol.__round__(2)} cu')
                math_sheet()
            except ValueError:
                print('Invalid input. Try again')

    def sphere_vol():
        print(
            '\nA sphere is a perfectly round geometrical 3D object. The formula for its volume equals: volume = (4/3) * π * r³ '
            '\nUsually, you don\'t know the radius - but you can measure the circumference of the sphere instead, e.g., '
            '\nusing the string or rope. The sphere circumference is the one-dimensional distance around the sphere '
            '\nat its widest point. circumference = 2 * π * r, so r = circumference / (2 * π)')
        while True:
            try:
                sphere_circum = input('\nEnter the circumference of the sphere: ')
                sphere_circum = float(sphere_circum)
                sphere_radius = sphere_circum / (2 * math.pi)
                sphere_vol = sphere_radius ** 3 * 1.3333333333333 * math.pi
                print(f'\nThe volume of the sphere is {sphere_vol.__round__(2)} cu')
                math_sheet()
            except ValueError:
                print('Invalid input. Try again')

    choice = ''
    while choice not in range(1, 6):
        try:
            choice = int(input('choose 1 - 6: '))
            if choice not in range(1, 7):
                print('Invalid entry. Try again')
            else:
                if choice == 1:
                    circle_area()
                elif choice == 2:
                    pyramid_vol()
                elif choice == 3:
                    prism_vol()
                elif choice == 4:
                    cylinder_vol()
                elif choice == 5:
                    cone_vol()
                elif choice == 6:
                    sphere_vol()
        except:
            print('Invalid entry. Try again')


math_sheet()
