from behave import *
from page.access_home_page_pages import CoodeshMainPage
from features.support.anchors import *

coodesh = CoodeshMainPage()

@given(u'i access valid url')
def step_impl(context):
    coodesh.access_page(baseurl)


@then(u'the elements expects was loaded in screen')
def step_impl(context):
    coodesh.check_load_page()
