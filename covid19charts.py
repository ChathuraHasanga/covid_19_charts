import numpy
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([90500,60300,47100,32600,22800,48600,115000,124000,96400,127000,69800])

plt.subplot(3,3,1)
plt.plot(x,y, color='red', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("Russian Federation")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([3900,3900,3800,10500,20200,21000,17200,18800,11800,11200,10300])

plt.subplot(3,3,2)
plt.plot(x,y, color='orange', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("Greece")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([78300,10000,17600,21800,10700,6300,4100,2600,5500,6200,5200])

plt.subplot(3,3,3)
plt.plot(x,y, color='black', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("New Zeeland")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([2400,2300,3800,9300,41000,62900,42600,47000,16400,8200,5100])

plt.subplot(3,3,4)
plt.plot(x,y, color='green', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("Italy")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([6300,8000,10300,16500,19500,10400,10400,15200,8200,5500,4000])

plt.subplot(3,3,5)
plt.plot(x,y, color='blue', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("United Kingdom")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([1100,441,523,1300,3900,16300,43100,27500,8000,4200,3200])

plt.subplot(3,3,6)
plt.plot(x,y, color='indigo', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("Poland")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([0,0,0,0,0,0,0,5700,3700,2700,3100])

plt.subplot(3,3,7)
plt.plot(x,y, color='purple', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("France")

x = np.array(["7 April 2024", "5 May 2024", "2 Jun 2024", "30 Jun 2024", "28 Jul 2024", "25 Aug 2024","22 Sep 2024", "20 Oct 2024", "17 Nov 2024", "15 Dec 2024", "12 Jan 2025"])
y = np.array([403,245,274,587,1200,3800,13100,29600,10300,5600,2800])

plt.subplot(3,3,8)
plt.plot(x,y, color='hotpink', marker='o')
plt.xticks(np.arange(len(x)), x, rotation=90)
plt.grid(color='grey', linestyle='--',linewidth='0.5')
plt.title("Czechia")

plt.suptitle("COVID-19 cases, country level trends", color='blue', size=20)
plt.show()

