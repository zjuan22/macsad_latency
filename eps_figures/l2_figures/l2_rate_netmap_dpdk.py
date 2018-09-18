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


markers = ["*","o","^",".",">"]

x_values= ["98", "128","256","512","1024","1280","1518"]


#bng_8_dpdk= [1.5, 2.5, 5.02, 9.18, 9.58, 9.86, 9.86]
#bng_16_dpdk= [1.53, 2.51, 5.03, 9.18, 9.58, 9.86, 9.86]
#bng_32_dpdk= [1.56, 2.55, 5.15, 9.18, 9.58, 9.86, 9.86]
#bng_64_dpdk= [1.56, 2.53, 5.15, 9.19, 9.58, 9.86, 9.86]
#

# this data for l2 with 1k entries
bng_8_dpdk=    [ 2.636	,5.268	,9.275	,9.624	,9.857	,9.857	,9.857]
bng_16_dpdk=   [ 2.829	,5.407	,9.275	,9.624	,9.857	,9.857	,9.857]
bng_32_dpdk=   [ 2.64	,5.30	,9.62	,9.80	,9.80	,9.80	,9.86 ]
bng_64_dpdk=   [ 2.728	,5.472	,9.270	,9.624	,9.857	,9.857	,9.857]
bng_128_dpdk=  [ 2.742	,5.479	,9.270	,9.624	,9.857	,9.857	,9.857]
bng_256_dpdk=  [ 2.627	,5.253	,9.270	,9.624	,9.857	,9.857	,9.857]
bng_512_dpdk=  [ 2.635	,5.273	,9.275	,9.624	,9.857	,9.857	,9.857]
bng_1024_dpdk= [ 2.767	,5.471	,9.275	,9.624	,9.857	,9.857	,9.857]



bng_8_netmap =  [0.36	,0.59	,1.125	,2.210	,4.270	,5.106	,5.28  ] 
bng_16_netmap = [0.56	,0.942	,1.851	,3.570	,6.733	,8.064	,7.47  ]
bng_32_netmap = [0.77	,1.400	,2.723	,5.114	,9.204	,9.846	,9.857 ]
bng_64_netmap = [0.937	,1.842	,3.550	,6.499	,9.809	,9.846	,9.857 ]
bng_128_netmap= [1.12	,2.156	,4.108	,7.319	,9.809	,9.846	,9.857 ]
bng_256_netmap= [1.240	,2.356	,4.449	,7.750	,9.809	,9.846	,9.857 ]
bng_512_netmap= [1.170	,2.242	,4.190	,6.748	,9.809	,9.846	,9.857 ]
bng_1024_netmap=[1.170	,2.289	,4.208	,5.998	,9.809	,9.846	,9.857 ]



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

#ax.plot(ind, l2_32_netmap,  marker=markers[0],  color="green",  dashes=dashList[0],markerfacecolor="green",markeredgecolor="green", lw=2, markersize=9 )
#ax.plot(ind, l2_128_netmap, color="green",  dashes=dashList[1], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
#ax.plot(ind, l2_256_netmap, color="green",  dashes=dashList[2], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )

ax.plot(ind, bng_8_dpdk,  color="blue",   dashes=dashList[1], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[1] )
ax.plot(ind, bng_32_dpdk,  color="blue",   dashes=dashList[2], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[2] )
ax.plot(ind, bng_256_dpdk,  color="blue",   dashes=dashList[3], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[3] )
ax.plot(ind, bng_512_dpdk,  color="blue",   dashes=dashList[0], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[0] )
ax.plot(ind, bng_1024_dpdk,  color="blue",   dashes=dashList[4], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[4] )


ax.plot(ind, bng_8_netmap,  color="green",   dashes=dashList[1], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
ax.plot(ind, bng_32_netmap,  color="green",   dashes=dashList[2], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )
ax.plot(ind, bng_256_netmap,  color="green",   dashes=dashList[3], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[3] )
ax.plot(ind, bng_512_netmap,  color="green",   dashes=dashList[0], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[0] )
ax.plot(ind, bng_1024_netmap,  color="green",   dashes=dashList[4], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[4] )


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

#leg=plt.legend(['Batch size 8','Batch size 64','Batch size 256','Batch size 512', 'Batch size 1024'], loc='lower right', fontsize= 9)

leg=plt.legend(['Batch size 8-DPDK ','Batch size 64-DPDK','Batch size 256-DPDK','Batch size 512-DPDK', 'Batch size 1024-DPDK','Batch size 8-Netmap','Batch size 64-Netmap','Batch size 256-Netmap','Batch size 512-Netmap', 'Batch size 1024-Netmap'], fontsize= 9, loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=3)

leg.get_frame().set_linewidth(0.0)

#plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)
plt.tight_layout(pad=3.5, w_pad=1, h_pad=2)

filename="l2_rate_netmap_dpdk"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".png")
#plt.savefig(filename+".svg")
