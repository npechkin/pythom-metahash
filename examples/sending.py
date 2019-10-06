#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass

################################################
net = 'main'
address = '0x00'
#passwd = '12345' # for *.ec.priv
passwd = getpass ("password:") # for *.ec.priv
value = '0' # 1 MHC = 1000000
to = '0x0088825ae25e516a34cb94bada9b25a811213b55ae3160c888'

#################  KEY LOAD   ##################
## EC PEM private key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )

##################   SEND MHC   ###################
fee = '0'
nonce = metahash.fetch_balance( net, address )['result']['count_spent'] + 1
data = ''
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )

####################   END   ######################
