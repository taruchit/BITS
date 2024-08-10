# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:56:49 2023

@author: Tushar Spectre
"""

"""
0/1 Knapsack without repetition using functions and recursion
"""
import sys


#Method to find maximum and identify whether the mission was selected or not selected
def findMaximum(a,b):
    if(a>=b):

        return a,-1
    else:

        return b,1
    
#Method to find number of rows in the input file
def numberOfRows(file_contents):
    endLine=file_contents.split("\n")
    count=0
    for i in endLine:
        if len(i)!=0:
            count=count+1
    return count

#Recursive function to implement 0/1 Knapsack without repetition
def knapsack(wts,val,NumElements,CurrentCapacity,dp,included_items):

    if(CurrentCapacity<wts[NumElements-1]):
        
        
        included_items[NumElements][CurrentCapacity] = included_items[NumElements - 1][CurrentCapacity]
        return dp[NumElements-1][CurrentCapacity]
    

    
    notSelected=dp[NumElements-1][CurrentCapacity]
    selected=val[NumElements-1]+dp[NumElements-1][CurrentCapacity-wts[NumElements-1]]
    

    maxValue,temp=-100,-100
    maxValue,temp=findMaximum(selected,notSelected)
    if(temp==-1):
        included_items[NumElements][CurrentCapacity] = included_items[NumElements - 1][CurrentCapacity - wts[NumElements-1]] + [NumElements - 1]
    else:
        included_items[NumElements][CurrentCapacity] = included_items[NumElements - 1][CurrentCapacity]
    return maxValue

def main():
    #Reading the input file
    try:
        input_file = open('inputPS09.txt','r')
    except FileNotFoundError:
        print("inputPS09.txt file was not found, thus, exiting the program execution.")
        sys.exit()
    
    file_contents = input_file.read()
    input_file.close()
    
    n=numberOfRows(file_contents)
    if(n==0):
        print("Input file is empty, thus, exiting the program execution.")
        sys.exit()
    
    
    temp_list=file_contents.strip().split('\n')
    
    # Store the parsed data as tuples (S.No, Budget, Value)
    val_list = [] 
    
    for line in temp_list:
        parts = line.strip().split('/')
        if len(parts) != 3:
            print(f"Invalid line format: {line}")
            print("Expected input format is as follows: <Mission name i> integer / < Budget bi(crores)> numeric / < Value vi> numeric")
            print("Example of expected input:-\n 4/30/50")
            print("Since the input is not as per expected format, thus, exiting the program execution.")
            sys.exit()
        
        try:
            s_no = int(parts[0])
            budget = float(parts[1])
            value = float(parts[2])
            val_list.append((s_no, budget, value))
        except (ValueError, IndexError):
            print(f"Invalid data in line: {line}")
            print("Expected input format is as follows: <Mission name i> integer / < Budget bi(crores)> numeric / < Value vi> numeric")
            print("Example of expected input:-\n 4/30/50")
            print("Since the input is not as per expected format, thus, exiting the program execution.")
            sys.exit()

    
    srlist=[]
    wtlist=[]
    vallist=[]

    for i in range(n):
        for j in range(3):
            if(j==0):
                srlist.append(val_list[i][j])
            elif(j==1):
                wtlist.append(val_list[i][j])
            else:
                vallist.append(val_list[i][j])
      
    
    
    C=100
    
    wts=[]
    

    val=[]

    flag11=-1
    flag12=-1
    flag21=-1
    flag22=-1
    flag4=0
    

    null_nan=['null','nan']
    for element in wtlist:
        if not element or element==" ":
            #print("Data is missing")
            flag11=100
            break
        if element in null_nan:
            flag21=100
            break

        int_element=int(element)
        if(int_element>C):
            flag4=flag4+1
        wts.append(int_element)
    
    for element in vallist:
        if not element or element==" ":
            #print("Data is missing")
            flag12=100
            break
        if element in null_nan:
            flag22=100
            break
   
        int_element=int(element)
        val.append(int_element)
    
    #Error handling
    if(flag11==100):
        print("We have a missing data point for Budget; thus, exiting the program execution.")
        sys.exit()
    
    if(flag12==100):
        print("We have missing data point for Value; thus, exiting the program execution.")
        sys.exit()
    
    if(flag21==100):
        print("Under Budget we have a data point with value as nan or null, thus, exiting the program execution.")
        sys.exit()
    
    if(flag22==100):
        print("Under Value we have a data point with value as nan or null, thus, exiting the program execution.")
        sys.exit()
    
    if(flag4==n):
        print("All missions have budget greater than ",C," crores.")
        print("As a result, NO mission can be funded.")
        print("Thus, exiting the program execution.")
        sys.exit()
    dp = [[0 for _ in range(C+1)] for _ in range(n+1)]
    included_items = [[[] for _ in range(C + 1)] for _ in range(n + 1)]
    
    for i in range(1,n+1):
        for j in range(1,C+1):
            dp[i][j]=knapsack(wts,val,i,j,dp,included_items)
            #print("Value stored at dp[",i,"][",j,"]: ",dp[i][j])
    

    max_order=included_items[n][C]

    budgetUsed=0

    for i in max_order:

        budgetUsed=budgetUsed+wts[i]

    missionList="The missions that should be funded: "
    for i in max_order:

        missionList=missionList+str(i+1)
        missionList=missionList+", "
        
    line2="Total value: "+str(dp[-1][-1])

    line3="Budget remaining: "+str(C-budgetUsed)

    
    file_output=open("outputPS09.txt","w")
    file_output.write(missionList[0:-2])
    file_output.write("\n")
    file_output.write(line2)
    file_output.write("\n")
    file_output.write(line3)
    file_output.close()
    
    
    
    
main()