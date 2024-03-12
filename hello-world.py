print("Hello world")
for i in range(1, 2094):
    # print("Второй октет: ", i // 254, " Третий октет: ", i % 256)
    ip_addr="11." + str(i // 254) +"."+str(i % 256) + ".1/24"
    print(ip_addr)
