# Private Broadcast: Warnet

## A Simulation to test https://github.com/bitcoin/bitcoin/pull/29415

## Requires https://github.com/bitcoin-dev-project/warnet

Deploy the network, start mining blocks and creating random transactions
that are broadcast randomly with or without private-broadcast.

```
warnet deploy networks/private-broadcast-100
warnet run scenarios/miner_std --allnodes --mature
warnet run scenarios/tx_flood --private-random --debug
```

## Monitor a single node's connection dashboard

```
watch warnet bitcoin rpc tank-0050 -netinfo 4
```

Multiple `priv` connections being made (outbound) as well as `onion` inbound
with user agent `pynode:0.0.1` from other privately-boradcasting peers:

![warnet terminal](./docs/terminal.png)


## Monitor the network using Grafana

```
warnet dashboard
```

![grafana dashboard](./docs/grafana.png)
