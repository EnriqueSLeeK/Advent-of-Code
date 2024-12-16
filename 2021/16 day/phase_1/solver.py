with open("input", "r") as f:
    transmission = f.readline().strip()

def hex_to_bin(digit):
    binary = bin( int(digit, 16) )[2:]
    return ("0" * (4 - len(binary)) + binary)

transmission_bin = ""

for k in range(len(transmission)):
    transmission_bin += hex_to_bin( transmission[k] )

version_sum = 0
pivot = 0

def get_literal_val():
    global pivot
    literal_val = ""
    while (True):
        segment = transmission_bin[pivot: pivot + 5]
        pivot += 5
        literal_val += segment[1: len(segment)]
        if (segment[0] == '0'):
            break
    return(int(literal_val, 2))

def i_zero(total_len, ref):
    global pivot
    while (pivot - ref < total_len):
        packet_parsing(get_header())

def i_one(total_quant):
    for k in range(total_quant):
        packet_parsing(get_header())

def packet_parsing(header):
    global pivot
    version, mode = header
#    print(version)
    if (mode == 4):
        return (get_literal_val())
    else:
        len_id = int(transmission_bin[pivot: pivot + 1], 2)
        pivot += 1

        if (len_id == 0):
            subpacket_total_len = int(
                    transmission_bin[pivot: pivot + 15], 2)
            pivot += 15
            i_zero(subpacket_total_len, pivot)

        elif (len_id == 1):
            subpacket_total_quant = int(
                    transmission_bin[pivot: pivot + 11], 2) 
            pivot += 11
            i_one(subpacket_total_quant)

def get_header():
    global pivot, version_sum
    version = int(transmission_bin[pivot: pivot + 3], 2)
    version_sum += version
    pivot += 3
    id = int(transmission_bin[pivot: pivot + 3], 2)
    pivot += 3
    return (version, id)

packet_parsing(get_header())
print(version_sum)
