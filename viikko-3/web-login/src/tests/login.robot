*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Login With Credentials  kalle  kalle123
    Login Should Succeed

Login With Incorrect Password
    Login With Credentials  kalle  kalle456
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Login With Credentials  nobody  kalle123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
