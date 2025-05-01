#Q.1 Write a program to create a class that represents Complex numbers containing real and imaginary parts and
#then use it to perform complex numberaddition, subtraction, multiplication and division.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(round(real, 2), round(imag, 2))


# Example usage
if __name__ == "__main__":
    c1 = Complex(4, 5)
    c2 = Complex(2, -3)

    print(f"First Complex Number: {c1}")
    print(f"Second Complex Number: {c2}\n")

    print("Addition:", c1 + c2)
    print("Subtraction:", c1 - c2)
    print("Multiplication:", c1 * c2)
    print("Division:", c1 / c2)

#Q.2 Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices.

    class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                val = sum(self.data[i][k] * other.data[k][j] for k in range(3))
                row.append(val)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)


# Example usage
if __name__ == "__main__":
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    B = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA * B:")
    print(A * B)

    print("\nTranspose of A:")
    print(A.transpose())


#Q.3 Write a program to create a class that can calculate the surface area and volume of a solid.
    #The class should also have a provision to accept the data relevant to the solid.

import math

class Solid:
    def __init__(self, shape, **dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def calculate_surface_area(self):
        if self.shape == "cube":
            side = self.dimensions.get("side", 0)
            return 6 * side ** 2
        elif self.shape == "sphere":
            radius = self.dimensions.get("radius", 0)
            return 4 * math.pi * radius ** 2
        elif self.shape == "cylinder":
            radius = self.dimensions.get("radius", 0)
            height = self.dimensions.get("height", 0)
            return 2 * math.pi * radius * (radius + height)
        else:
            return "Unknown shape"

    def calculate_volume(self):
        if self.shape == "cube":
            side = self.dimensions.get("side", 0)
            return side ** 3
        elif self.shape == "sphere":
            radius = self.dimensions.get("radius", 0)
            return (4/3) * math.pi * radius ** 3
        elif self.shape == "cylinder":
            radius = self.dimensions.get("radius", 0)
            height = self.dimensions.get("height", 0)
            return math.pi * radius ** 2 * height
        else:
            return "Unknown shape"

# Example usage
if __name__ == "__main__":
    # Cube with side 3
    cube = Solid("cube", side=3)
    print(f"Cube Surface Area: {cube.calculate_surface_area()} units²")
    print(f"Cube Volume: {cube.calculate_volume()} units³\n")
    
    # Sphere with radius 5
    sphere = Solid("sphere", radius=5)
    print(f"Sphere Surface Area: {sphere.calculate_surface_area()} units²")
    print(f"Sphere Volume: {sphere.calculate_volume()} units³\n")
    
    # Cylinder with radius 4 and height 10
    cylinder = Solid("cylinder", radius=4, height=10)
    print(f"Cylinder Surface Area: {cylinder.calculate_surface_area()} units²")
    print(f"Cylinder Volume: {cylinder.calculate_volume()} units³")

#Q.4 Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape.
    #The class should also have a provision to accept the data relevant to the shape.

    import math

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def calculate_perimeter(self):
        if self.shape_type == "square":
            side = self.dimensions.get("side", 0)
            return 4 * side
        elif self.shape_type == "circle":
            radius = self.dimensions.get("radius", 0)
            return 2 * math.pi * radius
        elif self.shape_type == "triangle":
            a = self.dimensions.get("a", 0)
            b = self.dimensions.get("b", 0)
            c = self.dimensions.get("c", 0)
            return a + b + c
        elif self.shape_type == "rectangle":
            length = self.dimensions.get("length", 0)
            width = self.dimensions.get("width", 0)
            return 2 * (length + width)
        else:
            return "Unknown shape"

    def calculate_area(self):
        if self.shape_type == "square":
            side = self.dimensions.get("side", 0)
            return side ** 2
        elif self.shape_type == "circle":
            radius = self.dimensions.get("radius", 0)
            return math.pi * radius ** 2
        elif self.shape_type == "triangle":
            base = self.dimensions.get("base", 0)
            height = self.dimensions.get("height", 0)
            return 0.5 * base * height
        elif self.shape_type == "rectangle":
            length = self.dimensions.get("length", 0)
            width = self.dimensions.get("width", 0)
            return length * width
        else:
            return "Unknown shape"

# Example usage
if __name__ == "__main__":
    # Square with side 4
    square = Shape("square", side=4)
    print(f"Square Perimeter: {square.calculate_perimeter()} units")
    print(f"Square Area: {square.calculate_area()} square units\n")
    
    # Circle with radius 5
    circle = Shape("circle", radius=5)
    print(f"Circle Circumference: {circle.calculate_perimeter()} units")
    print(f"Circle Area: {circle.calculate_area()} square units\n")
    
    # Triangle with sides 3, 4, and 5 (Right-angled triangle)
    triangle = Shape("triangle", a=3, b=4, c=5)
    print(f"Triangle Perimeter: {triangle.calculate_perimeter()} units")
    print(f"Triangle Area: {triangle.calculate_area()} square units\n")
    
    # Rectangle with length 5 and width 6
    rectangle = Shape("rectangle", length=5, width=6)
    print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()} units")
    print(f"Rectangle Area: {rectangle.calculate_area()} square units")

#Q.5 Write a program that creates and uses a Time class to perform various time arithmetic operations.

    class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        """Normalize the time to make sure seconds and minutes are in valid ranges."""
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24  # Keep hours within 24-hour format

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other):
        """Add two Time instances."""
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def subtract(self, other):
        """Subtract two Time instances."""
        total_seconds = self.to_seconds() - other.to_seconds()
        if total_seconds < 0:
            raise ValueError("Resulting time cannot be negative")
        return Time.from_seconds(total_seconds)

    def to_seconds(self):
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """Create a Time instance from total seconds."""
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def compare(self, other):
        """Compare two Time instances."""
        if self.to_seconds() == other.to_seconds():
            return "Equal"
        elif self.to_seconds() > other.to_seconds():
            return "Greater"
        else:
            return "Smaller"

# Example usage
if __name__ == "__main__":
    # Create Time instances
    time1 = Time(10, 45, 30)  # 10:45:30
    time2 = Time(5, 30, 45)   # 05:30:45

    print(f"Time 1: {time1}")
    print(f"Time 2: {time2}")

    # Addition of time
    added_time = time1.add(time2)
    print(f"Time 1 + Time 2: {added_time}")

    # Subtraction of time
    subtracted_time = time1.subtract(time2)
    print(f"Time 1 - Time 2: {subtracted_time}")

    # Compare two times
    comparison_result = time1.compare(time2)
    print(f"Time 1 is {comparison_result} than Time 2.")

#Q.6 Write a program to create a class Date that has a list containing day, month and year attributes.
    #Define an overloaded == operator to compare two Date objects.

    class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"

    def __eq__(self, other):
        """Overload == operator to compare two Date objects."""
        if not isinstance(other, Date):
            return False
        return self.day == other.day and self.month == other.month and self.year == other.year

# Example usage
if __name__ == "__main__":
    # Create two Date objects
    date1 = Date(25, 12, 2022)
    date2 = Date(25, 12, 2022)
    date3 = Date(1, 1, 2023)

    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Date 3: {date3}")
    
    # Compare dates using overloaded == operator
    print(f"Is Date 1 equal to Date 2? {date1 == date2}")
    print(f"Is Date 1 equal to Date 3? {date1 == date3}")

#Q.7 Create a class Weather that has a list containing weather parameters.
    #Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)

    class Weather:
    def __init__(self, temperature, humidity, wind_speed):
        # Initialize the weather parameters in a list
        self.parameters = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }

    def __contains__(self, item):
        """Overload the 'in' operator to check if an item is a weather parameter."""
        return item in self.parameters.values()

    def __str__(self):
        return f"Weather parameters: {self.parameters}"

# Example usage
if __name__ == "__main__":
    # Create a Weather object
    weather = Weather(25, 65, 15)  # Temperature 25°C, Humidity 65%, Wind Speed 15 km/h

    print(weather)
    
    # Check if certain parameters are in the weather list using the 'in' operator
    print(f"Is temperature (25) in the weather parameters? {'temperature' in weather}")
    print(f"Is humidity (65) in the weather parameters? {65 in weather}")
    print(f"Is wind speed (20) in the weather parameters? {20 in weather}")

#Q.8 Implement a String class containing the following functions:
#a. Overloaded += operator function to perform string concatenation
#b. Method toLower() to convert upper case letters to lower case.
#c. Method toUpper() to convert lower case letters to upper case.

    class Weather:
    def __init__(self, temperature, humidity, wind_speed):
        # Initialize the weather parameters in a list
        self.parameters = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }

    def __contains__(self, item):
        """Overload the 'in' operator to check if an item is a weather parameter."""
        return item in self.parameters.values()

    def __str__(self):
        return f"Weather parameters: {self.parameters}"

# Example usage
if __name__ == "__main__":
    # Create a Weather object
    weather = Weather(25, 65, 15)  # Temperature 25°C, Humidity 65%, Wind Speed 15 km/h

    print(weather)
    
    # Check if certain parameters are in the weather list using the 'in' operator
    print(f"Is temperature (25) in the weather parameters? {'temperature' in weather}")
    print(f"Is humidity (65) in the weather parameters? {65 in weather}")
    print(f"Is wind speed (20) in the weather parameters? {20 in weather}")
