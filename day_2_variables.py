
def snake_case():
    # let's talk about coding conventions

    this_is_snake_case = 'good'
    thisIsCamelCase = 'not allowed'
    YouSeeThisInCPlusPlusSometimes = 'also bad for python'

    counter = 0  # probably meaningful
    total_cost = 5.00  # snake case and meaningful
    median_value = 212  # legal and meaningful
    x = 17  # not meaningful but technically snake_case, avoid

    print(this_is_snake_case, thisIsCamelCase, YouSeeThisInCPlusPlusSometimes, counter,
          total_cost, median_value, x)


def input_example():
    argument_of_input = 'hello'

    variable_name = input(argument_of_input)

    print(variable_name)

    in_string = input('Enter some input: ')
    # just to ensure no unused variable warning for in_string
    in_string += 'hello'

    number_of_robots = int(input('Enter the number of robots: '))
    amount_of_water = float(input('Enter the amount of water in ml: '))
    is_it_really = bool(input('Really? Enter True or False: '))
    # We don't need to cast this one.
    password = input('Enter Password: ')

    print(number_of_robots, amount_of_water, is_it_really, password)


def circle_example():
    # An extra space allows us to enter the radius without it directly touching the colon.
    in_string = input('Enter a radius: ')
    # Remember here that we need to cast from string to float, because input takes in strings.
    radius = float(in_string)
    area = 3.14159265358979 * radius * radius  # or radius ** 2
    circumference = 2 * 3.14159265358979 * radius
    print('A circle with radius', radius, 'will have area', area, 'and circumference', circumference)


def schwarzchild_radius():
    # This means 6.67 * (10 ** -11), written in engineering scientific notation.
    GRAV_CONSTANT = 6.67E-11
    SPEED_OF_LIGHT = 299792458
    mass = float(input('Enter the mass of the black hole: '))
    radius = 2 * GRAV_CONSTANT * mass / SPEED_OF_LIGHT ** 2
    print('The Schwarzchild radius of the blackhole is: ', radius)


def casting_examples():
    string_five = '5'
    int_eight = int(string_five) + 3
    # Note that they print the same way.
    print(int_eight, int(string_five), string_five)

    golden_ratio = (1 + 5 ** (1/2)) / 2
    print(golden_ratio, str(golden_ratio))

    true_or_false = False
    the_result = 'The result is ' + str(true_or_false)
    # print will cast primitive types into strings automatically.
    print(true_or_false, the_result)
    # Here are a number of things which convert into strings in the print function.
    print(True, False, None, 1, 1.25)


# circle_example()
# input_example()
# schwarzchild_radius()
casting_examples()
