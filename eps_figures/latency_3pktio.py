import pandas as pd
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


l2_d=[5.382,5.543,5.7214,6.623,7.361,7.9896]
l2_n=[13.0864,13.2946,13.7014,14.3362,14.8114,15.4322]
l2_s=[15.9068,16.2808,16.9266,18.1144,18.6336,19.2088]

l3_d=[5.391,5.589,5.7614,6.6298,7.4148,7.9928]
l3_n=[13.2428,13.5816,13.8094,14.6842,15.2932,15.697]
l3_s=[15.9992,16.4414,17.0152,18.1378,19.0462,19.4106]

nu_d=[5.421,5.659,5.8154,6.8916,7.5602,8.1968]
nu_n=[13.8536,14.2572,15.1908,16.126,16.447,16.9336]
nu_s=[17.6358,17.9254,18.6382,19.2902,19.9438,20.3038]

nd_d=[5.498,5.716,5.871,7.0592,7.6132,8.3106]
nd_n=[13.765,14.309,15.125,16.2548,16.5664,16.9958]
nd_s=[17.6334,18.1244,18.803,19.6898,20.2692,20.4264]


nat_dl = [np.nan , np.nan ,nd_d[0], np.nan,nd_d[1] ,np.nan,nd_d[2] ,np.nan,nd_d[3] ,np.nan,nd_d[4],np.nan,nd_d[5], np.nan,np.nan,nd_n[0],np.nan,nd_n[1],np.nan,nd_n[2],np.nan,nd_n[3],np.nan,nd_n[4],np.nan,nd_n[5], np.nan,np.nan,nd_s[0],np.nan,nd_s[1],np.nan,nd_s[2],np.nan,nd_s[3],np.nan,nd_s[4],np.nan,nd_s[5]]

nat_ul = [np.nan , np.nan ,nu_d[0], np.nan,nu_d[1] ,np.nan,nu_d[2] ,np.nan,nu_d[3] ,np.nan,nu_d[4],np.nan,nu_d[5], np.nan,np.nan,nu_n[0],np.nan,nu_n[1],np.nan,nu_n[2],np.nan,nu_n[3],np.nan,nu_n[4],np.nan,nu_n[5], np.nan,np.nan,nu_s[0],np.nan,nu_s[1],np.nan,nu_s[2],np.nan,nu_s[3],np.nan,nu_s[4],np.nan,nu_s[5]]


l3=   [np.nan ,l3_d[0] , np.nan,l3_d[1],np.nan,l3_d[2],np.nan,l3_d[3],np.nan,l3_d[4],np.nan,l3_d[5], np.nan,np.nan,l3_n[0],np.nan,l3_n[1],np.nan,l3_n[2],np.nan,l3_n[3],np.nan,l3_n[4],np.nan,l3_n[5], np.nan,np.nan,l3_s[0],np.nan,l3_s[1],np.nan,l3_s[2],np.nan,l3_s[3],np.nan,l3_s[4],np.nan,l3_s[5],np.nan]

l2=   [np.nan ,l2_d[0] , np.nan,l2_d[1],np.nan,l2_d[2],np.nan,l2_d[3],np.nan,l2_d[4],np.nan,l2_d[5], np.nan,np.nan,l2_n[0],np.nan,l2_n[1],np.nan,l2_n[2],np.nan,l2_n[3],np.nan,l2_n[4],np.nan,l2_n[5], np.nan,np.nan,l2_s[0],np.nan,l2_s[1],np.nan,l2_s[2],np.nan,l2_s[3],np.nan,l2_s[4],np.nan,l2_s[5],np.nan]


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

verde="#B2E835"
tomate="#E88411"
azul="#1C179F"
cafe="#7E1410"

width = 0.4
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar([p + width for p in ind+0.05],	 nat_dl, width, color= verde, edgecolor="black",hatch="", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.37], nat_ul, width, color= azul, edgecolor="black",hatch="//", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.2], l3, width, color=tomate, edgecolor="black",hatch="..", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.2], l2, width, color= cafe, edgecolor="black",hatch="OO", lw=0.5, zorder = 0)

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


font_size=16
ax.set_xticklabels(cores, fontsize=font_size)

ax.set_ylabel('Average latency ($\mu$s)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=21)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')


pos_y= -3.2
ax.text(31, pos_y, u'Socket-mmap',fontsize=font_size)
ax.text(19, pos_y, u'Netmap',fontsize=font_size)
ax.text(5.4,pos_y, u'DPDK',fontsize=font_size)
ax.set_ylim([0,21])

leg = plt.legend(['NAT_UL','NAT_DL','L3', 'L2'], loc='upper left', fontsize=font_size)
leg.get_frame().set_linewidth(0.0)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="lat_pkt"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")
