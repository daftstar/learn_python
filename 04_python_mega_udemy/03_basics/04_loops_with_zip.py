names = ['james', 'john', 'kool-aid-man', 'terrible']
email_domains = ['gmail', 'hotmail', 'yahoo', 'comcast']

for i, j in zip(names, email_domains):
    print ("%s@%s.com" %(i, j))
