import pytest
from task import *

def test_task5_body_parser():
    assert Task5().parse_body('example<a>112</a>') == 'example&lt;a&gt;112&lt;/a&gt;','BAD body parse'
# @pytest.yield_fixture()
def test_task5_tags_parser():
    assert Task5().parse_tags('p.my-class1.my_class2#id2') == ('p','my-class1 my_class2','id2')


