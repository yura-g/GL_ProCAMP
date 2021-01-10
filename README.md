# GL_ProCamp

For display cpu and mem metrics we can run script metrics.py

-------------------------------------------------------------------------------------------
# CPU

-------------------------------------------------------------------------------------------

python3 metrics.py cpu

system.cpu.idle 498288.53 
system.cpu.user 31070.55 
system.cpu.guest 0.0 
system.cpu.iowait 268.62 
system.cpu.stolen 0.0 
system.cpu.system 12015.86


-------------------------------------------------------------------------------------------

# MEM 

-------------------------------------------------------------------------------------------

python3 metrics.py mem

virtual total 16175804416 
virtual used 10338594816 
virtual free 848625664 
virtual shared 1459568640
swap total 4294434816 
swap used 22806528 
swap free 4271628288

-------------------------------------------------------------------------------------------

# For display host metrics from docker container I built image with psutil after that ran container with key and mount volumes

-------------------------------------------------------------------------------------------

docker build -t yuriig/psutil:latest .

docker push yuriig/psutil:latest

docker run --name psutil --pid host -d -ti --userns host -v /home/yg/projects/my/GL_Procamp:/tmp -v /etc/passwd:/etc/passwd:ro yuriig/psutil:latest

-------------------------------------------------------------------------------------------

docker exec -ti psutil python3 /tmp/metrics.py cpu

system.cpu.idle 504920.7 
system.cpu.user 31863.54 
system.cpu.guest 0.0 
system.cpu.iowait 271.66 
system.cpu.stolen 0.0 
system.cpu.system 12327.92

docker exec -ti psutil python3 /tmp/metrics.py mem

virtual total 16175804416 
virtual used 10718982144 
virtual free 485036032 
virtual shared 1460670464
swap total 4294434816 
swap used 22806528 
swap free 4271628288


-------------------------------------------------------------------------------------------
 
# Display pid on host

-------------------------------------------------------------------------------------------

top

17:10:54 up 1 day, 17:51,  1 user,  load average: 1.96, 1.73, 1.66
Tasks: 395 total,   1 running, 394 sleeping,   0 stopped,   0 zombie
%Cpu(s):  9.8 us,  4.4 sy,  0.0 ni, 85.4 id,  0.0 wa,  0.0 hi,  0.4 si,  0.0 st
MiB Mem :  15426.4 total,    484.2 free,  10189.7 used,   4752.5 buff/cache
MiB Swap:   4095.5 total,   4073.7 free,     21.8 used.   3595.1 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                         
   4984 yg        20   0 3737704 881080 191464 S  29.1   5.6  57:47.40 Web Content                                                                     
   4795 yg        20   0 6257132   1.4g 660420 S  13.6   9.0 171:26.75 firefox                                                                         
   2468 yg        20   0 1002732 152208  97828 S  12.6   1.0  37:58.32 Xorg                                                                            
   3079 yg        -2   0 5233524 355252 119888 S  11.3   2.2  41:58.81 gnome-shell                                                                     
   8317 yg        20   0  980500  79164  55204 S   8.6   0.5   3:26.32 tilix                                                                           
   2354 yg        20   0 3402936  22984  16984 S   7.9   0.1  35:56.54 pulseaudio                                                                      
   4893 yg        20   0   15.8g   1.0g 192076 S   6.0   7.0  44:21.88 Web Content                                                                     
   5035 yg        20   0 3430620 617876 172608 S   4.6   3.9  23:30.85 Web Content                                                                     
   4953 yg        20   0 9983.2m   1.1g 168060 S   3.6   7.3  62:33.57 Web Content                                                                     
   4963 yg        20   0 9914.9m 873548 183608 S   3.0   5.5  51:57.15 Web Content                                                                     
   5065 yg        20   0 3543360 753484 164644 S   3.0   4.8  61:57.68 Web Content                                                                     
   4945 yg        20   0 3614056 750392 173872 S   2.3   4.8  89:17.58 Web Content                                                                     
   5004 yg        20   0 4154140 765216 199380 S   2.3   4.8  45:07.70 Web Content                                                                     
   7683 yg        20   0 4629964 420396 112968 S   1.7   2.7  34:22.95 telegram-deskto                                                                 
   5586 yg        20   0  937544  79248  46524 S   1.3   0.5   0:11.52 nautilus                                                                        
   7415 yg        20   0 3209064 578124 109072 S   1.0   3.7  10:48.30 vlc                                                                             
  54637 root      20   0       0      0      0 I   1.0   0.0   0:08.01 kworker/6:3-events                                                              
   5200 yg        20   0 2754896 235004 100724 S   0.7   1.5   1:58.65 WebExtensions                                                                   
  55838 root      20   0       0      0      0 I   0.7   0.0   0:00.37 kworker/u16:4-events_unbound                                                    
  55950 yg        20   0   21920   4068   3256 R   0.7   0.0   0:00.10 top                                                                             
     11 root      20   0       0      0      0 I   0.3   0.0   2:23.94 rcu_sched                                                                       
    761 root       0 -20       0      0      0 I   0.3   0.0   1:00.97 kworker/u17:1-i915_flip                                                         
    783 root     -51   0       0      0      0 S   0.3   0.0   3:23.57 irq/132-rtw88_p                                                                 
    984 root      20   0   81900   3796   3456 S   0.3   0.0   0:07.65 irqbalance                                                                      
   1006 root      20   0  626080   5468   4848 S   0.3   0.0   1:12.11 system76-power                                                                  
   3918 yg        20   0  162836   7744   6964 S   0.3   0.0   0:05.93 at-spi2-registr                                                                 
   8157 yg        20   0 4699912 222980  84848 S   0.3   1.4   6:28.33 slack                                                                           
  10071 yg        20   0   14.6g 248024 115176 S   0.3   1.6   5:40.88 code                                                                            
  25468 root      20   0  113388   7552   6108 S   0.3   0.0   0:08.01 containerd-shim                                                                 
  47190 root       0 -20       0      0      0 I   0.3   0.0   0:14.98 kworker/u17:2-i915_flip                                                         
  49755 root      20   0       0      0      0 I   0.3   0.0   0:09.86 kworker/u16:5-phy0                                                              
  52984 root      20   0       0      0      0 I   0.3   0.0   0:04.69 kworker/u16:1-events_unbound                                                    
  53594 root      20   0       0      0      0 I   0.3   0.0   0:00.51 kworker/4:2-events                                                              
  54221 root      20   0       0      0      0 I   0.3   0.0   0:03.04 kworker/u16:3-events_unbound                                                    
  54222 root      20   0       0      0      0 I   0.3   0.0   0:02.97 kworker/u16:6-events_unbound                                                    
  54593 root      20   0       0      0      0 I   0.3   0.0   0:01.67 kworker/u16:2-events_unbound                                                    
  55313 root      20   0       0      0      0 I   0.3   0.0   0:00.10 kworker/0:1-events                                                              
      1 root      20   0  167952  12052   8580 S   0.0   0.1   0:05.77 systemd                                                                         
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.04 kthreadd                                                                        
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp
      

###############################################################################

# Display pids and usernames from host in container 

-------------------------------------------------------------------------------------------

docker exec -ti psutil sh

top

top - 15:13:13 up 1 day, 17:53,  0 users,  load average: 1.30, 1.52, 1.59
Tasks: 396 total,   1 running, 395 sleeping,   0 stopped,   0 zombie
%Cpu(s):  9.6 us,  4.1 sy,  0.0 ni, 86.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  15426.4 total,    492.5 free,  10185.9 used,   4748.0 buff/cache
MiB Swap:   4095.5 total,   4073.7 free,     21.8 used.   3605.8 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                         
   4984 yg        20   0 3737704 869308 191464 S  27.4   5.5  58:27.27 Web Content                                                                     
   4795 yg        20   0 6258608   1.4g 660588 S  12.2   9.1 171:54.85 firefox                                                                         
   2468 yg        20   0  995536 151436  97056 S  10.2   1.0  38:06.31 Xorg                                                                            
   3079 yg        -2   0 5233524 354724 119540 S   9.2   2.2  42:06.01 gnome-shell                                                                     
   8317 yg        20   0  980500  79164  55204 S   8.9   0.5   3:29.33 tilix                                                                           
   2354 yg        20   0 3402936  22984  16984 S   7.3   0.1  36:05.72 pulseaudio                                                                      
   4953 yg        20   0 9983.2m   1.1g 168060 S   6.6   7.1  62:41.27 Web Content                                                                     
   5035 yg        20   0 3431620 635104 172584 S   6.6   4.0  23:58.00 Web Content                                                                     
   4893 yg        20   0   15.8g   1.1g 192076 S   4.6   7.0  44:29.05 Web Content                                                                     
   8157 yg        20   0 4699912 222980  84852 S   4.3   1.4   6:29.68 slack                                                                           
   4963 yg        20   0 9907.9m 860228 183608 S   4.0   5.4  52:02.52 Web Content                                                                     
   5065 yg        20   0 3542656 752424 163940 S   2.6   4.8  62:03.12 Web Content                                                                     
   4945 yg        20   0 3622248 757128 173872 S   2.3   4.8  89:21.65 Web Content                                                                     
   5004 yg        20   0 4154140 757436 199380 S   2.3   4.8  45:12.00 Web Content                                                                     
   7683 yg        20   0 4629964 420372 112968 S   1.7   2.7  34:25.17 telegram-deskto                                                                 
   7415 yg        20   0 3209048 580660 109196 S   1.3   3.7  10:49.94 vlc                                                                             
  54637 root      20   0       0      0      0 I   1.0   0.0   0:09.09 kworker/6:3-events                                                              
  56045 root      20   0   10208   3800   3072 R   1.0   0.0   0:00.14 top                                                                             
  49755 root      20   0       0      0      0 I   0.7   0.0   0:10.02 kworker/u16:5-events_unbound                                                    
    761 root       0 -20       0      0      0 I   0.3   0.0   1:01.15 kworker/u17:1-i915_flip                                                         
    783 root     -51   0       0      0      0 S   0.3   0.0   3:23.87 irq/132-rtw88_p                                                                 
    970 avahi     20   0    8684   3760   3248 S   0.3   0.0   0:04.11 avahi-daemon                                                                    
   1681 root      20   0 3602672 106524  51892 S   0.3   0.7   1:27.23 dockerd                                                                         
   5147 yg        20   0 2629776 150792 101792 S   0.3   1.0   2:38.28 Privileged Cont                                                                 
   5200 yg        20   0 2754896 235004 100724 S   0.3   1.5   1:58.77 WebExtensions                                                                   
  47190 root       0 -20       0      0      0 I   0.3   0.0   0:15.16 kworker/u17:2-i915_flip                                                         
  49772 root      20   0       0      0      0 I   0.3   0.0   0:09.76 kworker/u16:10-events_unbound                                                   
  52707 root      20   0       0      0      0 I   0.3   0.0   0:04.58 kworker/u16:7-events_unbound                                                    
  54593 root      20   0       0      0      0 I   0.3   0.0   0:01.96 kworker/u16:2-phy0                                                              
  55310 root      20   0       0      0      0 I   0.3   0.0   0:00.26 kworker/7:1-events                                                              
      1 root      20   0  167952  12052   8580 S   0.0   0.1   0:05.79 systemd                                                                         
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.04 kthreadd                                                                        
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                                                                          
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                                                                      
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-kblockd                                                            
      9 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq                                                                    
     10 root      20   0       0      0      0 S   0.0   0.0   0:02.16 ksoftirqd/0                                                                     
     11 root      20   0       0      0      0 I   0.0   0.0   2:24.16 rcu_sched                                                                       
     12 root      rt   0       0      0      0 S   0.0   0.0   0:00.51 migration/0                                                                     
     13 root     -51   0       0      0      0 S   0.0   0.0   0:00.00 idle_inject/0 
     
     -------------------------------------------------------------------------------------------
