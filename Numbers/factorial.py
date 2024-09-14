s=str(input().split())
a="AEIOUaeiou"
c=0
for i in range(len(s)):
    if s[i] in a:
        c+=1
fact=1
for i in range(c):
    fact*=(i+1)
print(fact)
