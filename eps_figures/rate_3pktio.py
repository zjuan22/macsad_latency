#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True


cores =     ["","128","","256","","512","","1024","","1280","","1518","","","128","","256","","512","","1024","","1280","","1518","","","128","","256","","512","","1024","","1280","","1518",""]

l2 =      [np.nan , np.nan ,832, np.nan, 902,np.nan,1632,np.nan,3220,np.nan,3765,np.nan,4230, np.nan,np.nan,1453,np.nan,2836,np.nan,5244,np.nan,8767,np.nan,9846,np.nan,9865, np.nan,np.nan,6900,np.nan,9575,np.nan,9802,np.nan,9809,np.nan,9846,np.nan,9857]
l3 =      [np.nan , np.nan ,797, np.nan, 818,np.nan,1690,np.nan,3290,np.nan,3820,np.nan,4126, np.nan,np.nan,1453,np.nan,2835,np.nan,5231,np.nan,8756,np.nan,9846,np.nan,9860, np.nan,np.nan,5530,np.nan,9624,np.nan,9808,np.nan,9808,np.nan,9846,np.nan,9857]

nat_ul=   [np.nan , 523, np.nan, 712,np.nan,1428,np.nan,2534,np.nan,3345,np.nan,3780, np.nan,np.nan,1215,np.nan,2495,np.nan,4938,np.nan,8740,np.nan,9843,np.nan,9861, np.nan,np.nan,4000,np.nan,9240,np.nan,9620,np.nan,9809,np.nan,9846,np.nan,9857,np.nan]
nat_dl=   [np.nan , 512, np.nan, 799,np.nan,1425,np.nan,2556,np.nan,3180,np.nan,3670, np.nan,np.nan,1230,np.nan,2450,np.nan,4938,np.nan,8738,np.nan,9846,np.nan,9860, np.nan,np.nan,4273,np.nan,9273,np.nan,9801,np.nan,9841,np.nan,9871,np.nan,9875,np.nan]

#dpdk_p = dpdk
#netmap_p = netmap
#socket_p = socket

numb = [0,128,256,512,1024,1280,1528,0,0,128,256,512,1024,1280,1528,0,0,128,256,512,1024,1280,1528]

#for i in range(0,len(cores)):
#	if dpdk[i] != np.nan: 
#		dpdk_p[i]=(dpdk[i]*1000)/((20+numb[i])*8) 
#		netmap_p[i]=(netmap[i]*1000)/((20+numb[i])*8) 
#		socket_p[i]=(socket[i]*1000)/((20+numb[i])*8) 
#	else: 
#		np.nan

ind = np.arange(len(cores))
width = 0.3
#fig = plt.figure(figsize=(7,5.3))
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.bar([p + width for p in ind], dpdk_p, width, color="#AFD2E9", edgecolor="black")
#ax.bar([p + width for p in ind+0.3], dpdk_p, width, edgecolor="black",hatch="OO", lw=1., zorder = 0)
ax.bar([p + width for p in ind+0], l2, width, color= "yellow", edgecolor="black",hatch="OO", lw=1., zorder = 0)
ax.bar([p + width for p in ind-0.3], l3, width, color= "purple", edgecolor="black",hatch="OO", lw=1., zorder = 0)
ax.bar([p + width for p in ind], nat_ul, width, color= "blue", edgecolor="black",hatch="OO", lw=1., zorder = 0)
ax.bar([p + width for p in ind+0.3], nat_dl, width, color= "red", edgecolor="black",hatch="OO", lw=1., zorder = 0)

#ax.bar([p + width for p in ind], netmap_p, width, edgecolor="black", lw=1., zorder = 0)

#ax.bar([p + width for p in ind-0.3], socket_p, width, edgecolor="black",hatch="..", lw=1., zorder = 0)

ax.set_xticks(ind+2*(width/2))
xticks = ax.xaxis.get_major_ticks()

xticks[3].set_visible(False)
xticks[7].set_visible(False)
xticks[11].set_visible(False)
xticks[12].set_visible(False)
xticks[16].set_visible(False)
xticks[20].set_visible(False)
ax.set_xticklabels(cores)

ax.set_ylabel('Throughput (Mpps)',fontsize=9)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=9)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

#ax.text(1, -0.7, u'64',fontsize=10)
#ax.text(4.8, -0.7, u'128',fontsize=10)
#ax.text(8.8, -0.7, u'256',fontsize=10)
#ax.text(14, -0.7, u'64',fontsize=10)
#ax.text(17.8, -0.7, u'128',fontsize=10)
#ax.text(21.8, -0.7, u'256',fontsize=10)
#ax.text(9.45, -1.4, u'Number of cores',fontsize=10)
#ax.text(4, -1, u'Uplink (UL)',fontsize=10)
#ax.text(16.4, -1, u'Downlink (DL)',fontsize=10)
#ax.set_ylim([0,7.4])

plt.legend(['L2', 'L3', 'NAT_UL','NAT_DL'], loc='upper right',frameon=False)


plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)
#plt.savefig("vxlan.png")
plt.savefig("vxlan.eps")
