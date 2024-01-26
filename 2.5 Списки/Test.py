
protocols = [[], ['tcp'], ['udp'], ['icmp'], ['gre'], ['esp'], ['igmp'], ['ah'], ['tcp', 'udp']]
test = [["tcp"], ["udp"], ["icmp"], ["tcp", "udp"]]
test1 =[["tcp"], ["udp"], ["icmp"], ["tcp", "udp"]]
for i in range (len(protocols)):
    if protocols[i] in [["tcp"], ["udp"], ["icmp"], ["tcp", "udp"]]:
        print("Go! ", protocols[i])
    else:
        print ("No ", protocols[i])