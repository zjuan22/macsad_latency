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


markers = ["*","o","^",".",">"]

x_values= ["128","256","512","1024","1280","1518"]

l2_1_netmap=  [8.5586,8.8094,9.0052,9.9238,10.5094,10.8576]
l2_32_netmap= [13.0864,13.2946,13.7014,14.3362,14.8114,15.4322]
l2_128_netmap=[13.5354,13.5466,13.7292,14.337,14.7586,15.3154]
l2_256_netmap=[13.0148,13.5952,13.7086,14.4354,14.7808,15.5314]

l2_16_dpdk=   [5.3586,5.5536,6.1406,6.6972,6.9564,7.5056]
l2_32_dpdk=   [5.3232,5.6058,5.9798,6.6484,6.9806,7.6048]


ind = np.arange(len(x_values))

width = 0.3
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim([0, 16])


dashList = [(4,2,20,2),(2,2),(5,1),(4,3,2,2),(8,4,3,1)] 
verde_oscuro="#006633"
azul_cielo="#2248E1"

fucsia="#DA22E1"
cafe="#A91524"

azul_mar="#161673"
azul_claro="#1AE2E2"

tomate="#E88411"
verde_fosfo="#B2E835"

ax.yaxis.grid(color='gray' )

ax.plot(ind, l2_1_netmap,  marker=markers[4],  color="green",  dashes=dashList[4],markerfacecolor="green",markeredgecolor="green", lw=2, markersize=9 )
ax.plot(ind, l2_32_netmap,  marker=markers[0],  color="green",  dashes=dashList[0],markerfacecolor="green",markeredgecolor="green", lw=2, markersize=9 )
ax.plot(ind, l2_128_netmap, color="green",  dashes=dashList[1], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
ax.plot(ind, l2_256_netmap, color="green",  dashes=dashList[2], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )

ax.plot(ind, l2_16_dpdk,  color="blue",   dashes=dashList[3], lw=2, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[3] )
ax.plot(ind, l2_32_dpdk,  color="blue",   dashes=dashList[0], lw=2 ,markerfacecolor="blue",markeredgecolor="blue",  marker=markers[0], markersize=9 )

#ax.set_xticks(ind+6*(width/2))
#xticks = ax.xaxis.get_major_ticks()
font_size= 14
ax.set_xticklabels(x_values, fontsize=10)
ax.set_ylabel('Average latency ($\mu$s)',fontsize=10)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=10)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')


leg= plt.legend(['1 Pkt Burst-Netmap','32 Pkt Burst-Netmap','128 Pkt Burst-Netmap','256 Pkt Burst-Netmap','16 Pkt Burst-DPDK','32 Pkt Burst-DPDK'], bbox_to_anchor=(0., 0.05, 1., .202), loc=3, ncol=3, mode="expand", borderaxespad=0.,  fontsize= 9)

leg.get_frame().set_linewidth(0.0)

plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="lat_diff_burst"
plt.savefig(filename+".eps")
plt.savefig(filename+".png")
plt.savefig(filename+".svg")
