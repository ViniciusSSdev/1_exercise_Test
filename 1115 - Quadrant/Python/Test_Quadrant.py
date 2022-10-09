from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"

def test_second_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = -10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_fourth_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 0
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "ordinate axis"

def test_third_should_get_quadrant_coordinate():
    # Arrange / Setup
    a = 10
    b = 0
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "abscissas axis"