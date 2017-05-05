# class Customer(object):
#     """ Produces objects that represent customers. """
#     def __init__(self, customer_id):
#         self.customer_id = customer_id

#     def display_cart(self):
#         print ("I'm a string that stands in for the contents of your shopping cart")


# class ReturningCustomer(Customer):  #inheritance from Customer
#     """ For customers of the repeat variety """

#     def display_order_history(self):
#         print ("I'm a string that stands in for your order history")


# monty_python = ReturningCustomer("ID: 12345")
# monty_python.display_cart()
# monty_python.display_order_history()

# newpie = Customer("333")
# print(newpie.customer_id)
# newpie.display_cart()

# newpie = ReturningCustomer("334")
# newpie.display_order_history()
# print (newpie.customer_id)


# INHERITANCE

class Shape(object):
    """ Makes shapes! """
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


# OVERRIDING WITHIN CLASSES

class Employee(object):
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        print ("Hello %s" % other.name)


class CEO(Employee):
    def greet(self, other):  # notice the same function name.
        print ("Get back to work %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")

emp.greet(ceo)
ceo.greet(emp)

# BASIC OVERRIDE

# class Employee(object):
#     """ Models real-life employees """
#     def __init__(self, employee_name):
#         self.employee_name = employee_name

#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 20.00


# class PartTimeEmployee(Employee):
#     """ makes part time employees """

#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 12.00



class Employee(object):
    """ Models real-life employees """
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    """ makes part time employees """

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        """ this references the method of the same name from the parent class """
        return super(PartTimeEmployee, self).calculate_wage(hours)



milton = PartTimeEmployee("Milton")

print (milton.full_time_wage(10))



class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle



test = Equilateral()


my_triangle = Triangle(90, 30, 60)

print (my_triangle.number_of_sides)
print (my_triangle.check_angles())