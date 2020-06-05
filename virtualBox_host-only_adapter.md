두 가지 설정 필요. 

### VirtualBox

VirtualBox -> Setting -> network -> host-only network -> (+)

DHCP setting
server addr: 192.168.56.100
server mask: 255.255.255.0
L : 192.168.56.101
U : 192.168.56.254

user DHCP server (check)


### Guest OS

setting -> network -> adapter 2

Use network adapter (check)
host-only adapter
vboxnet0
