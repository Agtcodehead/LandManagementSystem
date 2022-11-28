import hashlib
import json
from random import randint

class Blockchain:
    def __init__(self):
        self.chain = ()
        self.nodes = []
        self.stake = []
        self.power = []
        self.vote_strength = []
        self.votes = []
    
    def create_block(self, previous_hash, proof_of_delegated_stake, tr_list, hash):
        block = {'Index': len(self.chain) + 1,
                 'Previous Hash': previous_hash,
                 'Maxiumum Votes': proof_of_delegated_stake,
                 'Merkle Root Hash': hash,
                 'Transactions': tr_list
                }
        #print(block)
        temp_list = list(self.chain)
        temp_list.append( block )
        self.chain = tuple(temp_list)

        return block
    
    def latest_block(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    '''
    def proof_of_delegated_stake(self):
        file = open("user_stats.json", "r")
        data = json.loads(file.read())
        for i in data["user_stats"]:
            self.nodes.append(i["username"])
            propstr = i["properties_owned"]
            #stakes = (1+propstr.size())/2
            stakes = len(propstr)
            self.stake.append(stakes)

        for i in range(len(self.nodes)):
            self.power.append(int(self.stake[i]) * randint(1,100))
        self.power = list(zip(self.power,self.nodes))
        self.power.sort(reverse=True)
        return self.power[0][0]'''

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while(current_index<len(chain)):
            block = chain[current_index]
            #If the hash value of the current block isn't correct then return false
            if(block['previous_hash']) != self.hash(last_block):
                return False
            last_block = block
            current_index += 1
        return True





    def proof_of_delegated_stake(self):
        file = open("user_stats.json", "r")
        data = json.loads(file.read())
        for i in data["user_stats"]:
            self.nodes.append(i["username"])
            propstr = i["properties_owned"]
            stakes = len(propstr)
            price = 0
            self.vote_strength.append(price)
            for j in range(stakes):
                new_file = open("property_stats.json")
                new_data = json.loads(new_file.read())
                new_prop = "Property " + propstr[j]
                price += int(new_data[new_prop]["price"])
                self.vote_strength[-1] = price
                new_file.close()
        file.close()
        for i in range(len(self.nodes)):
            self.votes.append(0)

        for i in range(len(self.vote_strength)):
            n = randint(0,len(self.nodes)-1)
            self.votes[n] += self.vote_strength[i]
        self.votes.sort(reverse=True)
        return self.votes[0]




    def merkle_hash(self,tr_list):
        transactions = []
        transactions.append(tr_list[0][0])
        transactions.append(tr_list[1][0])
        transactions.append(tr_list[2][0])
        transactions.append(tr_list[3][0])
        hash1 = []
        for i in range(4):
            hash1.append(hashlib.sha256(str(transactions[i]).encode()).hexdigest())

        hash2 = []
        hash2.append(hash1[0]+hash1[1])
        hash2.append(hash1[2]+hash1[3])
        hash2[0] = hashlib.sha256(str(hash2[0]).encode()).hexdigest()
        hash2[1] = hashlib.sha256(str(hash2[1]).encode()).hexdigest()

        hash = hashlib.sha256((hash2[0]+hash2[1]).encode()).hexdigest()
        return hash
        

    def mine_block(self,tr_list,hash):
        if len(self.chain)==0:
            previous_hash = self.hash('Genesis Block')
            proof_of_delegated_stake = 1 * randint(0,100)
        else:
            previous_hash = self.hash(self.latest_block())
            proof_of_delegated_stake = self.proof_of_delegated_stake()
        #proof_of_delegated_stake = self.proof_of_delegated_stake
        self.create_block(previous_hash, proof_of_delegated_stake, tr_list, hash)
        #import storeTransaction
        #storeTransaction.store_data(tr_list)
        #storeTransaction.modify_data(tr_list)