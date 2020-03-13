*** Settings ***
Library   TestLibrary.py

*** Keywords ***
Supply Image
      [Arguments]    ${image}
      ${output}=    send img     ${image}
      [return]        ${output}

*** Test Cases ***
Send Image
      ${out}=   Supply Image    dog.jpg
      Should be equal   ${out}   ${True}
