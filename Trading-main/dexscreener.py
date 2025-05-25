import requests

def get_top_pairs(limit=5):
    url = "https://api.dexscreener.com/latest/dex/pairs"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pairs = data.get("pairs", [])
        
        # On filtre les paires avec volume et prix valides
        filtered = [
            {
                "pair": p.get("pairSymbol"),
                "price": p.get("priceUsd"),
                "volume": p.get("volume", {}).get("h24"),
                "dex": p.get("dexId")
            }
            for p in pairs
            if p.get("priceUsd") and p.get("volume", {}).get("h24")
        ]
        return filtered[:limit]
    return []

