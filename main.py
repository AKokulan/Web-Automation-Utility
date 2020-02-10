import web_handle,excel_handle,pandas as pd,time


def actions(action,input,output,output_dict):
    outcome=""
    if action=='launch-chrome': outcome=web_handle.launch_browser_with_chrome(driver_path=input[0]) #tested
    if action == 'launch-ie': output=web_handle.launch_browser_with_ie(driver_path=input[0])
    if action == 'launch-firefox': output=web_handle.launch_browser_with_firefox(driver_path=input[0])
    if action == 'open-url': web_handle.open_website(driver=output_dict[input[0]],url=input[1]) #tested
    if action == 'click-button': outcome=web_handle.click_left_button(driver=output_dict[input[0]],xpath=input[1],wait_time=int(input[2]),number_of_clicks=int(input[3])) #tested
    if action == 'read-text': outcome=web_handle.read_text(driver=output_dict[input[0]], xpath=input[1],wait_time=int(input[2])) #tested

    #2 scnarios for write text. #tested
    if action == 'write-text' and input[3] in output_dict:
        outcome=web_handle.write_text(driver=output_dict[input[0]], xpath=input[1], wait_time=int(input[2]),text=output_dict[input[3]])
    if action == 'write-text' and input[3] not in output_dict:
        outcome=web_handle.write_text(driver=output_dict[input[0]], xpath=input[1], wait_time=int(input[2]),text=input[3])

    if action == 'close-browser': web_handle.close_browser(driver=output_dict[input[0]]) #tested
    if action == 'read-excel': outcome=excel_handle.load_list_from_excel(file_path=input[0],sheet_name=input[1],number_of_columns=int(input[2]),header=int(input[3])) #tested
    output_dict[output] = outcome
    return output_dict


output_dict={}
file_path=""
file_path_action=open(r"C:\swau\Action File Path.txt")
for each in file_path_action:file_path=each

actions_list=excel_handle.load_list_from_excel(file_path=file_path,sheet_name="Actions",number_of_columns=100,header=0)

loop_active=False
loop_list,loop_actions_list,input_for_loop_action_list,output_for_loop_action_list="",list(),list(),list()
for series,each_rows in actions_list.iterrows():
    #action,input,output='','',''
    action=(str(actions_list.at[series,"Action"])).lower()
    input=((str(actions_list.at[series,"Input"]))).split(";")
    output = ((str(actions_list.at[series, "Output"]))).split(";")
    #condition = (str(actions_list.at[series, "Condition"]))
    #(action,input,output,condition)

    if action=="loop-start":
       loop_active = True
       if input[0] in output_dict:
           print(input[0])
           loop_list=output_dict[input[0]]
           print(loop_list)
       else:
           print("Input list given for loop is not defined")
           break

    if loop_active == True and action!="loop-start" and action!="loop-end" :
        loop_actions_list.append(action)
        input_for_loop_action_list.append(input)
        output_for_loop_action_list.append(output)
        print(loop_actions_list,input_for_loop_action_list,output_for_loop_action_list)

    if action=="loop-end" and loop_active == True:
        for series_loop,rows_loop  in loop_list.iterrows():
            for each in range(len(loop_actions_list)):
                actions(action=loop_actions_list[each], input=input_for_loop_action_list[each], output=(output_for_loop_action_list[each])[0],output_dict=output_dict)
        loop_active=False

    if loop_active == False:
        print(input)

        output_dict=actions(action=action,input=input,output=str(output[0]),output_dict=output_dict)
        print(output_dict)

    #time.sleep(5)
    print(loop_active)













