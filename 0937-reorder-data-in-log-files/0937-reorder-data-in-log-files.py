# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letlog=[]
#         diglog=[]
#         for i in logs:
#             if i.split(' ')[1].isnumeric():
#                 diglog.append(i)
#             else:
#                 letlog.append(i)
        
#         for i in range(len(letlog)):
#             new=letlog[i].split(' ')
#             new=new[1:]+[new[0]]
#             letlog[i]='#'.join(new)
#         letlog.sort()
#         for i in range(len(letlog)):
#             new=letlog[i].split('#')
#             new=[new[-1]]+new[:-1]
#             letlog[i]=' '.join(new)
#         final=[]
#         final=final+letlog
#         for i in diglog:
#             final.append(i)
            
#         return final

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort_key(log):
            identifier, content = log.split(' ', 1)
            return (0, content, identifier) if content[0].isalpha() else (1,)

        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split(' ')[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=custom_sort_key)

        return letter_logs + digit_logs
                
                
                
                