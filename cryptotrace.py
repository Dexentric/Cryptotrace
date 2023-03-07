import requests, os
import json 
import pyfiglet
import streamlit
streamlit.write('Hello World')


result = pyfiglet.figlet_format("Dexentric Investigations", font ="digital")
print(result)
## API Key
##export APIKEY as environmental variable

apikey = os.getenv('APIKEY')
#sampledata
address = ''
txhash = ''
block_number = ''
timestamp = ''
smart_contract_address = ''
block_range = ''
topic = ''
tag = ''
bool = ''
index = ''

## This is to receive user Input
choices = {1:'Get Account Balance of an Address',2:'Get Normal Transactions of an Address',3:'Get Internal Transactions with a contract address',
4:'Get Internal Transactions by Transaction Hash',5:'Get Blocks Mined by an address',6:'Get Transaction Status by Hash',7:'Get Block Rewards',
8:'Get Block Countdown Time',9:'Get Block Number from Timestamp', 10:'Get All ERC20 token transfers',11:'Get ERC20 total supply balance',12:'Get ERC20 account balance',13:
'Total supply of ether', 14:'Ether last price', 15:'Contract ABI', 16:'Internal Transaction by block range', 17:'Get All ERC721 token transfers',
18:'Sample Logs', 19:'Recent block', 20: 'Block Info with BlockNo Hex', 21: 'Tx info with BlockNo and Tx index position'}


for i in range(len(choices.keys())):
	print(str(i+1)+'. '+choices[i+1])

status = True
while status==True:

	choice = int(input("Please Enter your Choice: "))


	if choice==1 or choice==2 or choice==3 or choice==5:
		address = input("Enter Address (sample: 0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a): ")
	elif choice==4 or choice==6 :
		txhash = input("Enter Hash (sample: 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170): ")
	elif choice==7 or choice==8:
		block_number = input("Enter Block Number (sample: 2165403): ")
	elif choice==9:
		timestamp = input("Enter Timestamp (sample: 1578638524): ")
	elif choice==10 or choice==17: 
		smart_address = input("Enter smart contract address (sample: 0xb809b9b2dc5e93cb863176ea2d565425b03c0540): ")
		address = input("Enter Address (sample: 0xfbc324f89831015a906b7daff97c7fd46c374413): ")
	elif choice==11 or choice==15:
		smart_address = input("Enter smart contract address (sample: 0x1f9840a85d5af5bf1d1762f925bdaddc4201f984): ")
	elif choice==12: 
		smart_address = input("Enter smart contract address (sample: 0xe583769738b6dd4e7caf8451050d1948be717679): ")
		address = input("Enter Address (sample: 0x2ed6b367c231c5e8fd7ea45ec5755c4f36fa0774): ")
	elif choice==13 or choice==14 or choice==16 or choice==19:
		print('Your request is being processed')
	elif choice==18:
		address = input("Enter Address (sample: 0xfbc324f89831015a906b7daff97c7fd46c374413):")
		topic = input("Enter topic0 address (sample: 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef): ")
	elif choice==20:
		tag = input("Enter block number in hex (sample: 0xC36B3C): ")
	elif choice==21:
		tag = input("Enter block number in hex (sample: 0xC36B3C): ")
		index = input("Enter the position of the uncle's index in the block, in hex (sample: 0x0): ")
		#bool = input("Enter boolean status (sample: True): ")
	#elif choice==16:
	    #block_range = input("Enter your block range number")
	else:
		print("Invalid Choice\n")

	## API Endpoints to call
	account_balance_url = 'https://api-goerli.etherscan.io/api?module=account&action=balance&address='+address+'&tag=latest&apikey='+apikey
	normal_transaction_by_address_url = 'https://api-goerli.etherscan.io/api?module=account&action=txlist&address='+address+'&startblock=0&endblock=99999999&sort=asc&apikey='+apikey
	internal_transactions_by_address_url = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&address='+address+'&startblock=0&endblock=99999999&sort=asc&apikey='+apikey
	internal_transactions_by_hash_url = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&txhash='+txhash+'&apikey='+apikey
	blocks_mined_by_address_url = 'https://api-goerli.etherscan.io/api?module=account&action=getminedblocks&address='+address+'&blocktype=blocks&apikey='+apikey
	transaction_receipt_status_by_hash_url = 'https://api-goerli.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash='+txhash+'&apikey='+apikey
	block_rewards_by_number_url = 'https://api-goerli.etherscan.io/api?module=block&action=getblockreward&blockno='+block_number+'&apikey='+apikey
	block_countdowntime_by_number_url = 'https://api-goerli.etherscan.io/api?module=block&action=getblockcountdown&blockno='+block_number+'&apikey='+apikey
	block_number_by_timestamp_url = 'https://api-goerli.etherscan.io/api?module=block&action=getblocknobytime&timestamp='+timestamp+'&closest=before&apikey='+apikey
	list_of_all_erc20_token_transfer_url = 'https://api-goerli.etherscan.io/api?module=account&action=tokentx&contractaddress='+smart_contract_address+'&address='+address+'&page=1&offset=100&startblock=0&endblock=99999999&sort=asc&apikey='+apikey
	erc20_token_totalsupply = 'https://api-goerli.etherscan.io/api?module=stats&action=tokensupply&contractaddress='+smart_contract_address+'&apikey='+apikey
	erc20_token_account_balance = 'https://api-goerli.etherscan.io/api?module=account&action=tokenbalance&contractaddress='+smart_contract_address+'&address='+address+'&tag=latest&apikey='+apikey
	total_supply_of_eth = 'https://api-goerli.etherscan.io/api?module=stats&action=ethsupply&apikey='+apikey
	ether_last_price = 'https://api-goerli.etherscan.io/api?module=stats&action=ethprice&apikey='+apikey
	contract_abi = 'https://api-goerli.etherscan.io/api?module=contract&action=getabi&address='+smart_contract_address+'&apikey='+apikey
	int_block_range = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&startblock=5783806&endblock=5783906&sort=asc&apikey='+apikey
	erc721_transfers= 'https://api-goerli.etherscan.io/api?module=account&action=tokennfttx&contractaddress='+smart_contract_address+'&address='+address+'&startblock=0&endblock=99999999&sort=asc&apikey='+apikey
	sample_logs = 'https://api-goerli.etherscan.io/api?module=logs&action=getLogs&fromBlock=2704019&toBlock=latest&address='+address+'&topic0='+topic+'&apikey='+apikey
	recent_block = 'https://api-goerli.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey='+apikey
	block_info = 'https://api-goerli.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag='+tag+'&boolean='+bool+'&apikey='+apikey
	Tx_info_by_block_hex = 'https://api-goerli.etherscan.io/api?module=proxy&action=eth_getTransactionByBlockNumberAndIndex&tag='+tag+'&index='+index+'&apikey='+apikey
	if choice==1:
		result = requests.post(account_balance_url).text
		result = json.loads(result)
		xy = pow(10,18)
		weitoether = int(result['result']) / xy
		print('Account Balance: '+str(weitoether)+' ether')
	elif choice==2:
		result = requests.post(normal_transaction_by_address_url).text
		result = json.loads(result)
		print('Number of Transactions: '+str(len(result['result'])))
		print('Transaction Blocks')
		for i in range(len(result['result'])):
			print(result['result'][i]['blockNumber'])
	elif choice==3:
		result = requests.post(internal_transactions_by_address_url).text
		result = json.loads(result)
		print('Internal Transaction by Address: '+str(len(result['result'])))
	elif choice==4:
		result = requests.post(internal_transactions_by_hash_url).text
		result = json.loads(result)
		for i in range(len(result['result'])):
			print(result['result'][i]['blockNumber'])
		print('Transaction Block: '+str(result['result']))
	elif choice==5:
		result = requests.post(blocks_mined_by_address_url).text
		result = json.loads(result)
		print('Number of Blocks: '+str(len(result['result'])))
		print('Transaction Blocks')
		for i in range(len(result['result'])):
			print(result['result'][i]['blockNumber'])
	elif choice==6:
		result = requests.post(transaction_receipt_status_by_hash_url).text
		result = json.loads(result)
		if(result['result']['status']==1):
			print('Success')
		else:
			print('Reverted')
	elif choice==7:
		result = requests.post(block_rewards_by_number_url).text
		result = json.loads(result)
		print('Block Reward: '+ result['result']['blockReward']+' wei')
	elif choice==8:
		result = requests.post(block_countdowntime_by_number_url).text
		result = json.loads(result)
		print('Countdown Time: '+result['result'])#['EstimateTimeInSec'])
		print('Current Block: '+result['result'])#['CurrentBlock'])
		print('Blocks Left: '+result['result'])#['RemainingBlock'])
	elif choice==9:
		result = requests.post(block_number_by_timestamp_url).text
		result = json.loads(result)
		print('Block Number: '+result['result'])
	elif choice==10: 
		result = requests.post(list_of_all_erc20_token_transfer_url).text
		result = json.loads(result)

		total = "The total number of ERC20 token transfer is : " + str(len(result['result']))
		print(total)
		print(" ")
		for i in result['result']:
			for key, value in i.items():
				print(f"{key} : {value}")
			print(" ")
	elif choice==11: 
		result = requests.post(erc20_token_totalsupply).text
		result = json.loads(result)
		cc = pow(10,18)
		wei_ether = int(result['result']) / cc
		print("ERC20 token total supply balance : " + str(wei_ether) + " ether")
	elif choice==12: 
		result = requests.post(erc20_token_account_balance).text
		result = json.loads(result)
		cc = pow(10,18)
		wei_ether = int(result['result']) / cc
		print("ERC20 token account balance : " + str(wei_ether) + " ether")
	elif choice==13:
		result = requests.post(total_supply_of_eth).text
		result = json.loads(result)
		print("total supply : " +str((result['result'])) + "ether")
	elif choice==14:
		result = requests.post(ether_last_price).text
		result = json.loads(result)
		print("last price: " +str(result['result']))
	elif choice==15:
		result = requests.post(contract_abi).text
		result = json.loads(result)	
		print('contract code: '+str(result['result']))
	elif choice==16:
		result = requests.post(int_block_range).text
		result = json.loads(result)
		print('block range: '+str(result['result']))
	elif choice==17:
		result = requests.post(erc721_transfers).text
		result = json.loads(result)
		print('ERC721 Transfers: '+str(len(result['result'])))
	elif choice==18:
		result = requests.post(sample_logs).text
		result = json.loads(result)
		print('Sample LOGS: '+str(len(result['result'])))
	elif choice==19:
		result = requests.post(recent_block).text
		result = json.loads(result)
		print('Recent Block: '+str(result['result']))
	elif choice==20:
		result = requests.post(block_info).text
		result = json.loads(result)
		print('Block Result: '+str(result['result']))
	elif choice==21:
		result = requests.post(Tx_info_by_block_hex).text
		result = json.loads(result)
		print('Tx Info: '+str(result['result']))
	Condition = input('Would you like to perform another transaction? y/n  ')
	if Condition=='n':
		status = False
		print('Thank you !!!')
