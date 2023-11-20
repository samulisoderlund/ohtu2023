*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input Credentials  ${username}  ${password}

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username is invalid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle2  kalle123
    Output Should Contain  Username is invalid

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password must contain numbers
