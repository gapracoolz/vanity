from curve import *
from bitcoin_standards import *
import secrets
from time import sleep, time

class VanityAddress:

    @staticmethod
    def address_generator(count, pattern=None):
        generator_point = Super256Point(BitcoinStandards.generatorPointX, BitcoinStandards.generatorPointY)

        with open('hasil.txt', 'w') as f:
            while True:
                priv_key = secrets.randbelow(BitcoinStandards.primeNumber)
                public_key = priv_key * generator_point
                compressed_pub_key = BitcoinStandards.compress_public_key(hex(public_key.x), hex(public_key.y))
                address = BitcoinStandards.compressed_public_key_to_wallet_address(compressed_pub_key)
                if pattern:
                    if address.startswith('1' + pattern):
                        f.write(f'Wallet Add : {address}, Private Key : {hex(priv_key)[2:]}\n')
                else:
                    f.write(f'Wallet Add : {address}, Private Key : {hex(priv_key)[2:]}\n')

        return None

if __name__ == '__main__':
    pass

# Print out hasil.txt
with open('hasil.txt', 'r') as f:
    print(f.read())