from block import Block
import datetime
number_of_blocks=int(input("Enter the umber of blocks"))
num_blocks_to_add = number_of_blocks

block_chain = [Block.genesis_block()]

print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)

for i in range(1, num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
