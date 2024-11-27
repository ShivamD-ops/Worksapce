a,b,c,d = 2,3,4,5

print(f"using f-strings -> \na->{a}\nb->{b}\nc->{c}\nd->{d}")

print("Using .format()-->\na->{}\nb->{}\nc->{}\nd->{}".format(a,b,c,d))

# f-string allows to use embed expressions
#  directly inside string literals thus 
#  improving readability and clear what 
#  values are being used.