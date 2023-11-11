import schools
import math
import pathlib


def test_coordinate_constructor():
    c = schools.Coordinate(41.79, -87.71)
    assert c.latitude == 41.79
    assert c.longitude == -87.71


def test_coordinate_repr():
    c = schools.Coordinate(41.79, -87.71)
    assert str(c) == "Coordinate(41.79, -87.71)"


def test_coordinate_as_radians():
    c = schools.Coordinate(41.79, -87.71)
    cr = c.as_radians()
    assert math.isclose(cr[0], 0.7293730944084303)
    assert math.isclose(cr[1], -1.5308282869242262)


def test_coordinate_distance():
    chicago = schools.Coordinate(41.8781, -87.6298)
    nyc = schools.Coordinate(40.7128, -74.0060)
    la = schools.Coordinate(34.0522, -118.2437)

    assert math.isclose(chicago.distance(nyc), 711.4327006908619)
    assert math.isclose(nyc.distance(chicago), 711.4327006908619)
    assert math.isclose(chicago.distance(la), 1743.2947950288399)


def test_school_constructor():
    data = {
        "SCHOOL_ID": "101",
        "SCHOOL_NM": "Test School",
        "SCH_ADDR": "123 Main St, 60637",
        "GRADES": "K, 2, 3, 4",
        "SCH_TYPE": "Charter",
        "LAT": 41.8781,
        "LNG": -87.6298,
        "GRADE_CAT": "",
    }
    school = schools.School(data)
    assert school.id == "101"
    assert school.name == "Test School"
    assert school.address == "123 Main St, 60637"
    assert school.grades == ["K", "2", "3", "4"]
    assert school.school_type == "Charter"
    assert isinstance(school.location, schools.Coordinate)


def test_school_distance():
    chicago = schools.Coordinate(41.8781, -87.6298)
    nyc = schools.Coordinate(40.7128, -74.0060)
    data = {
        "SCHOOL_ID": "101",
        "SCHOOL_NM": "Test School",
        "SCH_ADDR": "123 Main St, 60637",
        "GRADES": "K, 2, 3, 4",
        "SCH_TYPE": "Charter",
        "LAT": 41.8781,
        "LNG": -87.6298,
        "GRADE_CAT": "",
    }
    school1 = schools.School(data)
    assert math.isclose(school1.distance(nyc), 711.4327006908619)
    assert math.isclose(school1.distance(chicago), 0)


def test_school_full_address():
    data = {
        "SCHOOL_ID": "101",
        "SCHOOL_NM": "Test School",
        "SCH_ADDR": "123 Main St, 60637",
        "GRADES": "K, 2, 3, 4",
        "SCH_TYPE": "Charter",
        "LAT": 41.8781,
        "LNG": -87.6298,
        "GRADE_CAT": "",
    }
    school = schools.School(data)
    assert school.full_address() == "123 Main St\nChicago, IL 60637"


def test_school_repr():
    data = {
        "SCHOOL_ID": "101",
        "SCHOOL_NM": "Test School",
        "SCH_ADDR": "123 Main St, 60637",
        "GRADES": "K, 2, 3, 4",
        "SCH_TYPE": "Charter",
        "LAT": 41.8781,
        "LNG": -87.6298,
        "GRADE_CAT": "",
    }
    school = schools.School(data)
    assert str(school) == "School(Test School)"


def test_school_system_from_csv():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    assert len(system.schools) == 680
    assert system.schools[0].id == "400009"
    assert system.schools[-1].id == "610573"


def test_school_system_by_type():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    assert len(system.get_schools_by_type("Charter")) == 131
    assert len(system.get_schools_by_type("X")) == 0


def test_school_system_by_grade():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    assert len(system.get_schools_by_grade("K")) == 462
    assert len(system.get_schools_by_grade("K", "1")) == 460
    assert len(system.get_schools_by_grade("10", "11")) == 169
    assert len(system.get_schools_by_grade("10", "11", "12")) == 160
    assert len(system.get_schools_by_grade("K", "12")) == 2
    assert len(system.get_schools_by_grade("K", "100")) == 0


def test_nearby_schools_default():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    center = schools.Coordinate(41.8781, -87.6298)
    assert len(system.nearby_schools(center)) == 5


def test_nearby_schools_radius():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    center = schools.Coordinate(41.8781, -87.6298)
    assert len(system.nearby_schools(center, 3)) == 76
    assert len(system.nearby_schools(center, 0.3)) == 1


def test_nearby_schools_far():
    filename = pathlib.Path(__file__).parent / "schools.csv"
    system = schools.SchoolSystem(filename)
    center = schools.Coordinate(41.8781, 87.6298)
    assert len(system.nearby_schools(center)) == 0
    assert len(system.nearby_schools(center, 100)) == 0
