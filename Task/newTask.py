import collections
# test_case=int(input())
# for i in range(test_case):
#     inputs = int(input())
#     name=[0 for r in range(inputs)]
#     tweet=[0 for r in range(inputs)]
#     for j in range(inputs):
#         name[j],tweet[j] = input().split()
#     freq={}
#     for item in name:
#         if item in freq:
#             freq[item]+=1
#         else:
#             freq[item]=1
#     all_values = freq.values()
#     max_value = max(all_values)
#     for key,value in freq.items():
#         if value == max_value:
#             print(key, value)
#
res = lambda a,b: a*b
s = "mango is a is bold fruit"
a = s.split()

print(collections.Counter(a))
