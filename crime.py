import state_crime
import matplotlib.pyplot as plt
import numpy as np
crimelist = state_crime.get_all_crimes()


emptydictionary = { }

for elem in range(len(crimelist)):
    if crimelist[elem]["Year"] == 2012:
            if crimelist[elem]["State"] != "United States":
                State = crimelist[elem]["State"]
                Totalnum = crimelist[elem]["Data"]["Totals"]["Violent"]["All"]
                emptydictionary[State] = Totalnum
top10 = []

for i in emptydictionary:
    if emptydictionary[i] >= 34595:
        top10.append(emptydictionary[i])


x = np.arange(10)

plt.bar(x, top10, align = 'center', color = "pink")
plt.xticks(np.arange(10), ("CA", "FL", "GA", "IL", "MI", "NY", "OH", "PA", "TN", "TX"))
plt.title("Top Ten States with Highest Crime Rates in 2012")
plt.show()
