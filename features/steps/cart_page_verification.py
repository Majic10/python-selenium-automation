from behave import when, then


@when("User navigates to the cart page")
def open_cart_page(context):
    context.app.header.click_cart()


@then("Cart page is displayed with no items in it")
def verify_cart(context):
    context.app.cart_page.verify_cart_empty()