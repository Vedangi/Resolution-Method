import sys
import copy
from operator import itemgetter

## Global Variables
Premises_count = 0

# defining unification function
def unification(clause_list1, clause_list2):
    index= 0;
    count = 0
    copy_clause_list1 = copy.deepcopy(clause_list1)
    copy_clause_list2 = copy.deepcopy(clause_list2)
    inner_clause_pos = copy_clause_list1[1]
    inner_clause_neg = copy_clause_list1[2]
    outer_clause_pos = copy_clause_list2[1]
    outer_clause_neg = copy_clause_list2[2]
    if clause_list1[1:] == [] or clause_list2[1:] == []:
        return "FAIL"
    else:
        PositiveNegative = 0
        NegativePositive = 0
        SUCCESS_count = 0
        statusDone = 0
        for i in range(0, len(inner_clause_pos )):
            for j in range(0, len(outer_clause_neg )):
               count = count + 1
               print("clauses are:", "1:", inner_clause_pos  ,"2:", outer_clause_neg )
               if (inner_clause_pos [i]!= []) and (outer_clause_neg [j]!= []):
                if (inner_clause_pos [i][0] == outer_clause_neg [j][0]) and (len(inner_clause_pos [i]) == len(outer_clause_neg [j])):
                   print(count, "\n")
                   index = index + 1
                   print(index)
                   temp_list = []
                   [Status, literal1, literal2, subval]= apply_substitution(inner_clause_pos [i][1:],outer_clause_neg [j][1:],temp_list)
                   if (Status == "SUCCESS"):
                       PositiveNegative = 1
                       list1pos = i;
                       list2neg = j;
                       SUCCESS_count += 1
                       print("SUCCESS_count in posneg is", SUCCESS_count)
                       
                       substitute_for_all(copy_clause_list1, copy_clause_list2,subval)
     
                       print("subvalue is", subval)
                       statusDone = 1
                       break

            if statusDone == 1:
             break
        if(statusDone!= 1)  :  
         for i in range(0, len(outer_clause_pos )):
          for j in range(0, len(inner_clause_neg )):
             count = count + 1
             print("clauses in 2 are:", "1:", outer_clause_pos  ,"2:", inner_clause_neg )
             if (outer_clause_pos [i]!= []) and (inner_clause_neg [j]!= []):
               if (outer_clause_pos [i][0] == inner_clause_neg [j][0]) and (len(outer_clause_pos [i]) == len(inner_clause_neg [j])):
                   print(count, "\n")
                   index = index + 1
                   print(index)
                   temp_list= []
                   [Status,literal1,literal2,subval]= apply_substitution(outer_clause_pos [i][1:],inner_clause_neg [j][1:],temp_list)
                   if (Status == "SUCCESS"):
                       NegativePositive = 1
                       list1neg = j;
                       list2pos = i;
                       SUCCESS_count += 1
                       print("SUCCESS_count in negpos  is", SUCCESS_count)
                       substitute_for_all(copy_clause_list1, copy_clause_list2,subval)
                       statusDone= 1
                       break

          if statusDone == 1:
             break
              
        if(SUCCESS_count== 1):
           resolvent_list= []
           if(PositiveNegative):
             resolvent_list = resolve(copy_clause_list1[1:], copy_clause_list2[1:], list1pos,list2neg,1)
             print(resolvent_list)
             return "SUCCESS",resolvent_list
           else:
             resolvent_list = resolve(copy_clause_list1[1:], copy_clause_list2[1:], list1neg,list2pos,0)
             return "SUCCESS",resolvent_list
        else:
            return("FAIL",[])

#defining substiituion function
def apply_substitution(literal1,literal2,temp_list):
     index = 0
     literal1_temp= copy.deepcopy(literal1)
     print("literal1 is ", literal1_temp)
     literal2_temp= copy.deepcopy(literal2)
     print("literal2 is ", literal2_temp)

     while (index!=len(literal1_temp)):
       if(literal1_temp[index]!=literal2_temp[index]):
        print("indices 1 and 2 are:",(isinstance(literal1_temp[index],list)),isinstance(literal2_temp[index],list))
        
## To check if both variables in clause_lists are not of type lists ie they are not functions
        if not((isinstance(literal1_temp[index],list)) or (isinstance(literal2_temp[index],list))):
         if(literal1_temp[index].islower()) :# and (literal2_temp[index].islower()):
             temp_list.append(literal1_temp[index])
             temp_list.append(literal2_temp[index])
             print("temp list for first", temp_list)
             temp_variable= literal1_temp[index]
             for i in range(0, len(literal1_temp)):
               if(literal1_temp[i] ==temp_variable):
## Substituing for all variables in clause_inner
                literal1_temp[i]=literal2_temp[index]
             for i in range(0, len(literal2_temp)):
              if(literal2_temp[i] ==temp_variable):
## Substituing for all variables in clause_outer
                literal2_temp[i]=literal2_temp[index]

## Comparing different cases - Upper, Lower
         elif(literal1_temp[index].isupper()) and (literal2_temp[index].islower()):
             temp_list.append(literal2_temp[index] )
             temp_list.append(literal1_temp[index])
             for i in temp_list:
               print(i, ", ")
             print ("\n")
             temp_variable= literal2_temp[index]
             for i in range(0, len(literal1_temp)):
               if(literal1_temp[i] ==temp_variable):
                print("helllo" , i)
                print("that is",literal2_temp[index] )
                literal1_temp[i]=literal1_temp[index]
                print("that is", literal1_temp[i] )
             for i in range(0, len(literal2_temp)):
              if(literal2_temp[i] ==temp_variable):
                literal2_temp[i]=literal1_temp[index]
##  Both are constants
         elif(literal1_temp[index].isupper() and literal2_temp[index].isupper()):
             print("values at failure stage", literal1_temp[index], literal2_temp[index])
             status = "Fail"
             break
         else: pass
        else:
         if not((isinstance(literal1_temp[index],list)) and (isinstance(literal2_temp[index],list))) : 
          if ((isinstance(literal1_temp[index],list))):
           if(literal2_temp[index].islower()):
            temp_list.append(literal2_temp[index])
            print("Temp_list after function first is", temp_list)
            temp_list.append(literal1_temp[index])
            print("Temp_list after second variable is", temp_list)
            temp_variable= literal2_temp[index]
            for i in range(0, len(literal1_temp)):
             if(literal1_temp[i] ==temp_variable):
                print("helllo" , i)
                print("that is",literal2_temp[index] )
                literal1_temp[i]=literal1_temp[index]
                print("that is", literal1_temp[i] )
            for i in range(0, len(literal2_temp)):
             if(literal2_temp[i] ==temp_variable):
                literal2_temp[i]=literal1_temp[index]
           else:
                status = "FAIL"
                break
          else:
           if ((isinstance(literal2_temp[index],list))):
            print(literal1_temp[index].islower())
            if(literal1_temp[index].islower()):
             temp_list.append(literal1_temp[index])
             print("Temp_list after function is", temp_list)
             temp_list.append(literal2_temp[index])
             print("Temp_list after second variable is", temp_list)
             temp_variable= literal1_temp[index]
             for i in range(0, len(literal1_temp)):
               if(literal1_temp[i] ==temp_variable):
                print("helllo" , i)
                print("that is",literal2_temp[index] )
                literal1_temp[i]=literal2_temp[index]
                print("that is", literal1_temp[i] )
             for i in range(0, len(literal2_temp)):
              if(literal2_temp[i] ==temp_variable):
                literal2_temp[i]=literal2_temp[index]
            else:
                status = "FAIL"
                break
         else:
            notmatched = 0
            temp_list_sub = []
            
## Recursive Calling for function within function
            [Status,literal1,literal2,subval]= apply_substitution(literal1_temp[index][1:],literal2_temp[index][1:],temp_list_sub)
            print("returning the value",subval)
            print("literal values are", literal1, literal2)
            for  i in range(0, len(subval)//2):
                i = i*2
                for j in range(0, len(temp_list)//2):
                 j = j*2
                 print("literals are" , literal1_temp[index][0],literal2_temp[index][0])
                 if( temp_list[j] ==subval[i] and temp_list[j+1] ==subval[i+1]) and (literal1_temp[index][0]!=literal2_temp[index][0]):
                     notmatched = 1;
                     break
                if (notmatched== 1):
                 break
            if(notmatched== 1):
             temp_list.extend(subval)
             status="FAIL"
             break
       index=index+1
       status= "SUCCESS"       
     print("End values are", literal1_temp)
     print(literal2_temp)
     if(literal1_temp== [] and literal2_temp== []):
         status= "FAIL"
     print ("\n")
     print("temp_list in apply_substitution is" , temp_list, "status" , status)
     return status, literal1_temp , literal2_temp, temp_list
    
# this function is used for substituting the substitution in all the matching literals in the clauses.
def substitute_for_all(clause1, clause2,subexp):
       clause1pos = clause1[1]
       clause1neg = clause1[2]
       clause2pos = clause2[1]
       clause2neg = clause2[2]
       print("subexp is", subexp)
       for p in range(0, len(subexp)//2):
        p = p*2
        print("p is", p)
        for k in range(1, len(clause1)):
         for i in range(0, len(clause1[k])):
           clauseposneg = clause1[k][i]
           print("clause1", clause1, clauseposneg)
           for  j in range(0, len(clauseposneg)):
             print("clauseposneg[j]", clauseposneg[j])
             if(not(isinstance(clauseposneg[j],list))):
              if(clauseposneg[j] ==subexp[p]):                
                clauseposneg[j]= subexp[p+1]
             else:
              print("Entering inside the function", subexp)
              variableSubstitution(clauseposneg[j],subexp)
        print("exiting first")
        for k in range(1, len(clause2)):
         for i in range(0, len(clause2[k])):
           clauseposneg = clause2[k][i]
           print("clause2", clause2, clauseposneg)
           for  j in range(0, len(clauseposneg)):
             print("clauseposneg[j]", clauseposneg[j],"subexp is",subexp,subexp[p],subexp[p+1])
             if(not(isinstance(clauseposneg[j],list))):
               if(clauseposneg[j] ==subexp[p]):
                 clauseposneg[j]= subexp[p+1]
             else:
              print("Entering inside the function 2", subexp)
              variableSubstitution(clauseposneg[j],subexp)   
        print("exiting second")
        print("clause1 is", clause1,"clause2 is", clause2)


# this function is used for multiple clauses deduplication(Incase we have multiple literals with same predicate in clauses.)
def multiplePredicateDedup(clause1, clause2):
    clausepos1 = clause1[1]
    clauseneg1 = clause1[2]
    clausepos2 = clause2[1]
    clauseneg2 = clause2[2]
    posneg1    = []
    posneg2    = []
    print("doing for posneg case")
    print ("ALL the clauses" , clausepos1, clauseneg1, clausepos2, clauseneg2 )
    for i in range(0, len(clauseneg2)):
        posnegindex = 0
        templist = []
        for j in range(0, len(clausepos1)):
         if(clauseneg2[i]!= [] and clausepos1[j]!= []):
            if(clausepos1[j][0] ==clauseneg2[i][0]):
                emptylist= []
                print("clauses being sent are" , clausepos1[j][1:], clauseneg2[i][1:] )
                [status,lit1,lit2,subexp]= apply_substitution(clausepos1[j][1:], clauseneg2[i][1:],emptylist)
                if(status=="SUCCESS"):
                  posnegindex = posnegindex + 1
                  templist.append(j)
        if (posnegindex > 1):
                posneg1.extend(templist)
    for i in range(0, len(clausepos1)):
        posnegindex = 0
        templist = []
        for j in range(0, len(clauseneg2)):
          if(clauseneg2[j]!= [] and clausepos1[i]!= []):
            if(clausepos1[i][0] ==clauseneg2[j][0]):
                emptylist = []
                [status,lit1,lit2,subexp]= apply_substitution(clausepos1[i][1:], clauseneg2[j][1:],emptylist)
                if(status == "SUCCESS"):
                  posnegindex = posnegindex + 1
                  templist.append(j)
        if (posnegindex > 1): 
                posneg2.extend(templist)          
    print("doing for negpos case")
    negpos1 = []
    negpos2 = []
    for i in range(0, len(clausepos2)):
        negposindex = 0
        templist = []
        for j in range(0, len(clauseneg1)):
            print("length",len(clauseneg1), clauseneg1,j,len(clausepos2), clausepos2)
            if(clauseneg1[j]!= [] and clausepos2[i]!= []):
             if(clauseneg1[j][0] ==clausepos2[i][0]):
                emptylist = []
                [status,lit1,lit2,subexp]= apply_substitution(clauseneg1[j][1:], clausepos2[i][1:],emptylist)
                if(status == "SUCCESS"):
                   negposindex = negposindex + 1
                   templist.append(j)
        if (negposindex > 1): 
                negpos1.extend(templist)
    for i in range(0, len(clauseneg1)):
        negposindex = 0
        templist = []
        for j in range(0, len(clausepos2)):
          if(clauseneg1[i]!= [] and clausepos2[j]!= []):
            if(clausepos2[j][0] ==clauseneg1[i][0]):
                emptylist = []
                [status,lit1,lit2,subexp]= apply_substitution(clausepos2[j][1:], clauseneg1[i][1:],emptylist)
                if(status == "SUCCESS"):
                    negposindex = negposindex + 1
                    templist.append(j)
        if (negposindex > 1):        
                negpos2.extend(templist)
    print("returning postive-negative and negative-positive cases", posneg1,posneg2,negpos1,negpos2)
    return posneg1,posneg2,negpos1,negpos2

#this function is used for variable substitution
def variableSubstitution (clause_list1,subexp):
  print("subexp is", subexp)
  for p in range(0, len(subexp)//2):
    p = p*2
    print("p is", p)
  for k in range(0, len(clause_list1)):
       #if(not(isinstance(clauseposneg[j],list))):
        if(clause_list1[k] ==subexp[p]):                
          clause_list1[k]= subexp[p+1]
  return
#This is the resolution function
def resolve(clause_list1, clause_list2, index1, index2, Posneg):
  clause_list1_copy = copy.deepcopy(clause_list1)
  clause_list2_copy = copy.deepcopy(clause_list2)
  if(Posneg):
      clause_list1_copy[0].pop(index1)
      clause_list2_copy[1].pop(index2)  
  else:
      clause_list1_copy[1].pop(index1)
      clause_list2_copy[0].pop(index2)
  print(clause_list1_copy[0]+ clause_list2_copy[0],"break", clause_list1_copy[1]+ clause_list2_copy[1])
  return_list= []
  return_list= [clause_list1_copy[0]+ clause_list2_copy[0], clause_list1_copy[1]+ clause_list2_copy[1]]
  dedupemptylist= deduplicacy(return_list)
  return dedupemptylist

# this function is used for removing the duplicacy inside the function only.
def multiplefunctiondedup(clausepos):
  print("input clause is" , clausepos)
  deduplicacydone = []
  lengthoflist = len(clausepos)
  for i in range(lengthoflist):
      deduplicacydone.append(0)
  for i in range(lengthoflist):
    if(deduplicacydone[i] !=1):
      temp_variable = clausepos[i]
      print("element number is", i,temp_variable)
      for j in range(i+1, lengthoflist):
          if(clausepos[j]==temp_variable):
              deduplicacydone[j] = 1
              print("inside multifunctiondedup", clausepos[j],deduplicacydone[j])
    else:
         pass
  poslist = []
  for i in range(len(clausepos)):
      if(deduplicacydone[i]!=1):
        poslist. append(clausepos[i])
  return poslist

 # this function is used for removing the duplicacy by the resolution function.   
def deduplicacy(clauselist):
  print("clauselist for deduplicacy is", clauselist)
  for j in range(0, len(clauselist)):
     if (clauselist[j][0] == []and len(clauselist[j])== 1):
         pass
     else: 
      print("clauselist[j] is", clauselist[j])
      lenclauselist = len(clauselist[j])
      for i in range(0, lenclauselist):
        if(i< len(clauselist[j])):
          if (isinstance(clauselist[j][i],list) and len(clauselist[j][i])==0):
              clauselist[j].pop(i)

  print("returning clauselist is" , clauselist)
  return clauselist


# this function is used for checking the duplicacy (in case the generated clause is already present in the list and also used for sorting the clauses.)
def ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound,Clause):
  temp_list=[]
  if(status== "SUCCESS"):
    for number in range(1,resolvent_index+1):
      resolvent_list[0]=multiplefunctiondedup(resolvent_list[0])
      resolvent_list[1]=multiplefunctiondedup(resolvent_list[1])
      resolvent_list[0].sort()
      resolvent_list[1].sort()
      Clause[number][1].sort()
      Clause[number][2].sort()
      if (resolvent_list==Clause[number][1:]):
        duplicatefound=1
        print("Breaking away")
        break
    if (duplicatefound!=1):
      resolvent_index +=1
      temp_list = []
      temp_list = copy.deepcopy(resolvent_list)
      temp_list.insert(0, resolvent_index)
  return temp_list, resolvent_index, duplicatefound

# Main function
def main ():

  method = sys.argv[1]
  problem = sys.argv[2]
  global Premises_count
  Clause ={}
  print "===================================="
  print "* We have the following database *  "
  print "===================================="
 ### Defining Menu for Problem
  print "===================================="
  print "* First Order Logic Theorem Prover*"
  print "===================================="
  print "1. Howling Hound Problem (howling)"
  print "------------------------------------"
  print "2. Coyote Problem (rr)"
  print "------------------------------------"
  print "3. Drug Dealer Problem  (customs)"
  print "------------------------------------"
  print "4. Harmonia Problem "
  print "------------------------------------"
  print "5. Harmonia : Question Answer Solving "
  print "------------------------------------"
  print "6. Custom Problem  (Problem5)"
  print "------------------------------------ \n"
  #problem = input("Please enter the inputs in the format as you see in the text displayed above: ")

### Defining Menu for Method 
  print "\n===================================="
  print " * List of Methods * "
  print "===================================="
  print "1. Two - Pointer Method (two-pointer)"
  print "------------------------------------"
  print "2. Unit - Preference Method (unit-preference)"
  print "------------------------------------ \n"
  if method == "two-pointer":
    InputOuterLoopIndex = int(sys.argv[3])-1
  else:
    InputOuterLoopIndex = 4
  #method = input("Please enter the inputs in the format as you see in the text displayed above: ")
  if problem == "howling":
  # test input for howling hound problem:
    Premises_count = InputOuterLoopIndex
    resolvent_index = Premises_count + 3
    Clause[1] = [1, [['howl',  'z']], [['hound' ,'z']]]
    Clause[2] = [2, [[]], [['have', 'x', 'y'], ['cat', 'y'], ['have', 'x',  'z'] ,['mouse', 'z']]]
    Clause[3] = [3, [[]],[[ 'ls' ,'w'], ['have' ,'w', 'v'] ,['howl', 'v']]]
    Clause[4] = [4, [['have', 'JOHN' ,'A']], [[]]]
    Clause[5] = [5, [['cat' , 'A'],[ 'hound', 'A']], [[]]]
    Clause[6] = [6, [['mouse' , 'B']] , [[]]]
    Clause[7] = [7, [['ls' ,'JOHN']], [[]]]
    Clause[8] = [8, [['have' , 'JOHN' , 'B' ]] , [[]]]
  elif problem == "roadrunner":
  #test input for coyote problem
    Premises_count = InputOuterLoopIndex
    resolvent_index = Premises_count + 2
    Clause[1] = [1, [['rr', 'A']], [['coyote','y']]]
    Clause[2] = [2, [['chase', 'z', 'A']], [['coyote' ,'z']]]
    Clause[3] = [3, [['smart' , 'x']], [['rr', 'x'],['beep', 'x']]]
    Clause[4] = [4, [[]], [['coyote', 'w'],['rr','u'],['catch', 'w','u'],['smart','u']]]
    Clause[5] = [5, [['frustrated', 's'], ['catch','s','t']],[['coyote','s'],['rr', 't'],['chase', 's' ,'t']]]				
    Clause[6] = [6, [['beep', 'r']], [['rr', 'r']]]
    Clause[7] = [7, [[ 'coyote', 'B']], [[]] ] 
    Clause[8] = [8, [[]], [['frustrated', 'B']]]
  elif problem == "drugdealer":
  #test input for drug dealer problem
    Premises_count = InputOuterLoopIndex
    resolvent_index = Premises_count + 1
    Clause[1] = [1, [['v' ,'x'],['s','x',['f','x']] ],[['e','x']]]
    Clause[2] = [2, [['v', 'y'],['c',['f', 'y']] ],[['e', 'y'] ] ]
    Clause[3] = [3, [['e', 'A'] ], [[]] ]
    Clause[4] = [4, [['d', 'A']], [[]] ]
    Clause[5] = [5, [['d', 'z']],[['s', 'A','z']]]
    Clause[6] = [6, [[]], [['d','w'],['v','w']]]
    Clause[7] = [7, [[]],[['d','r'],['c','r']]]
  elif problem == "Harmonia":
  #test input for harmonia problem
    Premises_count = InputOuterLoopIndex
    resolvent_index = Premises_count + 1
    Clause[1] = [1,[['Grandparent','x','y']],[['Parent','x','z'],['Parent','z','y']] ] 
    Clause[2] = [2,[['Parent','x','y']],[['Mother','x', 'y']]]
    Clause[3] = [3,[['Parent','x','y']],[['Father','x', 'y']]]
    Clause[4] = [4,[['Father','ZEUS','ARES']],[[]]]
    Clause[5] = [5,[['Mother','HERA','ARES']],[[]]]
    Clause[6] = [6,[['Father','ARES','HARMONIA']],[[]]]
    Clause[7] = [7,[[]],[['Grandparent','x','HARMONIA']]]

  elif problem == "HarmoniaAnswer":
  #test input for harmonia problem
   Premises_count = InputOuterLoopIndex
   resolvent_index = Premises_count + 1
   Clause[1]= [1,[['Grandparent','x','y']],[['Parent','x','z'],['Parent','z','y']] ] 
   Clause[2]= [2,[['Parent','x','y']],[['Mother','x', 'y']]]
   Clause[3]= [3,[['Parent','x','y']],[['Father','x', 'y']]]
   Clause[4]= [4,[['Father','ZEUS','ARES']],[[]]]
   Clause[5]= [5,[['Mother','HERA','ARES']],[[]]]
   Clause[6]= [6,[['Father','ARES','HARMONIA']],[[]]]
   Clause[7]= [7,[[]],[['Answer','x']]]
   Clause[8]= [8,[['Answer','x']],[['Grandparent','x','HARMONIA']]]

  elif problem == "Problem5":
  #test input for custom problem
    Premises_count = InputOuterLoopIndex
    resolvent_index = Premises_count + 1
    Clause[1] = [1,[['Conservative','x'],['Armadillo','A']],[['Austinite','x']]]
    Clause[2] = [2,[['Conservative','y'],['Loves','y','A']],[['Austinite','y']]]
    Clause[3] = [3,[['Aggie','z']],[['Wears','z']]]
    Clause[4] = [4,[['Loves','r','w']],[['Aggie','r'],['Dog','w']]]
    Clause[5] = [5,[['Dog','B']],[['Armadillo','v'],['Loves','w','v']]]
    Clause[6] = [6,[[]],[['Loves','w','B'],['Armadillo','v'],['Loves','w','v']]]
    Clause[7] = [7,[['Austinite','CLEM']],[[]]]
    Clause[8] = [8,[['Wears','CLEM']],[[]]]
    Clause[9] = [9, [['Conservative', 'CLEM']], [[]]]
    Clause[10]= [10,[[]],[['Conservative','u'],['Austinite','u']]]
    
  else:
    print "Wrong Choice Selected! Please enter between (1 - 6)....." 
    exit()
  
  #method = 1 (THis is the two-pointer Method)
  if method == "two-pointer":
   OL = Premises_count + 1
   status = "Fail"
   clause_resolved = 0
   print(len(Clause))
   while (OL <= len(Clause)):
     print(len(Clause))
     print("OL=", OL)
     IL = 0
     while (IL!=OL):
       IL +=1
       resolvent_list = []
       clausecopy = []
       duplicatefound = 0
       print (IL,OL)
       print("CLAUSE_Resolved_are having index:","FirstCLauseIndex=",IL, Clause[IL],"Second_clause_index=",OL, Clause[OL])
       [ posnegind1, posnegind2, negposind1, negposind2] = multiplePredicateDedup(Clause[IL], Clause[OL])
       if( posnegind1== [] and posnegind2 == [] and negposind1 == [] and  negposind2 == []):
         print("inside all empty")
         [status,resolvent_list]= unification(Clause[IL], Clause[OL])
         print(status,resolvent_index+1,resolvent_list,duplicatefound)
         [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
         if((status=="SUCCESS") and duplicatefound!= 1):
           Clause[resolvent_index] = temp_list
           if (resolvent_list[0][0] == [] and resolvent_list[1][0] == []):
               clause_resolved = 1;
               break
       if(posnegind1 != []):
          print("inside posnegind1 nonempty")
          for i in (posnegind1):
              clausecopy = copy.deepcopy(Clause[IL])
              RemoveValue = clausecopy[1][i]
              clausecopy[1].pop(i)
              clausecopy[1].append(RemoveValue)
              [status,resolvent_list]= unification(clausecopy, Clause[OL])
              [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
              if((status=="SUCCESS") and duplicatefound!= 1):
                Clause[resolvent_index] = temp_list
                if (resolvent_list[0][0] == [] and resolvent_list[1][0] == []):
                   clause_resolved = 1;
                   break
       if(posnegind2 != []):
          StoreValue = []
          print("inside posnegind2 empty")
          for i in (posnegind2):
              clausecopy = copy.deepcopy(Clause[OL])
              RemoveValue = clausecopy[2][i]
              clausecopy[2].pop(i)
              clausecopy[2].append(RemoveValue)
              [status,resolvent_list]= unification(Clause[IL], clausecopy)
              [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
              if((status=="SUCCESS") and duplicatefound!= 1):
                  Clause[resolvent_index] = temp_list
                  if (resolvent_list[0][0] == [] and resolvent_list[1][0] == []):
                      clause_resolved = 1;
                      break
       if(negposind1 != []):
          print("inside negposind1 empty")
          for i in (negposind1):
              clausecopy = copy.deepcopy(Clause[IL])
              RemoveValue = clausecopy[2][i]
              clausecopy[2].pop(i)
              clausecopy[2].append(RemoveValue)
              [status,resolvent_list]= unification(clausecopy, Clause[OL])
              [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
              if((status=="SUCCESS") and duplicatefound!= 1):
                  Clause[resolvent_index] = temp_list
                  if (resolvent_list[0][0] == [] and resolvent_list[1][0] == []):
                      clause_resolved = 1;
                      break
       if(negposind2 != []):
          print("inside negposind2 empty")
          for i in (negposind2):
              clausecopy = copy.deepcopy(Clause[OL])
              RemoveValue = clausecopy[1][i]
              clausecopy[1].pop(i)
              clausecopy[1].append(RemoveValue)
              [status,resolvent_list]= unification(Clause[IL], clausecopy)
             # resolvent_list[0].append(Storevalue)
              [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
              if((status=="SUCCESS") and duplicatefound!= 1):
                  Clause[resolvent_index] = temp_list
                  if (resolvent_list[0][0] == [] and resolvent_list[1][0] == []):
                      clause_resolved = 1;
                      break     

       if(IL==OL-1):
         if(OL==len(Clause)):
             OL+=1
             break
         else:
           IL =0 
           OL +=1;
      
     if(clause_resolved): 
        break
   print("Status of the method:")
   print(status)
   if(clause_resolved):
       print("Clauses are resolved")
   else:
       print("Method was not successful")
   for i in range(1, resolvent_index+1):
       print(Clause[i])
  # if(problem == 5):
   for i in range(1, len(Clause)):
       for j in range(len(Clause[i][1])):
         if(Clause[i][2][0]==[] and Clause[i][1][j][0]=='Answer' and Clause[i][1][j][1].isupper()):
            print("The answer is",Clause[i][1][j][1])

# this method is for the unit-prefernce fucntion call.
  elif method == "unit-preference":
    resolvent_index = len(Clause)
    if PointerIndexMover(Clause, resolvent_index):
      print ("Method is over")
  else:
    print ("Wrong Method Entered! Please enter either 1 or 2.....")

# Sorting function used for sorting based on the number of Literals in the clauses.
def SortingFunc(Clause, resolvent_index):
  SortingList = []
  SortedList = []
  for i in range(1,resolvent_index+1):
     temp_list= []
     emptyClause = 0
     for j in range(len(Clause[i][1])):
         if(Clause[i][1][j]==[]):
             emptyClause +=1
     for k in range(len(Clause[i][2])):
         if(Clause[i][2][k]==[]):
             emptyClause +=1
     temp_list.append(len(Clause[i][1]+Clause[i][2]) - emptyClause)
     temp_list.append(i)
     SortingList.append(temp_list)
     print (SortingList)
  SortedList = sorted(SortingList, key = itemgetter(0))
  return SortedList

# This function is used for moving the index for both innner loop pointer and outer loop pointer in case of Unit-Preference
def PointerIndexMover(Clause, resolvent_index,IL=0,OL=1):
  appended_Clause = []    
  SortedList = SortingFunc(Clause, resolvent_index)
  gameover = 0
  [appended_Clause, resolvent_index, status, clauseresolved] = UnitPref(Clause, SortedList,resolvent_index)
  while(clauseresolved != 1):
    if status == "SUCCESS":
      SortedList = SortingFunc(Clause, resolvent_index)
      IL = 0
      OL = 1
    else:
      if IL==len(SortedList):
        gameover = 1
        break
      else:
        if OL == len(SortedList)-1:
          print ("Printing the valus of IL and  OL",IL, OL)
          IL = IL + 1
          OL = IL + 1
        else:
          OL = OL + 1
    [appended_Clause, resolvent_index, status, clauseresolved]=UnitPref(Clause,SortedList, resolvent_index, IL, OL)
  print ("Theorem Proved!")
  print("The list of  Clauses is")
  for i in range(1, resolvent_index+1):
       print(Clause[i])
  return True
 
 # this function is the unit Preference Function .      
def UnitPref(Clause, SortedList, resolvent_index, IL = 0, OL = 1):
  global Premises_count
  status = "Fail"
  clauseresolved = 0
  temp_finished = 0
  resolvent_list = []
  clausecopy = []
  duplicatefound = 0
  print("CLAUSE_Resolved_are having index:","FirstCLauseIndex=",IL,Clause[SortedList[IL][1]],"Second_clause_index=",OL,Clause[SortedList[OL][1]])
  [ posnegind1, posnegind2, negposind1, negposind2] = multiplePredicateDedup(Clause[SortedList[IL][1]], Clause[SortedList[OL][1]])
  if( posnegind1== [] and posnegind2 == [] and negposind1 == [] and  negposind2 == []):
    print("inside all empty")
    [status,resolvent_list]= unification(Clause[SortedList[IL][1]], Clause[SortedList[OL][1]])
    [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
    if((status=="SUCCESS") and duplicatefound!= 1):
      Clause[resolvent_index] = temp_list
      if resolvent_list[0][0] == [] and resolvent_list[1][0] == []:
        clauseresolved = 1;
      return Clause, resolvent_index, status,clauseresolved
    else:
      status = "FAIL"
      print("satus" , status)
      return Clause, resolvent_index, status, clauseresolved

  if(posnegind1 != []):
    print("inside posnegind1 nonempty")
    for i in (posnegind1):
        clausecopy = copy.deepcopy(Clause[SortedList[IL][1]])
        RemoveValue = clausecopy[1][i]
        clausecopy[1].pop(i)
        clausecopy[1].append(RemoveValue)
        [status,resolvent_list]= unification(clausecopy, Clause[SortedList[OL][1]])
        [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
        if((status=="SUCCESS") and duplicatefound!= 1):
           status = "SUCCESS"
           OneSuccessStatus = 1
           Clause[resolvent_index] = temp_list
           if resolvent_list[0][0] == [] and resolvent_list[1][0] == []:
               clauseresolved = 1;
               break 
        else:
           status = "FAIL"
    if(OneSuccessStatus ==1):
            status = "SUCCESS"
    return Clause, resolvent_index, status, clauseresolved
  if(posnegind2 != []):
    StoreValue = []
    print("inside posnegind2 empty")
    OneSuccessStatus = 0
    for i in (posnegind2):
        clausecopy = copy.deepcopy(Clause[SortedList[OL][1]])
        RemoveValue = clausecopy[2][i]
        clausecopy[2].pop(i)
        clausecopy[2].append(RemoveValue)
        [status,resolvent_list]= unification(Clause[SortedList[IL][1]], clausecopy)
        [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
        if((status=="SUCCESS") and duplicatefound!= 1):
           status = "SUCCESS"
           OneSuccessStatus = 1
           Clause[resolvent_index] = temp_list
           if resolvent_list[0][0] == [] and resolvent_list[1][0] == []:
               clauseresolved = 1;
               break 
        else:
           status = "FAIL"
    if(OneSuccessStatus ==1):
            status = "SUCCESS"
    return Clause, resolvent_index, status, clauseresolved
  if(negposind1 != []):
    print("inside negposind1 empty")
    for i in (negposind1):
        clausecopy = copy.deepcopy(Clause[SortedList[IL][1]])
        RemoveValue = clausecopy[2][i]
        clausecopy[2].pop(i)
        clausecopy[2].append(RemoveValue)
        [status,resolvent_list]= unification(clausecopy, Clause[SortedList[OL][1]])
        [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
        if((status=="SUCCESS") and duplicatefound!= 1):
           status = "SUCCESS"
           OneSuccessStatus = 1
           Clause[resolvent_index] = temp_list
           if resolvent_list[0][0] == [] and resolvent_list[1][0] == []:
               clauseresolved = 1;
               break 
        else:
           status = "FAIL"
    if(OneSuccessStatus ==1):
            status = "SUCCESS"
    return Clause, resolvent_index, status, clauseresolved
  if(negposind2 != []):
    print("inside negposind2 empty")
    for i in (negposind2):
        clausecopy = copy.deepcopy(Clause[SortedList[OL][1]])
        RemoveValue = clausecopy[1][i]
        clausecopy[1].pop(i)
        clausecopy[1].append(RemoveValue)
        [status,resolvent_list]= unification(Clause[SortedList[IL][1]], clausecopy)
        [temp_list,resolvent_index,duplicatefound] =  ClauseListDeduplicator(status,resolvent_index,resolvent_list,duplicatefound, Clause)
        if((status=="SUCCESS") and duplicatefound!= 1):
           status = "SUCCESS"
           OneSuccessStatus = 1
           Clause[resolvent_index] = temp_list
           if resolvent_list[0][0] == [] and resolvent_list[1][0] == []:
               clauseresolved = 1;
               break 
        else:
           status = "FAIL"
    if(OneSuccessStatus ==1):
            status = "SUCCESS"
    return Clause, resolvent_index, status, clauseresolved
  return Clause, resolvent_index, status, clauseresolved
if __name__ == '__main__':
   main()
