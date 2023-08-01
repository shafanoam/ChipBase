import re


testList = [('74ls', '74ls00', 'Quad NAND Gate'), ('74ls', '74ls04', 'Hex Inverter'), ('74ls', '74ls08', 'Quad OR Gate'), ('N/A', 'quad/A', 'ALU')]
print(testList)

goodList = [chip for chip in testList if re.search('Quad'.lower(), str(chip).lower())]
print(goodList)
