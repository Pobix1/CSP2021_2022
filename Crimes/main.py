import matplotlib.pyplot as plt

#open crimes2019.txt

violentCrimesFile = open("crimes2019.txt")

crimelist = violentCrimesFile.readlines()
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 ,2009, 2010,2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

for i in range(len(crimelist)):
    crimelist[i]=int(crimelist[i])

print(crimelist)

plt.clf()

plt.plot(years, crimelist, marker = 's', linestyle = "--")
plt.axis([2000, 2019, 1100000, 1500000])
plt.ylabel("Violent Crimes")
plt.xlabel("Year")
plt.show()

