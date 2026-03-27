import asyncio
from tonutils.client import LiteserverClient
from tonutils.wallet import WalletV4R2
from tonutils.utils import to_nano

async def send_ton_message():
    # 1. Connect directly to a Lite Server (No API Key needed)
    # Changed from mainnet to testnet as requested
    client = LiteserverClient.testnet() 
    await client.connect()

    # 2. Setup your wallet
    # Replace with your 24-word mnemonic phrase
    mnemonic = "ancient already anger arm base actual actress antenna annual bleak base alien bulb black bone area body bean awesome blame boat blur arrive binary"
    wallet, public_key, private_key, _ = WalletV4R2.from_mnemonic(client, mnemonic)

    # Display the wallet address as requested
    print(f"TON Wallet Address (Testnet): {wallet.address.to_str(is_user_friendly=True, is_bounceable=True)}")

    # 3. Define the message
    destination_address = "EQB..." # Send to yourself or a friend
    amount = to_nano(0.01, "ton")  # Tiny amount to carry the message
    comment = "This message is sent via TON Testnet!"

    # 4. Send the transaction
    print(f"Preparing to send message to: {destination_address}")
    tx_hash = await wallet.transfer(
        destination=destination_address,
        amount=amount,
        body=comment  # This is your message
    )

    print(f"Success! Transaction Hash: {tx_hash}")
    await client.close()


if __name__ == "__main__":
    asyncio.run(send_ton_message())