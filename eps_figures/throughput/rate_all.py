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

cores =     ["","64","","128","","256","","512","","","64","","128","","256","","512","","","64","","128","","256","","512","","","64","","128","","256","","512","","","64","","128","","256","","512","","","64","","128","","256","","512",""]


l2_100k=[2.65,5.27,9.27,9.62,9.80,9.80,9.80]
l3_100k=[2.70,5.14,9.27,9.62,9.80,9.80,9.80]

l2_10k=[2.67,5.32,9.28,9.62,9.80,9.80,9.80]
l3_10k=[2.70,5.15,9.62,9.80,9.80,9.80,9.80]

l2_100=[2.74,5.90,9.50,9.80,9.80,9.80,9.80]
l3_100=[2.71,5.53,9.62,9.80,9.80,9.80,9.80]

l2_1k=[2.64,5.30,9.62,9.80,9.80,9.80,9.80]
l3_1k=[2.67,5.38,9.62,9.80,9.80,9.80,9.80]

nat_ul_100k=[1.57,3.16,6.29,9.62,9.81,9.88,9.88]
nat_dl_100k=[1.72,3.24,6.35,9.74,9.80,9.80,9.80]

nat_ul_10k=[1.63,3.32,6.40,9.62,9.81,9.81,9.81]
nat_dl_10k=[1.79,3.56,6.67,9.72,9.80,9.80,9.80]

nat_ul_100=[2.10,3.62,6.56,9.62,9.81,9.85,9.86]
nat_dl_100=[2.07,3.68,6.63,9.60,9.80,9.80,9.80]

nat_ul_1k=[1.94,3.51,6.35,9.64,9.81,9.81,9.81]
nat_dl_1k=[1.98,3.69,6.56,9.68,9.80,9.80,9.80]

bng_ul_100k=[1.10,2.14,4.61,9.18,9.58,9.80,9.80]
bng_dl_100k=[2.0,3.33,6.12,9.64,9.81,9.84,9.88]

bng_ul_10k=[1.23,2.13,4.72,9.20,9.58,9.80,9.80]
bng_dl_10k=[2.00,3.40,6.22,9.64,9.81,9.85,9.88]

bng_ul_100=[1.56,2.55,5.15,9.21,9.58,9.80,9.80]
bng_dl_100=[2.00,3.71,6.56,9.65,9.81,9.85,9.88]

bng_ul_1k=[1.32,2.31,4.90,9.21,9.58,9.80,9.80]
bng_dl_1k=[1.98,3.46,6.31,9.65,9.81,9.85,9.88]





e_1k = [np.nan , np.nan ,l2_1k[0], np.nan, l2_1k[1] ,np.nan, l2_1k[2] ,np.nan, l2_1k[3] ,np.nan,np.nan,l3_1k[0],np.nan,l3_1k[1],np.nan,l3_1k[2],np.nan,l3_1k[3],np.nan , np.nan ,nat_ul_1k[0], np.nan, nat_ul_1k[1] ,np.nan, nat_ul_1k[2] ,np.nan, nat_ul_1k[3] , np.nan,np.nan,nat_dl_1k[0],np.nan,nat_dl_1k[1],np.nan,nat_dl_1k[2],np.nan,nat_dl_1k[3],np.nan,np.nan ,bng_ul_1k[0], np.nan, bng_ul_1k[1] ,np.nan, bng_ul_1k[2] ,np.nan, bng_ul_1k[3], np.nan,np.nan,bng_dl_1k[0],np.nan,bng_dl_1k[1],np.nan,bng_dl_1k[2],np.nan,bng_dl_1k[3]]

e_100 = [np.nan , np.nan ,l2_100[0], np.nan,l2_100[1] ,np.nan,l2_100[2] ,np.nan,l2_100[3], np.nan,np.nan,l3_100[0],np.nan,l3_100[1],np.nan,l3_100[2],np.nan,l3_100[3], np.nan , np.nan ,nat_ul_100[0], np.nan,nat_ul_100[1] ,np.nan,nat_ul_100[2] ,np.nan,nat_ul_100[3],  np.nan,np.nan,nat_dl_100[0],np.nan,nat_dl_100[1],np.nan,nat_dl_100[2],np.nan,nat_dl_100[3],np.nan , np.nan ,bng_ul_100[0], np.nan,bng_ul_100[1] ,np.nan,bng_ul_100[2] ,np.nan,bng_ul_100[3], np.nan,np.nan,bng_dl_100[0],np.nan,bng_dl_100[1],np.nan,bng_dl_100[2],np.nan,bng_dl_100[3]]
#
e_10k = [np.nan ,l2_10k[0] , np.nan,l2_10k[1],np.nan,l2_10k[2],np.nan,l2_10k[3], np.nan,np.nan,l3_10k[0],np.nan,l3_10k[1],np.nan,l3_10k[2],np.nan,l3_10k[3],np.nan,np.nan ,nat_ul_10k[0] , np.nan,nat_ul_10k[1],np.nan,nat_ul_10k[2],np.nan,nat_ul_10k[3], np.nan,np.nan,nat_dl_10k[0],np.nan,nat_dl_10k[1],np.nan,nat_dl_10k[2],np.nan,nat_dl_10k[3],np.nan,np.nan ,bng_ul_10k[0] , np.nan,bng_ul_10k[1],np.nan,bng_ul_10k[2],np.nan,bng_ul_10k[3], np.nan,np.nan,bng_dl_10k[0],np.nan,bng_dl_10k[1],np.nan,bng_dl_10k[2],np.nan,bng_dl_10k[3],np.nan]
#
e_100k= [np.nan ,l2_100k[0] , np.nan,l2_100k[1],np.nan,l2_100k[2],np.nan,l2_100k[3], np.nan,np.nan,l3_100k[0],np.nan,l3_100k[1],np.nan,l3_100k[2],np.nan,l3_100k[3],np.nan, np.nan ,nat_ul_100k[0] , np.nan,nat_ul_100k[1],np.nan,nat_ul_100k[2],np.nan,nat_ul_100k[3], np.nan,np.nan,nat_dl_100k[0],np.nan,nat_dl_100k[1],np.nan,nat_dl_100k[2],np.nan,nat_dl_100k[3],np.nan, np.nan ,bng_ul_100k[0] , np.nan,bng_ul_100k[1],np.nan,bng_ul_100k[2],np.nan,bng_ul_100k[3], np.nan,np.nan,bng_dl_100k[0],np.nan,bng_dl_100k[1],np.nan,bng_dl_100k[2],np.nan,bng_dl_100k[3],np.nan]

aa =len(e_1k)
bb =len(e_10k)
cc =len(e_100k)
dd =len(e_100)
print(aa )
print(bb )
print(cc )
print(dd )
#print str(len(e_100))
#print str(len(e_10k))
#print str(len(e_100k))
#


l2_g= [] 
l3_g= [] 
natu_g= [] 
natd_g= [] 
#netmap_p = netmap
#socket_p = socket

#numb = [0,98,128,256,512,1024,1280,1528,0,0,98,128,256,512,1024,1280,1528]

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
ax.bar([p + width for p in ind+0.05],e_100 , width, color= verde, edgecolor="black",hatch="", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.37],e_1k , width, color= azul, edgecolor="black",hatch="//", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.2], e_10k, width, color=tomate, edgecolor="black",hatch="..", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.2], e_100k, width, color= cafe, edgecolor="black",hatch="OO", lw=0.5, zorder = 0)

ax.set_xticks(ind+6*(width/2))
xticks = ax.xaxis.get_major_ticks()

xticks[0].set_visible(False)
xticks[2].set_visible(False)
xticks[4].set_visible(False)
xticks[6].set_visible(False)
#xticks[8].set_visible(False)
#xticks[9].set_visible(False)
#xticks[10].set_visible(False)
#xticks[11].set_visible(False)
#xticks[12].set_visible(False)
#xticks[13].set_visible(False)
#xticks[14].set_visible(False)
#xticks[15].set_visible(False)
#xticks[16].set_visible(False)
#xticks[17].set_visible(False)
# xticks[19].set_visible(False)
# xticks[21].set_visible(False)
# xticks[23].set_visible(False)
# xticks[25].set_visible(False)
# xticks[27].set_visible(False)
# #xticks[30].set_visible(False)


font_size=16
ax.set_xticklabels(cores, fontsize=font_size)

#ax.set_ylabel('Average latency ($\mu$s)',fontsize=font_size)
ax.set_ylabel('Througput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=21)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')


pos_y= -1.5
ax.text(3.5, pos_y, '     L2 ',fontsize=font_size)
ax.text(13.5, pos_y, '     L3 ',fontsize=font_size)
ax.text(20.5, pos_y, '     NAT_UP ',fontsize=font_size)
ax.text(30, pos_y, '     NAT_DL ',fontsize=font_size)
ax.text(39, pos_y, '     BNG_UL ',fontsize=font_size)
ax.text(48, pos_y, '     BNG_DL ',fontsize=font_size)

#ax.text(23.5, pos_y, u'L3',fontsize=font_size)
#ax.text(5.4,pos_y, u'DPDK',fontsize=font_size)
ax.set_ylim([0,10])

leg = plt.legend(['100','1k','10k', '100k'], loc='upper left', fontsize=font_size)
leg.get_frame().set_linewidth(0.0)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_diff_table_e_all"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
#plt.savefig(filename+".svg")
plt.savefig(filename+".png")
