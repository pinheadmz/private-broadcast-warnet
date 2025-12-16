#!/usr/bin/env python3

import threading
from time import sleep
from commander import Commander

class OnionAddrGossip(Commander):
    def set_test_params(self):
        # This is just a minimum
        self.num_nodes = 0
        self.miners = []

    def add_options(self, parser):
        parser.description = "Distribute onion addresses"
        parser.usage = "warnet run /path/to/onion_addr_gossip.py"

    def run_test(self):
        onions = []

        def get_onion(self, node):
            self.log.info(f"Getting local onion address from {node.tank}...")
            while True:
                info = node.getnetworkinfo()
                for addr in info["localaddresses"]:
                    if "onion" in addr["address"]:
                        onions.append(addr["address"])
                        self.log.info(f"{node.tank}: {addr['address']}")
                        return
                self.log.info(f"No onion address for {node.tank}, wait and retry...")
                sleep(5)
        addr_threads = [
            threading.Thread(target=get_onion, args=(self, node)) for node in self.nodes
        ]
        for thread in addr_threads:
            thread.start()
        all(thread.join() is None for thread in addr_threads)
        self.log.info(f"Got {len(onions)} addresses from {len(self.nodes)} tanks")

        def add_peers(self, node):
            self.log.info(f"Adding onion address to {node.tank}...")
            for addr in onions:
                node.addpeeraddress(addr, 18444)
        peer_threads = [
            threading.Thread(target=add_peers, args=(self, node)) for node in self.nodes
        ]
        for thread in peer_threads:
            thread.start()
        all(thread.join() is None for thread in peer_threads)
        self.log.info(f"Added {len(onions)} addresses to {len(self.nodes)} tanks")

def main():
    OnionAddrGossip().main()

if __name__ == "__main__":
    main()
