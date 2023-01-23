from behave import give, then, when, step

@given("I create a new User")
def login_with_credentials(context, item):
    print('The item is {}'.formate(item))