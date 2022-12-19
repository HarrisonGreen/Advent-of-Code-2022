from ast import literal_eval

file = open("Data/day13.txt", "r")
packets = []

for line in file:
    if line == "\n":
        continue

    packets.append(literal_eval(line))

def correct_order(packet_one, packet_two):

    if type(packet_one) == list and type(packet_two) == list:

        for i in range(min(len(packet_one), len(packet_two))):
            result = correct_order(packet_one[i], packet_two[i])

            if result != "Unsure":
                return result
        
        if len(packet_one) < len(packet_two):
            return True
        elif len(packet_one) > len(packet_two):
            return False
        else:
            return "Unsure"
    
    if type(packet_one) == list and type(packet_two) == int:
        return correct_order(packet_one, [packet_two])
    
    if type(packet_one) == int and type(packet_two) == list:
        return correct_order([packet_one], packet_two)

    if type(packet_one) == int and type(packet_two) == int:
        if packet_one < packet_two:
            return True
        elif packet_one > packet_two:
            return False
        else:
            return "Unsure"

total = 0

for i in range(len(packets)//2):
    total += (i + 1) * correct_order(packets[2 * i], packets[2 * i + 1])

print(f"Part one: {total}")

packets.append([[2]])
packets.append([[6]])

sorted_packets = [packets.pop(0)]

while packets:
    current = packets.pop(0)
    pos = -1

    while True:
        pos += 1
        is_before = correct_order(current, sorted_packets[pos])

        if is_before:
            sorted_packets = sorted_packets[:pos] + [current] + sorted_packets[pos:]
            break
        elif pos == len(sorted_packets) - 1:
            sorted_packets.append(current)
            break

decoder_key = 1

for i, packet in enumerate(sorted_packets):
    if packet in ([[2]], [[6]]):
        decoder_key *= (i + 1)

print(f"Part two: {decoder_key}")
