import numpy as np
from matplotlib import pyplot as plt

#reads only DNA bases
with open(input("Insert Genome File:")) as s:
    pg=s.read()
    S=''.join(pg.strip())
    genome=""
    for i in S:
        if i=="A" or i=="T" or i=="G" or i=="C":
            genome+=i
        else:
            continue

def gc(genome):
    a=genome.count("A")
    t=genome.count("T")
    g=genome.count("G")
    c=genome.count("C")
    gc=((g+c)*100)/(a+t+g+c)
    return gc

def at(genome):
    a=genome.count("A")
    t=genome.count("T")
    g=genome.count("G")
    c=genome.count("C")
    at=(a-t)/(a+t)
    return at


win_size=int(input("Window Size: "))
SD=float(input("Certainty in SDs: "))
epoch_val=[]
x=0
for i in range((len(genome)//win_size)):
    ep_gc=gc(genome[x:x+win_size])
    epoch_val.append(ep_gc)
    x+=win_size


at_val=[]
y=0
for i in range(len(genome)//win_size):
    ep_at=at(genome[y:y+win_size])
    at_val.append(ep_at)
    y+=win_size


std_dev = np.std(epoch_val)
av=np.mean(epoch_val)
at_mean=np.mean(at_val)

positions=[]
for i in range(len(epoch_val)):
    if (epoch_val[i])>(av+std_dev*SD) or epoch_val[i]<av-std_dev*SD:
        positions.append(i)
    else:
        continue

#plots

plt.figure(1)
plt.plot(range(len(epoch_val)),epoch_val)
plt.axhline(av,color="black", linestyle="--")
plt.axhline(av+std_dev*SD,linestyle="--")
plt.axhline(av-std_dev*SD,linestyle="--")
plt.xlabel("genome position")
plt.ylabel("GC %")
plt.title("GC Analysis")
plt.show()

plt.figure(2)
plt.plot(range(len(at_val)),at_val)
plt.axhline(at_mean,color="black")
plt.xlabel("genome position")
plt.ylabel("Weighted AT")
plt.title("weighted AT Analysis")
plt.show()

print(positions)
print("Total GC amount: "+ str(round(gc(genome),3)) + " %")
nuc_printing=input("Press Y for sequences or any other letter for exit: ")
if nuc_printing=="Y":
    with open(input("Name your file: "),"a+") as a:
        for i in range(len(positions)):
            fasta=a.write(genome[positions[i]:(positions[i] + win_size)]+"\n\n\n\n")


print("DONE")











