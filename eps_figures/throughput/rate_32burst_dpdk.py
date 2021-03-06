#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 7, 3.5 


markers = ["*","^","."]

x_values= ["128","256","512","1024","1280","1518"]

osnt_l2=[6.9,9.575,9.802,9.809,9.846,9.857]
nfpa_l2=[6.061,10,10,10,10,10]
osnt_l3=[5.53,9.624,9.808,9.808,9.846,9.857]
nfpa_l3=[5.219,9.524,10,10,10,10]
osnt_nu=[4,9.24,9.62,9.809,9.846,9.857]
nfpa_nu=[3.929,7.135,9.817,10,10,10]
osnt_nd=[4.273,9.273,9.801,9.841,9.871,9.875]
nfpa_nd=[3.945,7.086,9.624,10,10,10]
osnt_al=[8.649,9.775,9.82,9.828,9.828,9.868]
nfpa_al=[10,10,10,10,10,10]



#l2 =      [np.nan,]
#l3 =      [
#nat_ul=   [857,np.nan]
#nat_dl=   [875,np.nan]

 
ind = np.arange(len(x_values))

width = 0.3
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_ylim([0, 10])

#ax.bar([p + width for p in ind+0], l2, width, color= "#FFC72D", edgecolor="black",hatch="OO", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind-0.3], l3, width, color="#B78ADF", edgecolor="black",hatch="..", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind], nat_dl, width, color= "#E65D22", edgecolor="black",hatch="", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind+0.3], nat_ul, width, color= "#06566E", edgecolor="black",hatch="//", lw=0.5, zorder = 0)


linestyles = ['-', '--', '-.', ':']
dashList = [(4,2,20,2),(2,3),(5,1),(4,3,2,2),(8,4,3,1)] 
verde_oscuro="#006633"
azul_cielo="#2248E1"

fucsia="#DA22E1"
cafe="#A91524"

azul_mar="#161673"
azul_claro="#1AE2E2"

tomate="#E88411"
verde_fosfo="#B2E835"

ax.yaxis.grid(color='gray' )
ax.plot(ind, osnt_l2,  color=azul_cielo,   linestyle="-.", dashes=dashList[0], lw=2, )
ax.plot(ind, nfpa_l2,  color=verde_oscuro, linestyle="-.", dashes=dashList[0], lw=2)

ax.plot(ind, osnt_l3,  color="red",   dashes=dashList[1], lw=2)
ax.plot(ind, nfpa_l3,  color="green", dashes=dashList[1], lw=2)

ax.plot(ind, osnt_nu,  color=cafe,   dashes=dashList[2], lw=2)
ax.plot(ind, nfpa_nu,  color=fucsia, dashes=dashList[2], lw=2)

ax.plot(ind, osnt_nd,  color=azul_mar,   dashes=dashList[3], lw=2)
ax.plot(ind, nfpa_nd,  color=azul_claro, dashes=dashList[3], lw=2)

ax.plot(ind, osnt_al,  color="black",   dashes=dashList[4], lw=2)
ax.plot(ind, nfpa_al,  color=tomate,    dashes=dashList[4], lw=2)

#ax.set_xticks(ind+6*(width/2))
#xticks = ax.xaxis.get_major_ticks()
font_size = 14
ax.set_xticklabels(x_values, fontsize=font_size)

ax.set_ylabel('Throughput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

#ax.text(5, -1.2, u'Socket-mmap',fontsize=10)
#ax.text(19, -1.2, u'Netmap',fontsize=10)
#ax.text(33, -1.2, u'DPDK',fontsize=10)
#ax.set_ylim([0,7.4])

leg= plt.legend(['OSNT-L2', 'NFPA-L2','OSNT-L3', 'NFPA-L3', 'OSNT-NAT-UL', 'NFPA-NAT_UL', 'OSNT-NAT-DL', 'NFPA-NAT_DL', 'OSNT-Standalone','NFPA-Standalone'], loc='upper right',frameon=False, fontsize= 11)
leg.get_frame().set_linewidth(0.0)

plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_32burst_pkt"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")
