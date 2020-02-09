import unittest

from bottle import view


class TestView(unittest.TestCase):

    @view("stpl_include")
    def test_basic(self):
        # Assert no errors
        return {"var": "foo"}

    @view("stpl_include2", template_lookup=["./views", "./non_standard_folder/views"])
    def test_template_lookup(self):
        # Assert no errors
        return {"var": "foo"}
