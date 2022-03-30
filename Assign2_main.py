# name: Shenghua He
# student number: 251016121
# project: Assignment 2 - main.py
# class: CS1026A 002 SU21
# professor: Duff Jones
# project description: This project allow users to input shapes (3 in total), and shape dimensions. Outputting volumes in sorted orders.

# import volumes to let functions in volumes able to be used
import volumes


# input function in normal circumstances
def normal_inputting():
    origin_input = str(input('Please enter shape (quit/q, cylinder/c, prism/p, sphere/s): '))
    return origin_input


# inputting function when invalid shape entered
def after_error_inputting():
    origin_input = str(input('Please enter shape: '))
    return origin_input


# when cylinder entered, asking height and radius, return in tuple to be put in list
def cylinder_dimensions_and_calculation():
    height = float(input("Enter height of the cylinder: "))
    radius = float(input("Enter radius of the cylinder: "))
    # calculating volume, functions in volumes.py
    volume = volumes.volume_of_a_cylinder(radius, height)
    print("The volume of a cylinder with height %.1f and radius %.1f is: %7.2f." % (height, radius, volume))
    # return in a tuple
    return "cylinder", volume


# when prism entered, asking length, width ,and height. return in tuple to be put in list
def prism_dimensions_and_calculation():
    length = float(input("Enter length of the rectangular prism: "))
    width = float(input("Enter width of the rectangular prism: "))
    height = float(input("Enter height of the rectangular prism: "))
    # calculating volume, functions in volumes.py
    volume = volumes.volume_of_a_rectangular_prism(length, width, height)
    print("The volume of a rectangular prism with length %.1f, width %.1f and height %.1f is: %7.2f." % (length, width, height, volume))
    # return in a tuple
    return "prism", volume


# when prism entered, asking radius, return in tuple to be put in list
def sphere_dimensions_and_calculation():
    radius = float(input("Enter the sphere's radius: "))
    # calculating volume, functions in volumes.py
    volume = volumes.volume_of_a_sphere(radius)
    print("The volume of a sphere with radius %.1f is: %7.2f." % (radius, volume))
    # return in a tuple
    return "sphere", volume


# main function that gives all processing logics
def main():
    volume_list = []  # creating a list
    type_end = False  # to start and end a while loop
    entered_shape = ""  # to determine whether a valid shape is entered before
    error = False  # to determine whether using normal inputting function or after_error_inputting function
    # loop start, asking user to enter
    while not type_end:
        if not error:
            # normal_inputting function see above
            origin_input = normal_inputting()
        else:
            # after_error_inputting function see above
            origin_input = after_error_inputting()
            error = False  # default the error boolean
        lower_input = origin_input.lower()  # lowercase the input
        if lower_input == "quit" or lower_input == "q":
            # judge if there is a valid shape entered before
            if entered_shape != "":  # if there was a valid input, end loop
                break
            else:
                print("Output: No shapes entered")  # if no valid input, print as seen
                break
        # if valid input determined
        elif lower_input == "cylinder" or lower_input == "c":
            tuple_result = cylinder_dimensions_and_calculation()  # function returns tuple_result
            volume_list.append(tuple_result)  # append tuple into list
            entered_shape = " "  # valid shape is entered
        elif lower_input == "prism" or lower_input == "p":
            tuple_result = prism_dimensions_and_calculation()  # function returns tuple_result
            volume_list.append(tuple_result)  # append tuple into list
            entered_shape = " "  # valid shape is entered
        elif lower_input == "sphere" or lower_input == "s":
            tuple_result = sphere_dimensions_and_calculation()  # function returns tuple_result
            volume_list.append(tuple_result)  # append tuple into list
            entered_shape = " "  # valid shape is entered
        # if invalid shape is entered
        else:
            print("  -- invalid input: enter (quit/q, cylinder/c, prism/p, sphere/s)")
            error = True  # use after_error_inputting function
    # ensure empty list print nothing
    if len(volume_list) != 0:
        volume_list.sort(key=lambda my_list: my_list[1])  # sort list
        print("Output: Volumes of shapes entered in sorted order: ")
        position = 0  # determine print process in list elements
        while position < len(volume_list):
            print("%s %.2f" % (volume_list[position][0], volume_list[position][1]))
            position += 1


# run main function
if __name__ == '__main__':
    main()
