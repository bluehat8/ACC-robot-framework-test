from behave import given, then, when, step

@given('credentials are given')
def cred_are_given(context):
    print('user id: playok.com')

@when('we input correct credentials')
def step_impl(context):
    print('Credenciales correctas')
    
@then('login will be successful')
def step_impl(context):
    print('Bienvenido')