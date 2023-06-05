# To run pytest on PyCharm IDE, top right left of play icon click drop down, select edit configurations,
# click "+" to add new config, select pytest, on right side, for target, select the pytest file, click OK.
# Now you can click green play button on top right to run tests on selected pytest file.
# Pytest will automatically find all python test files if they start with test_*.py or end with *_test.py if you run
# pytest in command line at source directory
# On command line pytest -v will give more verbose
# On command line pytest -s no capture
# On command line pytest -k green will run tests with green keyword only
# On command line pytest -vk yellow will run yellow keyword tests with verbose
# On command line pytest Pytest/Basics_test.py to run tests from Basics_test.py from src level
# On command line pytest Pytest/Basics_test.py::test_click_blue_button to run only test_click_blue_button


def test_click_blue_button():
    print("Blue menu appears")


def test_click_green_button():
    print("Green menu appears")


def test_click_yellow_button():
    print("Yellow menu appears")
