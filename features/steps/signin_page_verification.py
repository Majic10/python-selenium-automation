from behave import given, when, then


@given("User is on Amazon homepage")
def open_amazon(context):
    context.app.home_page.open_home_page()


@when("User navigates to signin page")
def open_orders_page(context):
    context.app.header.click_orders()


@then("The sign-in page is displayed")
def verify_signin(context):
    context.app.signin_page.verify_signin_opens()