import time
import requests


MEMPOOL_API = "https://mempool.space/api/mempool/recent"


def fetch_recent_txs(limit=5):
    try:
        r = requests.get(MEMPOOL_API, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data[:limit]
    except Exception as e:
        print("error fetching mempool:", e)
        return []


def main():
    print("Bitcoin Radio core — listening to the network...\n")

    txs = fetch_recent_txs()

    if not txs:
        print("no transactions received")
        return

    for tx in txs:
        txid = tx.get("txid", "")[:10]
        vsize = tx.get("vsize")
        fee = tx.get("fee")
        print(f"tx {txid}… | vsize={vsize} | fee={fee}")

    print("\nmarket signal received")


if __name__ == "__main__":
    main()
