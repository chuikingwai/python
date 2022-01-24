import re





log = "Joe, Kim"

pattern = "^."
pattern1 = "^."
pattern2 = "[^A-z]$"
pattern3 = ".*"

pattern4 = "^(\w*), (\w*)$"

result = re.search(pattern4,log)

print(result.groups())


print("{} {} {} ".format(result[0] , result[1],  result[2]))
print(result[0] + " :: " + result[1])

result = re.sub('abc(def)(ghi)',r'\1test\2',"111abcdefghi222")

print(result)
