import threading
import time
import re
import subprocess
import os
import argparse
import sys

lst_psize_bng= [ 128, 256, 512, 1024] 
#lst_psize_bng= [1518] 
#lst_psize_bng= [98] 
lst_psize_bng_dl= [ 128, 256, 512, 1024] 
#lst_psize_bng_dl= [1280] 
#lst_psize_bng_dl= [128, 256, 512, 1024] 
#lst_psize_bng_dl= [74] 
lst_psize= [64, 128, 256, 512, 1024, 1280, 1518] 
#lst_psize= [ 1518] 
#lst_psize= [1518]
n_lat_test=2

#mac_directory= '/root/Juan/mac_16'  

osnt="python osnt-tool-cmd.py -ifp0 "
#traces_l2= "../traces/ipv4_1_entries/ipv4_1_random."
#traces_l2= "../traces/ipv4_l2_100_pcap/ipv4_100_random."
#traces_l2= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/l2_l3_1k_pcap/nfpa.trPR_ipv4_1000_random."
traces_l2= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/l2_l3_10k_pcap/nfpa.trPR_ipv4_10000_random."
#traces_l2= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/l2_l3_100k_pcap/nfpa.trPR_ipv4_100000_random."

 
#traces_nat_dl= "/home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_dl/nfpa.trPR_nat_dl_1_random."


#traces_nat_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_dl_1entry/nfpa.trPR_nat_dl_1_random."
#traces_nat_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_dl_100_entries/nfpa.trPR_nat_dl_100_random."
#traces_nat_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_dl_1k/nfpa.trPR_nat_dl_1000_random."
traces_nat_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_dl_10k/nfpa.trPR_nat_dl_10000_random."
#traces_nat_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_dl_100k/nfpa.trPR_nat_dl_100000_random."


#traces_nat_dl= "/home/sunnet/Desktop/OSNT_nietFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_pcap/nfpa.trPR_nat_dl_100_random." 
#traces_nat_ul= "/home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_ul/nfpa.trPR_tcp_1_random." 
#traces_nat_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_pcap/nfpa.trPR_tcp_100_random."
traces_nat_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_ul_10k/nfpa.trPR_tcp_10000_random."
#traces_nat_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/nat_ul_1k/nfpa.trPR_tcp_1000_random."


#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_225545/nfpa.trPR_bng_ul_100_225545."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_20130/nfpa.trPR_bng_ul_1000_20130."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_211757/nfpa.trPR_bng_ul_10000_211757."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_up_ts_1_16317/nfpa.trPR_bng_ul_1_16317."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_up_ts_100_163110/nfpa.trPR_bng_ul_100_163110."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_up_ts_1000_163120/nfpa.trPR_bng_ul_1000_163120."
#traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_up_ts_10000_164144/nfpa.trPR_bng_ul_10000_164144."
traces_bng_ul= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_up_ts_100000_17303/nfpa.trPR_bng_ul_100000_17303."


#traces_bng_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_dl_ts_1_17185/nfpa.trPR_bng_dl_1_17185."
#traces_bng_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_dl_ts_100_171754/nfpa.trPR_bng_dl_100_171754."
#traces_bng_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_dl_ts_1000_171558/nfpa.trPR_bng_dl_1000_171558."
#traces_bng_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_dl_ts_10000_17172/nfpa.trPR_bng_dl_10000_17172."
traces_bng_dl= "/home/sunnet/Desktop/OSNT_netFPGA/OSNT-SUME-live/contrib/challenge2017/PCAP/pcap_bng_dl_ts_100000_171729/nfpa.trPR_bng_dl_100000_171729."

#values=" -flt ../filter.cfg -rpn0 100 -lpn 100 -lty3 -rnm -ipg0 1000000 "
values=" -flt ../filter.cfg -rpn0 1 -lpn 100 -lty3 -rnm -ipg0 1000000 "
#values=" -flt ../filter.cfg -rpn0 1 -lpn 100 -lty3 -rnm -ipg0 1000000 "



def exec_func(traces, size, args, num):

   if (size == 64):
     cmd= osnt + traces + str(size) + "bytes.cap "+values+"-txs0 4 -rxs3 5"+ " -llog " + args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)

   if (size == 128):
     cmd= osnt + traces + str(size) + "bytes.cap "+values+"-txs0 7 -rxs3 8"+ " -llog " + args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)

   elif (size == 256):
     cmd= osnt + traces + str(size) + "bytes.cap "+values+"-txs0 9 -rxs3 10"+ " -llog " +  args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 512):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 9 -rxs3 10"+ " -llog " + args.pktio_env+"_"+ str(psize) +"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1024):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 12 -rxs3 13"+ " -llog " + args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1280):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 11 -rxs3 12"+ " -llog "+  args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   elif (size == 1518):
     cmd=osnt + traces + str(size) + "bytes.cap "+values+"-txs0 12 -rxs3 13"+ " -llog "+ args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)
   
   else: 
     print "put other value like: 128, 256, 512, 1024, 1280, 1518"

def exe_bng(traces, size, args, num):
    if (size == 74 or size==98 or size==128  or size==256 or  size==512 or size==1024 or  size==1218 or size==1280 or  size==1518 ):
     cmd=osnt + traces + str(size) + "bytes.pcap "+values+"-txs0 2 -rxs3 3"+ " -llog "+ args.pktio_env+"_"+ str(psize)+"_num_"+str(num)
     print "command= "+ cmd 
     os.system(cmd)





#python osnt-tool-cmd.py -ifp0 ../traces/ipv4_1_entries/ipv4_1_random.256bytes.cap -flt ../filter.cfg -rpn0 300 -lpn 300 -lty3 -rnm -ipg0 10000 -ipg3 10000 -txs0 7 -rxs3 8   

#Main funcion
if __name__ == '__main__':


    parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
    parser.add_argument("-s", "--psize", action= "store", dest="psize",
                      default = "128", required = False,
                      help="Output file test name ")

    parser.add_argument("-e", "--env", action="store", dest="pktio_env",
                      default= '0', required = False,
                      help="Choose the pktio enviroment/s to compile with MACSAD core i.e 0=l2, 1=l3, 2=nat_ul, 3=nat_dl, 4=bng_ul 5=bng_dl")


    parser.add_argument("-t", "--test", action="store", dest="set_test",
                      default= '0', required = False,
                      help="Set of latency test with all packet sizes. On default is off. To activate it set t=1. i.e: -t 1 ")
    parser.add_argument("-r", "--rate", action="store", dest="rate",
                      default= '0', required = False,
                      help="Choose the rate to do a throughput test")
    arguments = parser.parse_args() 

#pr int "leee " + str(len(dic[arguments.pktio_env]))


      



    if (arguments.pktio_env == '0') or (arguments.pktio_env == '1'): 
      print "l2" 
    
    
      if (arguments.set_test == "1"): 
         for i in range(n_lat_test): 
            for psize in lst_psize:                                                      
                print "set of latency tests for diferents packet sizes"                           
                print "test  "+ str(lst_psize)     
                #cmd= osnt + traces_l2 + arguments.psize + "bytes.cap "+values+"-txs0 7 -rxs3 8 " + " -llog "+ arguments.psize+"_"+ str(psize)+"_num_"+str(i)   
                #print "command= "+ cmd 
                #os.system(cmd)
    
            
                #os.chdir(nfpa_directory)                                                
                if (psize == 64):
		  cmd= osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 4 -rxs3 5" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)  
                  print "command= "+ cmd 
                  os.system(cmd)
    
                elif (psize == 128):
                  cmd= osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)  
                  print "command= "+ cmd 
                  os.system(cmd)
    
                elif (psize == 256):
                  cmd= osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 512):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 7 -rxs3 8" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1024):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 9 -rxs3 10" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1280):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 10 -rxs3 11" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                elif (psize == 1518):
                  cmd=osnt + traces_l2 + str(psize) + "bytes.cap "+values+"-txs0 10 -rxs3 11" + " -llog "+ arguments.pktio_env+"_"+ str(psize)+"_num_"+str(i)
                  print "command= "+ cmd 
                  os.system(cmd)
                
                else: 
                  print "put other value like: 128, 256, 512, 1024, 1280, 1518"
                   
                                                                                        
                time.sleep(1)    
    
           
      elif (arguments.rate == "1"):
       
         cmd= "python osnt-tool-cmd.py -ifp0 ../traces/ipv4_l2_100_pcap/ipv4_100_random."+arguments.psize + "bytes.cap -rpn0 10000000000 -run -st -ds"
         print "command= "+ cmd 
         os.system(cmd)
    
    elif (arguments.pktio_env == '2'): 
      print "nat_ul"
      if (arguments.set_test == "1"): 
         for i in range(n_lat_test): 
            for psize in lst_psize:                                                      
              exec_func(traces_nat_ul, psize, arguments, i)
         #md= "cat -n tcpdump_"+arguments.pktio_env+"1280_num_4 | grep -n ^ | grep ^302  
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 /home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_ul/nfpa.trPR_tcp_1_random."+ arguments.psize+ "bytes.cap -rpn0 100000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)
      else:
         exec_func(traces_nat_ul, int(arguments.psize), arguments)
    
    elif (arguments.pktio_env == '3'): 
      print "nat_dl"
      if (arguments.set_test == "1"):  
         for i in range(n_lat_test): 
            for psize in lst_psize:                                                      
              exec_func(traces_nat_dl, psize, arguments, i)


           
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 /home/sunnet/topicos_sistemas/nat_mac/PCAP/1entry_nat_dl/nfpa.trPR_nat_dl_1_random."+ arguments.psize+ "bytes.cap -rpn0 100000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)

    elif (arguments.pktio_env == '4'): 
      print "bng_ul"
      if (arguments.set_test == "1"):  
         for i in range(n_lat_test): 
            for psize in lst_psize_bng:                                                      
              exe_bng(traces_bng_ul, psize, arguments, i)


           
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 "+traces_bng_ul+ arguments.psize+ "bytes.pcap -rpn0 1000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)

         print "not implemented for bng yet "+ cmd 
      else:
         exec_func(traces_nat_ul, int(arguments.psize))

      #exec_func(arguments,traces_nat_dl)
     
    elif (arguments.pktio_env == '5'): 
      print "bng_dl"
      if (arguments.set_test == "1"):  
         for i in range(n_lat_test): 
            for psize in lst_psize_bng_dl:                                                      
              exe_bng(traces_bng_dl, psize, arguments, i)


           
      elif (arguments.rate == "1"):
         cmd= "python osnt-tool-cmd.py -ifp0 "+traces_bng_dl+ arguments.psize+ "bytes.pcap -rpn0 1000000 -run -st -ds "
         print "command= "+ cmd 
         os.system(cmd)

         #print "not implemented for bng yet "+ cmd 
      else:
         exec_func(traces_nat_ul, int(arguments.psize))

      #exec_func(arguments,traces_nat_dl)
    print "ENDING PROGRAM"







