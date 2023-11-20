*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Reset Application  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is invalid

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Click Button  Register
    Register Should Fail With Message  Password is too weak

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  123kalle
    Click Button  Register
    Register Should Fail With Message  Password confirmation does not match

Login After Successful Registration
    Register User  kalle  kalle123
    Go To Login Page
    Login With Credentials  kalle  kalle123
    Login Should Succeed

Login After Failed Registration
    Register User  k  kalle123
    Go To Login Page
    Login With Credentials  k  kalle123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register User
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password}
    Click Button  Register
