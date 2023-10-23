import re

txt ="The ain in Spain"
x=re.findall(r"^ain",txt)
print(x)

pattern=re.compile(r"\b\w{5}\b")

res=pattern.findall("Jessa and Kelly")
print(res)

target_string="Jessa loves Python and pandas"

pater=r"\w{6}"
# match() method
# result = re.match(pattern, target_string)
# print(result)
# Output None
result=re.findall(pater,target_string)
print(result)