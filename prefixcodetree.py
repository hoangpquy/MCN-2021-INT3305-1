# Class New Node
class Node:
    def __init__(self, data):
        self.dataNode = data
        self.left = None
        self.right = None

    def isLeafNode(self):
        if ((self.left is None) and (self.right is None)):
            return True
        return False

# PrefixCodeTree class
class PrefixCodeTree:

    # Constructor function
    def __init__(self):
        self.root = Node('')

    # Insert function
    def insert(self, codeword, symbol):
        node = self.root

        for c in codeword:
            if (c == 0):
                if (node.left is None):
                    node.left = Node('')
                    node = node.left
                else:
                    node = node.left
            else:
                if (node.right is None):
                    node.right = Node('')
                    node = node.right
                else:
                    node = node.right

        node.dataNode = symbol

    # Decode function
    def decode(self, encodedData, datalen):
        message = ''

        # Transform encodeData to bit data
        bitData = ''.join(f'{_:08b}' for _ in encodedData)
        bitData = ''.join(bitData.split())
        bitData = bitData[:datalen]

        node = self.root

        for i in range(datalen):
            if (bitData[i] == '0'):
                node = node.left
            else:
                node = node.right
            if (node.isLeafNode()):
                message = message + node.dataNode
                node = self.root

        return message


def test():
    codeTree = PrefixCodeTree()

    codebook = {'x1': [0],
                'x2': [1,0,0],
                'x3': [1,0,1],
                'x4': [1,1]}

    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    print(codeTree.decode(b'\xd2\x9f\x20', 21))

if __name__ == "__main__":
    test()