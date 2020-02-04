flagWithStarts = ["Australia", "Azerbaijan", "Bosnia and Herzegovina", "Brazil", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Chile", "China", "Comoros", "Croatia", "Cuba", "Djibouti", "Dominica", "East Timor", "Equatorial Guinea", "Ethiopia", "Federated States of Micronesia", "Ghana", "Grenada", "Guinea-Bissau", "honduras", "Israel", "Jordan", "Kosovo", "Liberia", "Malaysia", "Marshall Islands", "Morocco", "Myanmar", "Nauru", "Nepal", "New Zealand", "North Korea", "Northern Mariana Islands", "Panama", "Papua New Guinea", "Paraguay", "Philippines", "Saint Kitts and Nevis", "Samoa", "Sao Tome and Principe", "Senegal", "Singapore", "Slovenia", "Solomon Islands", "Somalia", "South Sudan", "Suriname", "Syria", "Tajikistan", "Togo", "Turkmenistan", "Tuvalu", "United States", "Uzbekistan", "Venezuela", "Vietnam"]
americaCountries = ["Antigua and Barbuda", "Argentine Republic↵", "Commonwealth of The Bahamas", "Barbados", "Belize", "Plurinational State of Bolivia↵", "Federative Republic of Brazil↵", "Canada", "Republic of Chile↵", "Republic of Colombia↵", "Republic of Costa Rica↵", "Republic of Cuba↵", "Commonwealth of Dominica", "Dominican Republic↵", "Republic of Ecuador↵", "Republic of El Salvador↵", "Grenada", "Republic of Guatemala↵", "Co-operative Republic of Guyana", "Republic of Haiti", "Republic of Honduras↵", "Jamaica", "United Mexican States", "Republic of Nicaragua", "Republic of Panama", "Republic of Paraguay", "Republic of Peru", "Federation of Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Republic of Suriname", "Republic of Trinidad and Tobago", "United States of America", "Oriental Republic of Uruguay", "Bolivarian Republic of Venezuela"]
flagWithSun = ["Antigua and Barbuda", "Argentine", "Bangladesh", "Japan", "Kazakhstan", "Kiribati", "Malawi", "Macedonia", "Namibia", "Nepal", "Niger", "Rwanda", "Philippines", "South Korea (one of the trigrams represents the Sun)", "Taiwan", "Uruguay"]

cu = []

for flag in flagWithStarts:
    for ac in americaCountries:
        if str.lower(ac).find(str.lower(flag))!=-1 or str.lower(ac) == str.lower(flag):
            cu.append(flag)

cu2=[]
for flag in flagWithSun:
    for ac in americaCountries:
        if str.lower(ac).find(str.lower(flag))!=-1 or str.lower(ac) == str.lower(flag):
            cu2.append(flag)
cu = set(cu)
cu2 = set(cu2)

print(len(cu)," - starts")
print(cu)
print(len(cu2),"  - suns")
print(cu2)