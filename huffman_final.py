from heapq import heappush, heappop, heapify
from collections import defaultdict
CharOccur = defaultdict(int)
dl=dc=[]
def encode(CharOccur):
	heap = [[num, [lett, ""]] for lett, num in CharOccur.items()]
	heapify(heap)
	while len(heap) > 1:
		low = heappop(heap)
		high = heappop(heap)
		for pair in low[1:]:
			pair[1] = '0' + pair[1]
		for pair in high[1:]:
			pair[1] = '1' + pair[1]
        	heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
	return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    
def frequency(input_str):
	for ch in input_str:
		CharOccur[ch] += 1

def printhuffcode(huff,dl):
	print "Letter\tOccurance\tHuffman Code"	
	for p in huff:
    		print "  %s\t   %s\t\t   %s" % (p[0], CharOccur[p[0]], p[1])
		dl.append(p[0])		
		dc.append(p[1])
	return dl

def decode(input_code,dl):
	i=0
	while i<=len(dl)-1:
		if input_code==dl[i]:
			print dl[i-1]
		i=i+1 
			

def main():
	print "Enter the String"	
	input_str=raw_input()
	frequency(input_str)
	huff = encode(CharOccur)
	printhuffcode(huff,dl)
	print "Enter the Code"
	input_code=raw_input()
	decode(input_code,dl)
if __name__ == '__main__':
	main()
