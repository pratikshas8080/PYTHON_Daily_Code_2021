s = "Pratiksha"
print(len(s))
print(s[0])
print(s[1:3])
print(s[-1])
print(s[1:])
print(s[0:3])
print(s[:8])
print(s[:])
print(s + " " + "Sawandkar")
print(s * 8)

S1 = "shrubbery"
L = list(S1)  # Expand to a List :[.......]
print(L)
L[1] = "c"  # change it in place
"".join(L)  # joine with empty delimiter
print(L)

B = bytearray(b"Spam")
B.extend(b"eggs")
print(B.decode())

k = "sattyapatil"
print(k.find("pa"))  ## Find the offset of a substring in S
print(k.replace("pa", "xyz"))  # Replace occurrences of a string in S with another
