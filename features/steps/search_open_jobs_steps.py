from behave import *
from nose.tools import assert_equal
from page.search_open_jobs_pages import CoodeshSearchJobs
from page.user_account_pages import CoodeshLoginPage
from page.access_home_page_pages import CoodeshMainPage
from features.support.anchors import *

coodesh = CoodeshMainPage()
login = CoodeshLoginPage()
jobs = CoodeshSearchJobs()


@given(u'i access the Coodesh plataform with a valid user account')
def step_impl(context):
    coodesh.access_page(baseurl)
    login.login_into_platform('testenailtoncoodesh@gmail.com', 'T&stenailtoncoodesh9')


@when(u'inform the company name')
def step_impl(context):
    jobs.search_jobs('Piedpiper')


@then(u'open jobs company are show in screen search')
def step_impl(context):
    assert_equal(jobs.check_results_page(), baseurl+"/vagas?search=Piedpiper")


