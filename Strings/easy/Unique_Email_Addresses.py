emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

s = set()
for i in emails:
    a1 = i.split('@')[0]
    a2 = a1.split('+')
    a = a2[0].replace('.', '') + '@' + i.split('@')[1]
    s.add(a)

print(len(s))
