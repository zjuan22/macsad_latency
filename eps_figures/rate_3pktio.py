#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 20, 4

cores =     ["","128","","256","","512","","1024","","1280","","1518","","","128","","256","","512","","1024","","1280","","1518","","","128","","256","","512","","1024","","1280","","1518",""]

l2 =      [np.nan , np.nan ,0.832, np.nan, 0.902,np.nan,1.632,np.nan,3.220,np.nan,3.765,np.nan,4.230, np.nan,np.nan,1.453,np.nan,2.836,np.nan,5.244,np.nan,8.767,np.nan,9.846,np.nan,9.865, np.nan,np.nan,6.900,np.nan,9.575,np.nan,9.802,np.nan,9.809,np.nan,9.846,np.nan,9.857]
l3 =      [np.nan , np.nan ,0.797, np.nan, 0.818,np.nan,1.690,np.nan,3.290,np.nan,3.820,np.nan,4.126, np.nan,np.nan,1.453,np.nan,2.835,np.nan,5.231,np.nan,8.756,np.nan,9.846,np.nan,9.860, np.nan,np.nan,5.530,np.nan,9.624,np.nan,9.808,np.nan,9.808,np.nan,9.846,np.nan,9.857]

nat_ul=   [np.nan , 0.523, np.nan,0.712,np.nan,1.428,np.nan,2.534,np.nan,3.345,np.nan,3.780, np.nan,np.nan,1.215,np.nan,2.495,np.nan,4.938,np.nan,8.740,np.nan,9.843,np.nan,9.861, np.nan,np.nan,4.000,np.nan,9.240,np.nan,9.620,np.nan,9.809,np.nan,9.846,np.nan,9.857,np.nan]
nat_dl=   [np.nan , 0.512, np.nan, 0.799,np.nan,1.425,np.nan,2.556,np.nan,3.180,np.nan,3.670, np.nan,np.nan,1.230,np.nan,2.450,np.nan,4.938,np.nan,8.738,np.nan,9.846,np.nan,9.860, np.nan,np.nan,4.273,np.nan,9.273,np.nan,9.801,np.nan,9.841,np.nan,9.871,np.nan,9.875,np.nan]

l2_g= [] 
l3_g= [] 
natu_g= [] 
natd_g= [] 
#netmap_p = netmap
#socket_p = socket

numb = [0,128,256,512,1024,1280,1528,0,0,128,256,512,1024,1280,1528,0,0,128,256,512,1024,1280,1528]

#for i in range(0,len(cores)):
#	if l1[i] != np.nan or l2[i] != np.NaN:
#                print l2[i] 
#		l2_g.append(int(l2[i]/1000))
#		l3_g.append(int(l3[i]/1000))
#		#l3_g[i]=l3[i]/1000 
#	else: 
#		np.nan
#
#for i in range(0,len(cores)):
#	if nat_ul[i] != np.nan: 
#		natu_g.append(nat_ul[i]/1000)
#		natd_g.append(nat_dl[i]/1000) 
#	else:
#		np.nan

 
ind = np.arange(len(cores))

width = 0.4
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar([p + width for p in ind+0.05], l2, width, color= "#FFC72D", edgecolor="black",hatch="..", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.37], l3, width, color="#B78ADF", edgecolor="black",hatch="o", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.2], nat_dl, width, color= "#E65D22", edgecolor="black",hatch="", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.2], nat_ul, width, color= "#06566E", edgecolor="black",hatch="//", lw=0.5, zorder = 0)

#ax.bar([p + width for p in ind+0], l2_g, width, color= "#FFC72D", edgecolor="black",hatch="OO", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind-0.3], l3_g, width, color="#B78ADF", edgecolor="black",hatch="..", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind], natd_g, width, color= "#E65D22", edgecolor="black",hatch="", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind+0.3], natu_g, width, color= "#06566E", edgecolor="black",hatch="//", lw=0.5, zorder = 0)

ax.set_xticks(ind+6*(width/2))
xticks = ax.xaxis.get_major_ticks()

xticks[0].set_visible(False)
xticks[2].set_visible(False)
xticks[4].set_visible(False)
xticks[6].set_visible(False)
xticks[8].set_visible(False)
xticks[10].set_visible(False)
xticks[12].set_visible(False)
xticks[13].set_visible(False)
xticks[15].set_visible(False)
xticks[17].set_visible(False)
xticks[19].set_visible(False)
xticks[21].set_visible(False)
xticks[23].set_visible(False)
xticks[25].set_visible(False)
xticks[26].set_visible(False)
xticks[28].set_visible(False)
xticks[30].set_visible(False)
xticks[32].set_visible(False)
xticks[34].set_visible(False)
xticks[36].set_visible(False)
xticks[38].set_visible(False)

font_size= 16

ax.set_xticklabels(cores, fontsize=font_size)

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

ax.text(5, -1.6, u'Socket-mmap',fontsize=font_size)
ax.text(20, -1.6, u'Netmap',fontsize=font_size)
ax.text(33, -1.6, u'DPDK',fontsize=font_size)
#ax.set_ylim([0,7.4])

leg = plt.legend(['L2', 'L3', 'NAT_DL','NAT_UL'], loc='upper left')

leg.get_frame().set_linewidth(0.0)


plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_pkt"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")
