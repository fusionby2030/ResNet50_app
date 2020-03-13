*** Settings ***
Library   TestLibrary.py
Library   JsonValidator

*** Keywords ***
Supply Image
      [Arguments]    ${image}
      ${output}=    send img     ${image}
      [return]        ${output}
Detection
      [Arguments]    ${image}
      ${output}=    image analysis     ${image}
      [return]        ${output}
Post Image
      [Arguments]    ${image}
      ${output}=    post img     ${image}
      [return]        ${output}
*** Test Cases ***
Send Image
      ${out}=   Supply Image    dog.jpg
      Should be equal   ${out}   ${True}
Correct Analysis
      ${out}=   Detection     dog.jpg
      should contain    ${out}    beagle

Check Element
      ${out}=   Post Image    dog.jpg
      Element should exist   ${out}   .label:contains("beagle")
