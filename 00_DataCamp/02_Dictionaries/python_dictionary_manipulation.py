europe = {
        'spain': 'madrid',
        'france': 'paris',
        'germany': 'berlin',
        'norway': 'oslo'
        }

# add key italy w/ value rome to europe
europe["italy"] = "rome"

# selectively print a country
print (europe["italy"])

# print if italy exists in europe
print ("italy" in europe)

# add poland: warsaw to europe
europe["poland"] = "warsaw"

# print (europe)



europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }


# change value of key Germany to berlin
europe["germany"] = "berlin"


# remove australia from dictionary
del europe["australia"]

print (europe)