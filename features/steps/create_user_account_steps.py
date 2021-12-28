from behave import *
from nose.tools import assert_equal
from page.user_account_pages import CoodeshLoginPage
from page.access_home_page_pages import CoodeshMainPage
from features.support.anchors import *
import calendar
import time

coodesh = CoodeshMainPage()
login = CoodeshLoginPage()
ts = str(calendar.timegm(time.gmtime()))


@given(u'i access the Coodesh plataform')
def step_impl(context):
    coodesh.access_page(baseurl)


@when(u'type all mandatory personal data')
def step_impl(context):
    login.create_account(ts,ts+"@gmail.com",'T&stenailtoncoodesh9')


@then(u'account was created')
def step_impl(context):
    assert_equal(login.check_user_creation(), ts)
