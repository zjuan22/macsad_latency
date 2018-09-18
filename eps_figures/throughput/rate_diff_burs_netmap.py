#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 6.5, 3.5 


markers = ["*","o","^","."]

x_values= ["128","256","512","1024","1280","1518"]

l2_32_netmap= [1.453,2.836,5.244,8.767,9.846,9.865]
l2_128_netmap=[2.343,4.5,7.94,9.829,9.855,9.865]
l2_256_netmap=[2.732,5.23,8.92,9.82,9.856,9.86]
l2_16_dpdk=   [7.15,9.275,9.624,9.809,9.843,9.852]
l2_32_dpdk=   [6.9,9.269,9.82,9.809,9.846,9.857]


ind = np.arange(len(x_values))

width = 0.3
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_ylim([0, 10])


linestyles = ['-', '--', '-.', ':']
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

ax.plot(ind, l2_32_netmap,  marker=markers[0],  color="green",  dashes=dashList[0],markerfacecolor="green",markeredgecolor="green", lw=2, markersize=9 )
ax.plot(ind, l2_128_netmap, color="green",  dashes=dashList[1], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
ax.plot(ind, l2_256_netmap, color="green",  dashes=dashList[2], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )
ax.plot(ind, l2_16_dpdk,  color="blue",   dashes=dashList[3], lw=2, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[3] )
ax.plot(ind, l2_32_dpdk,  color="blue",   dashes=dashList[0], lw=2 ,markerfacecolor="blue",markeredgecolor="blue",  marker=markers[0], markersize=9 )

#ax.set_xticks(ind+6*(width/2))
#xticks = ax.xaxis.get_major_ticks()
font_size=14
ax.set_xticklabels(x_values, fontsize=font_size)

ax.set_ylabel('Throughput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.font_size)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

leg=plt.legend(['32 Pkt Burst-Netmap','128 Pkt Burst-Netmap','256 Pkt Burst-Netmap','16 Pkt Burst-DPDK','32 Pkt Burst-DPDK'], loc='center right', fontsize= 11)

leg.get_frame().set_linewidth(0.0)

plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_diff_burst"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".png")
plt.savefig(filename+".svg")
