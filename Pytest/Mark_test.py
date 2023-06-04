import pytest


# Markers allow us to run specific tests or restrict certain tests from running
# From command line we can use pytest -m "regression" to run tests marked "regression"
# To exclude the regression marker tests we can use pytest -m "not regression"
# To register custom Markers to remove warning create pytest.ini file at src, look at example

# Custom Markers
@pytest.mark.regression
def test_add_to_cart():
    print("Added one item to cart")


@pytest.mark.regression
def test_remove_from_cart():
    print("Remove one item from cart")


def test_remove_all_items_from_cart():
    print("Removed all items from cart")


# Built in Markers
# To skip a test
@pytest.mark.skip(reason="sample test to skip")
def test_sample_to_be_skipped():
    print("This test is skipped")


# Mark test function as expected to fail, can be many reasons, ex implementation has not been implemented yet
# Prevents whole test suites from failing due to one expected test to fail
@pytest.mark.xfail(reason="Not implemented yet")
def test_expected_fail():
    assert 2 + 2 == 5
