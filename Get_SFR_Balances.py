from privex.steemengine import SteemEngineToken
from beem import Steem
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList

#nodes = NodeList().get_nodes()
#stm = Steem(node=cfg.RPCNODE)
stm = Steem(node='https://api.steemit.com')
s = SteemEngineToken(network_account='ssc-mainnet1')
set_shared_steem_instance(stm)

balances = []
f = open("flagger.txt", "r")
flaggers = f.readlines()

for flagger in flaggers:
    fdict = {}
    flagger = flagger.replace('\n','')
    bal = s.get_token_balance(flagger, 'SFR')
    fdict = {'Flagger': flagger,'Balance': bal}
    balances.append(fdict)
    print(fdict)
