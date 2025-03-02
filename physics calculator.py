def average_speed(distance,time):
    return distance / time

def acceleration(Δv,Δt):
    return Δv/Δt

def density(mass, volume):
    return mass / volume

def power(work, time):
    return work / time

def newtons_second_law(mass, acceleration):
    return mass * acceleration

def weight(mass, gravity=9.8):
    return mass * gravity

def pressure(force, area):
    return force / area

def ohms_law(current, resistance):
    return current * resistance

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def frequency(velocity, wavelength):
    return velocity / wavelength

def pendulum(length, gravity=9.8):
    import math
    return 2 * math.pi * math.sqrt(length / gravity)

def fahrenheit(celsius):
    return (9/5 * celsius) + 32

def work(force, distance, angle):
    import math
    return force * distance * math.cos(math.radians(angle))

def torque(force, radius, angle):
    import math
    return force * radius * math.sin(math.radians(angle))

def displacement(final_position, initial_position):
    return final_position - initial_position

def mass(force, acceleration):
    return force / acceleration

##############################################################

current_page = 0

while True:
    if current_page == 0:
        print("\nWelcome to the Physics Calculator!")
        print("Z. Next Page")
        print("Q. Quit")
    elif current_page == 1:
        print("\nPage 1 - Select operation:")
        print("1. Average Speed")
        print("2. Acceleration")
        print("3. Density")
        print("4. Power")
        print("5. Newton's Second Law")
        print("6. Weight")
        print("7. Pressure")
        print("8. Ohm's Law")
        print("Z. Next Page")
        print("X. Previous Page")
        print("Q. Quit")
    elif current_page == 2:
        print("\nPage 2 - Select operation:")
        print("9. Kinetic Energy")
        print("10. Frequency")
        print("11. Pendulum Period")
        print("12. Fahrenheit Conversion")
        print("13. Work")
        print("14. Torque")
        print("15. Displacement")
        print("16. Mass")
        print("X. Previous Page")
        print("Q. Quit")
        
##############################################################

    option = input("Enter your option: ").upper()

    if option == 'Q':
        print("Thank you for using the physics calculator!")
        break
    elif option == 'Z':
        if current_page < 2:
            current_page += 1
        continue
    elif option == 'X':
        if current_page > 0:
            current_page -= 1
  
    match option:
        case "1":
            num1 = float(input("Enter distance: "))
            num2 = float(input("Enter time: "))
            print("Result:", average_speed(num1, num2))

        case "2":
            num1 = float(input("Enter Δv: "))
            num2 = float(input("Enter Δt: "))
            print("Result:", acceleration(num1, num2))

        case "3":
            num1 = float(input("Enter mass: "))
            num2 = float(input("Enter volume: "))
            print("Result:", density(num1, num2))

        case "4":
            num1 = float(input("Enter work: "))
            num2 = float(input("Enter time: "))
            print("Result:", power(num1, num2))

        case "5":
            num1 = float(input("Enter mass: "))
            num2 = float(input("Enter acceleration: "))
            print("Result:", newtons_second_law(num1, num2))

        case "6":
            num1 = float(input("Enter mass: "))
            print("Result:", weight(num1))

        case "7":
            num1 = float(input("Enter force: "))
            num2 = float(input("Enter area: "))
            print("Result:", pressure(num1, num2))

        case "8":
            num1 = float(input("Enter current: "))
            num2 = float(input("Enter resistance: "))
            print("Result:", ohms_law(num1, num2))

        case "9":
            num1 = float(input("Enter mass: "))
            num2 = float(input("Enter velocity: "))
            print("Result:", kinetic_energy(num1, num2))

        case "10":
            num1 = float(input("Enter velocity: "))
            num2 = float(input("Enter wavelength: "))
            print("Result:", frequency(num1, num2))

        case "11":
            num1 = float(input("Enter length: "))
            print("Result:", pendulum(num1))

        case "12":
            num1 = float(input("Enter celsius: "))
            print("Result:", fahrenheit(num1))

        case "13":
            num1 = float(input("Enter force: "))
            num2 = float(input("Enter distance: "))
            num3 = float(input("Enter angle: "))
            print("Result:", work(num1, num2, num3))

        case "14":
            num1 = float(input("Enter force: "))
            num2 = float(input("Enter radius: "))
            num3 = float(input("Enter angle: "))
            print("Result:", torque(num1, num2, num3))

        case "15":
            num1 = float(input("Enter final position: "))
            num2 = float(input("Enter initial position: "))
            print("Result:", displacement(num1, num2))

        case "16":
            num1 = float(input("Enter force: "))
            num2 = float(input("Enter acceleration: "))
            print("Result:", mass(num1, num2))

        case _:
            print("Invalid option! Please try again.")
#physics calculator