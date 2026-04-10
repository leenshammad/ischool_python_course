# task:find_common_list
# input:n/a
# output:common_list


def find_common_list(list1,list2):
    common_list=[]
    for i in list1:
        for j in list2:
            if i==j and i not in common_list:
                common_list.append(i)
    return common_list


list1=['1','2','3','4','5','6']
list2=['4','6','7','2','9','4']

print(find_common_list(list2,list1))
