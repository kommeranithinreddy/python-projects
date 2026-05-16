
O= [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]



input_List = ['aaa', 'nat', 'tan', 'ate', 'eat', 'tea']

Main_List = [] #Output List
Inner_List = [] #for making inner Lists
Rm_Dup = [] #To remove duplicate inner Lists

for i in input_List:
    if i not in Rm_Dup: # if i is already an anagram >> it'll skip here to add it 
        Inner_List.append(i)
        Rm_Dup.append(i) #Adding element to Rm Duplicate list to skip for next time
    for j in input_List:
        ct1 = 0
        ct2 = 0
        
        for k in range(len(i)):
            if i != j and i[k] in j and j not in Rm_Dup: #Rm_Dup is for skipping past data
                ct1 += 1
            if i != j and j[k] in i and j not in Rm_Dup: #Rm_Dup is for skipping past data
                ct2 += 1
            
        if ct1 == 3 and ct2 == 3:
            Inner_List.append(j)
            Rm_Dup.append(j) #Adding j element if it's anagram. So, it'll be skipped
    if Inner_List != []:
        Main_List.append(Inner_List)
        Inner_List = []
    


print(Main_List)

        
            
