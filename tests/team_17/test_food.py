import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("group", 20, 15)

def test_get_value(food):
    assert food.get_value() == 20

def test_get_cost(food):
    assert food.get_cost() == 15

def test_density(food):
    assert food.density() == 20/15

def test_str(food):
    assert str(food) == "group: <20, 15>"