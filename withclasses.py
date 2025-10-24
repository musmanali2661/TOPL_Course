# --- Complete Setup and Execution ---
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


# Base class for all geometric shapes
class Shape(ABC):
    @abstractmethod
    def from_line(line: str) -> 'Shape' or None:
        """
        Abstract method to be implemented by all concrete shape classes.
        Parses a line of text and returns a new instance of the shape.
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Abstract method for a human-readable string representation.
        """
        pass


class Rectangle(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def from_line(line: str) -> 'Rectangle' or None:
        parts = line.strip().split(',')

        if parts[0] == 'RECT' and len(parts) == 5:
            try:
                # Cast the four coordinate strings to integers
                coords = [int(p) for p in parts[1:]]
                return Rectangle(*coords)
            except ValueError:
                return None
        return None

    def __str__(self):
        return f"Rectangle(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"


class Circle(Shape):
    def __init__(self, cx: int, cy: int, r: int):
        self.cx = cx
        self.cy = cy
        self.r = r

    @staticmethod
    def from_line(line: str) -> 'Circle' or None:
        parts = line.strip().split(',')

        if parts[0] == 'CIRC' and len(parts) == 4:
            try:
                # Cast the three values (cx, cy, r) to integers
                vals = [int(p) for p in parts[1:]]
                return Circle(*vals)
            except ValueError:
                return None
        return None

    def __str__(self):
        return f"Circle(Center: ({self.cx}, {self.cy}), Radius: {self.r})"


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.v1 = (x1, y1)
        self.v2 = (x2, y2)
        self.v3 = (x3, y3)

    @staticmethod
    def from_line(line: str) -> 'Triangle' or None:
        parts = line.strip().split(',')

        if parts[0] == 'TRIA' and len(parts) == 7:  # Expecting 6 coordinates + label
            try:
                coords = [int(p) for p in parts[1:]]
                return Triangle(*coords)
            except ValueError:
                return None
        return None

    def __str__(self):
        return f"Triangle(V1:{self.v1}, V2:{self.v2}, V3:{self.v3})"


class Line(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)

    @staticmethod
    def from_line(line: str) -> 'Line' or None:
        parts = line.strip().split(',')

        if parts[0] == 'LINE' and len(parts) == 5:
            try:
                coords = [int(p) for p in parts[1:]]
                return Line(*coords)
            except ValueError:
                return None
        return None

    def __str__(self):
        return f"Line(P1:{self.p1}, P2:{self.p2})"



class Shape(ABC):
    @staticmethod
    @abstractmethod
    def from_line(line: str) -> 'Shape' or None:
        pass

    @abstractmethod
    def __str__(self):
        pass


# Define all classes here (omitted for brevity, but assume they are defined)
# ...

# REVISED data to match class expectations (especially Triangle)
file_content = """RECT,12,45,56,23
CIRC,12,45,56
TRIA,12,45,56,23,34,55  # Added a 6th coordinate for robust Triangle parsing
LINE,12,45,56,23
RECT,10,20,30,40
CIRC,5,5,10
TRIA,1,1,2,2,3,3
LINE,1,2,3,4"""
with open('shapes.txt', 'w') as f:
    f.write(file_content)

# Map the string identifier to the corresponding class object
SHAPE_MAP = {
    'RECT': Rectangle,
    'CIRC': Circle,
    'TRIA': Triangle,
    'LINE': Line
}

# List to store the heterogeneous shape objects
all_shapes = []

print("--- Parsing 'shapes.txt' Polymorphically ---")
with open('shapes.txt', 'r') as f:
    line = f.readline()

    while line:
        line = line.strip()
        if not line:  # Skip empty lines
            line = f.readline()
            continue

        parts = line.split(',')
        label = parts[0]

        # Check if the label exists in our map
        if label in SHAPE_MAP:
            ShapeClass = SHAPE_MAP[label]  # Get the correct class (e.g., Rectangle)

            # Use the static method to create the specific shape object
            shape_object = ShapeClass.from_line(line)

            if shape_object:
                all_shapes.append(shape_object)
                print(f"Created: {shape_object}")
            # Note: The from_line method handles lines that don't match the
            # expected length or data type by returning None.
        else:
            print(f"Skipped: Unknown shape type '{label}'")

        line = f.readline()

print("\n--- Summary of All Shapes (Polymorphic List) ---")
for shape in all_shapes:
    # Here is the polymorphism in action: calling __str__() on different types
    # of objects (Rectangle, Circle, etc.) using the same variable 'shape'.
    print(shape)