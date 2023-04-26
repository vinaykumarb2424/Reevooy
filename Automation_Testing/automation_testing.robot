*** Settings ***
Library         ./Automation.py      WITH NAME       client1
#Resource        ./Evernote/keywords/Evernote.robot
Suite Setup     Create Instance


*** Variables ***
${email}     email_id@gmail.com
${password}     Todoist@1
${task_name}    task_name
${description}  description
${sub_task_task_name}   sub_task_task_name
${sub_task_description}          add_sub_task_description
*** Keywords ***
I do login account
  [Arguments]    ${Client}       ${email}       ${password}
   Call Method       ${Client}      click_login_link
   Call Method       ${Client}      enter_email     ${email}
   Call Method       ${Client}      enter_password      ${password}
   Call Method       ${Client}      click_login_btn

I do create new task and verify
  [Arguments]    ${Client}  ${task_name}     ${description}
  Call Method       ${Client}      click_add_task
  Call Method       ${Client}      enter_task_details   ${task_name}     ${description}
  Call Method       ${Client}      verify_task_creation   #${task_name}     ${description}

I do mark todo as complete succssfull
    [Arguments]    ${Client}
    Call Method       ${Client}      mark_task_complete

I do add sub task, verify
    [Arguments]    ${Client}    ${sub_task_task_name}    ${sub_task_description}
    Call Method       ${Client}     open_created_task
    Call Method       ${Client}      add_sub_task     ${sub_task_task_name}    ${sub_task_description}
    Call Method       ${Client}      verify_sub_task_creation

Create Instance
    ${Client}=  Get Library Instance      client1
    Set Suite Variable      ${Client}
*** Test Cases ***
I do login and verify
    I do login account  ${Client}       ${email}        ${password}

I do create new todo list and verify
    I do create new task and verify     ${Client}       ${task_name}     ${description}


#I do mark todo as complete
    #I do mark todo as complete succssfull    ${Client}

I do add sub task and verify
    I do add sub task, verify   ${Client}       ${sub_task_task_name}    ${sub_task_description}
