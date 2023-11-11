import csv
import pathlib
import math

class School:
  """
    Initialize the properties of each school based on the first row of the csv file.
    Grades stored in a list of string.
    The location is converted to a Coordinate.
  """
  def __init__(self, data):
    self.id = data['SCHOOL_ID']
    self.name = data['SCHOOL_NM']
    self.address = data['SCH_ADDR']
    self.grades = data['GRADES'].split(', ') #spaces need to be stripped at the same time
    self.school_type = data['SCH_TYPE']
    self.location = Coordinate(float(data['LAT']), float(data['LNG']))
  
  def distance(self, coord):
    """
    Returns the distance from the current location to the given coordinates.
    """
    return self.location.distance(coord)
  
  def full_address(self):
    """
    Returns the address of the instance with the given format.
    """
    return f"{self.address[:-7]}\nChicago, IL {self.address[-5:]}"
  
  def __str__(self):
    """
    Shows the instance's information.
    """
    return f"School({self.name})"
  
class Coordinate:
  """
    Assign the latitude and longitude to the Coordinate.
  """
  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  def distance(self, coord):
    """
    Calculate the distance using the given formula from the current instance to given coord.
    """
    r = 3961
    lat1, lon1 = self.as_radians()
    lat2, lon2 = coord.as_radians()

    lat_diff = lat1 - lat2
    lon_diff = lon1 - lon2

    intermediate_value1 = math.sin(lat_diff / 2) ** 2
    intermediate_value2 = math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2

    return 2 * r * math.asin(math.sqrt(intermediate_value1 + intermediate_value2))
  
  def as_radians(self):
    """
    Covert the instance to a radians value.
    """
    return (math.radians(self.latitude), math.radians(self.longitude))
  
  def __str__(self):
    """
    Shows the longitude and latitude for the current coord.
    """
    return f"Coordinate({self.latitude}, {self.longitude})"
  
class SchoolSystem:
  """
    Initialize a list of schools in the current SchoolSystem.
    Open and read the csv file, assign a line to a school.
  """
  def __init__(self, filename):
    self.schools = []
    with open(pathlib.Path(__file__).parent / filename) as fd:
      reader = csv.DictReader(fd)
      for line in reader:
        self.schools.append(School(line))

  def get_schools_by_type(self, school_type):
    """
    Filtering the schools of a given type.
    """
    return [school for school in self.schools if school.school_type == school_type]

  def get_schools_by_grade(self, *grades):
    """
    Filtering schools which offer exactly the same grades as the given grades list.
    """
    return [school for school in self.schools if all(grade in school.grades for grade in grades)]
      
  def nearby_schools(self, coord, radius=1.0):
    """
    Filtering the schools in a certain radius within the given coord.
    """
    return [school for school in self.schools if school.distance(coord) <= radius]