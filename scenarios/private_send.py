#!/usr/bin/env python3

from commander import Commander

class PrivateSend(Commander):
    def set_test_params(self):
        # This is just a minimum
        self.num_nodes = 0
        self.miners = []

    def add_options(self, parser):
        parser.description = "Send a private transaction"
        parser.usage = "warnet run /path/to/private_send.py --sender=<tank_index> --to=<tank_index>"
        parser.add_argument(
            "--from",
            dest="sender",
            type=str,
            help="The tank to send from",
            required=True
        )
        parser.add_argument(
            "--to",
            dest="to",
            type=str,
            help="The tank to send to",
            required=True
        )
        parser.add_argument(
            "--amt",
            dest="amt",
            type=float,
            help="The amount in BTC to send (default: 0.01)",
            default=0.01,
            required=False
        )


    def run_test(self):
        sender = self.tanks[self.options.sender]
        recip = self.tanks[self.options.to]
        addr = recip.getnewaddress()
        created = sender.createrawtransaction([], [{addr: self.options.amt}])
        funded = sender.fundrawtransaction(created)
        signed = sender.signrawtransactionwithwallet(funded["hex"])
        txid = sender.sendrawtransaction(signed["hex"])
        self.log.info(txid)




def main():
    PrivateSend().main()


if __name__ == "__main__":
    main()
