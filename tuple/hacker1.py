# # # from itertools import combinations
# # # s,n=input().split()
# # # for i in s:
# # #     print(i)
# # # comb=list(combinations(sorted(s),int(n)))

# # # for i in range(len(comb)):
# # #     for j in range(len(comb[i])-1):
# # #         print(comb[i][j]+comb[i][j+1])
# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # # t=int(input())
# # # for i in range(t):
# # #     a,b=input().split()
# # #     # print(a,type(a),b)


# # #     try:
# # #         div=int(a)/int(b)
# # #         print(int(div))
# # #     except ZeroDivisionError:
# # #         print("Error Code: integer division or modulo by zero")
# # #     except ValueError:
# # #         if a.isnumeric():
# # #             print(f"Error Code: invalid literal for int() with base 10: '{b}'")
# # #         elif b.isnumeric():
# # #             print(f"Error Code: invalid literal for int() with base 10: '{a}'")
# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# # m = input()
# # m_set = set(map(int, input().split()))
# # n = input()
# # n_set = set(map(int, input().split()))
# # y=m_set.symmetric_difference(n_set)
# # y=list(y)
# # print(y)
# # for i in y:
# #     print (i)
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# # t=int(input())
# # for i in range(t):
# #     n=int(input())
# #     ele=set(map(int,input().split()))
# #     l=int(input())
# #     ele1=set(map(int,input().split()))
   
# #     if ele.issubset(ele1):
# #         print("True")
# #     else:
# #         print("False")
# # import textwrap
# # def merge_the_tools(string, k):
# #     str_len=len(string)
# #     substr=textwrap.wrap(string,k)
# #     d={}
# #     for i in substr:
# #         print(set(i))
# # string, k = input(), int(input())
# # merge_the_tools(string, k)
# # def sub(string_,k):
# #     if len(string_)<k:
# #         return []
# #     else:
# #         return [string_[:k]]+sub(string_[k:],k)
# # w=[]

# # my_lst=sub("AABCAAADA",3)



    
       
# # st="AAB"
# # l=len(st)
# # w=[]
# # for i in range(l):
# #     if st[i] not in w:
# #             w.append(st[i])
# # print(w)
# # txt="".join(w)
# # print(txt)

# # string = "AABCAAADA"
# # w=3
# # lst = []
# # f_lst = []
# # for i in range(0,len(string),w):
# #     lst.append(string[i:i+w])
# # for i in lst:
# #     st = []
# #     for j in i:
# #         if j not in st:
# #             st.append(j)
# #     f_lst.append(''.join(st))
# # print(f_lst)
# # for i in f_lst:
# #     print(i)
 
# # def merge_the_tools(string, k):
# #     lst=[]
# #     f_lst = []
    
# #     for i in range(0,len(string),k):
# #         lst.append(string[i:i+k])
# #     for i in lst:
# #         st = []
# #         for j in i:
# #             if j not in st:
# #                 st.append(j)
# #         f_lst.append(''.join(st))
# #     for x in f_lst:
# #         print(x)
        

# # if __name__ == '__main__':
# #     string, k = input(), int(input())
# #     merge_the_tools(string, k)
# # from itertools import groupby
# # data="AAAABBBCCCDDDAA"
# # groups = []
# # uniquekeys = []
# # data = sorted(data)
# # ml=[k for k, g in groupby('AAAABBBCCDAABBB')]
# #     # groups.append(list(g))      # Store group iterator as a list
# #     # uniquekeys.append(k)
# # print(ml)
# # print(groups)
# # print(uniquekeys)
# # def solve(s):
# #     my_str = s.split(" ")
# #     new_str =[]
# #     for i in my_str:
# #         new_str.append(i.capitalize())
# #     return (" ".join(new_str))
        
     


# # s = input()

# # result = solve(s)
# # print(result)
# # import math
# # ab=int(input())
# # bc=int(input())
# # ac=round(math.sqrt(ab**2+bc**2))
# # print(ac)
# # mc=round(ac/2)
# # print(mc)
# # x=(math.atan(ab/bc))
# # print(x)
# # # angle_mcb=(math.atan(x))
# # print(round(math.degrees(x)))
# # 1
# # 121
# # 12321
# # 1234321
# # for i in range(1,int(input())+1): 
# #     print(((10**i)//9)**2)
# # n=int(input("enter the number"))
# # stri=""
# # for i in range(1,n+1):
# #     stri=stri+str(i)
# #     print(stri+stri[-2::-1])
# #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys




# # first_multiple_input = input().rstrip().split()

# # n = int(first_multiple_input[0])

# # m = int(first_multiple_input[1])

# # matrix = []
# # lst=[]
# # sub_=[]



# # for _ in range(n):
# #     matrix_item = input()
# #     matrix.append(matrix_item)
# # print(matrix)
# # for i in matrix:
# #     for j in range(1):
       
# #        sub_.append(i[0])
# # for i in matrix:
# #     for j in range(1):
       
# #        sub_.append(i[1])
# # for i in matrix:
# #     for j in range(1):
       
# #        sub_.append(i[2])

# # # for i in decode_:
# # #     for j in range(len(i)):
       
# # #        sub_.append(i[0][1])

# # print(sub_)
# import math
# import os
# import random
# import re
# import sys




# s = input()
# i = 0
# if len(s)==1:
#         print("("+str(1)+", "+str(s[0])+")",end = " ")
# while( i < len(s) - 1):
 
       
#         count = 1
 
#         while s[i] == s[i + 1]:
 
#             i += 1
#             count += 1
             
#             if i + 1 == len(s):
#                 break
         
#         print("(",str(s[i]) ,",",str(count),")",end = " ")
#         i += 1

        
# def solve(s):
#     my_str = s.split(" ")
#     new_str =[]
#     for i in my_str:
#         new_str.append(i.capitalize())
#     return (" ".join(new_str))
# st=input()
# result=solve(st)
# print(result)

# N=int(input())
# lst=[]
# c=[]
# for i in range(N):
#     txt = input("Enter a string: ")
#     lst.append(txt)
# print(lst)
# count = 1
# for i in lst:
   
    
#     if i not in c:
#         c.append(i)
#         count += 1
#     print(f"Character '{i}' occurs {count} times.")


# words = ['hello', 'goodbye', 'howdy', 'hello', 'hello', 'hi', 'bye']

# count = 0
# lst=[]
# for i in words:
#         lst.append(i)
#         if i in lst:
            
#             count = count + 1
#             print(i,count)
# from collections import Counter,OrderedDict
# ordered_dict = OrderedDict()
# for i in range(int(input())):
#     string = input()
#     if string in ordered_dict:
#         ordered_dict[string] += 1
#         # value_lst.append(('len'))
#     else:
#         ordered_dict[string] = 1
# # print(ordered_dict)
# print(len(ordered_dict.keys()))
# print(*ordered_dict.values())

# romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# s = 'MCMXCIV'     
# rvalue = 0  
# i=0
# while i<len(s):
#     if i>0 and i<len(s)-1 and romans[s[i]] < romans[s[i + 1]]:
#         rvalue += romans[s[i+1]]-romans[s[i]]
#         i+=1
#     else:
#         rvalue += romans[s[i]]
#     i+=1
#     print(i)
#     print(rvalue)
# sub=[]
# s=input()
# long_len=0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#             if len(set(s[i:j])) == len(s[i:j]) and long_len<len(s[i:j]):
#                 sub.append(s[i:j])
#                 long_len=len(s[i:j])
# print(long_len)


# longest_string = ''
# for i in sub:
#     if len(i) > len(longest_string):
#         longest_string = i
# print(len(longest_string))

# print(set('pturpp'))


# i=0
# sub_str = ''
# while i<len(s):
#     for i in s:
#         if i not in sub_str:
#             sub_str+=i
#             print(sub_str)


# sub=''      
# for i in s:
#     if i not in sub:
#         sub+=i
# print(sub)
# s="abcabcdbb"
# char={}  
# max_length=0
# j=0
# for i in range(len(s)):
#     if s[i] in char:
        

# print(max_length)
  

# s=input()
# lst=s.split()
# print(lst)
# print(len(lst[-1]))


# nums=[2]
# val=3
# if not nums:
#     print(0)
        
# for i in range(len(nums)):
#     if val in nums:
#         nums.remove(val)
           
# print(i)
# print(nums)

lst = [3,5,5,5,5,6]
val=5


while val in lst:
    lst.remove(val)
print(lst)



