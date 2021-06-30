# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:23:47 2021

@author: 91703
"""

import csv


def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Mobile no.","email"])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition=True
    student_num=1
    
    while(condition):
        student_info = input("Enter student information for student #{} in the following format (Name age mobile no. email)- "
                             .format(student_num))
        print("Entered student information is ",student_info)
        
        #split
        student_info_list = student_info.split(' ')
        print("Entered split up information is ",student_info_list)
        
        print("\nThe entered information is - \nName : {} \nAge : {} \nMobile no. : {} \nEmail : {}"
              .format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))
        
        choice_check=input("Is the entered information is correct ? (yes/no)")
        
        if choice_check == "yes":
            write_into_csv(student_info_list)
      
            
            condition_check=input("Enter (yes or no) if you want to submit reponse for another student- ")
            if condition_check == "yes":
                condition=True
                student_num+=1
            elif(condition_check=="no"):
                condition=False
                
        elif choice_check=="no":
            print("\nPlease reenter correct values.")