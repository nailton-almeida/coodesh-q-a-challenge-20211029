from browser import Browser

# Execute before all scenarios
def before_all(context):
    context.browser = Browser()


# Execute after all scenarios
def after_all(context):
      context.browser.browser_clear()
      context.browser.browser_quit()



