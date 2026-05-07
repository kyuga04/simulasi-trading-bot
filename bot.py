import ccxt
import time

# --- KONFIGURASI ---
SYMBOL = 'BTC/USDT'

# Inisialisasi Bursa (Binance) - Tanpa API Key untuk ambil data publik
exchange = ccxt.binance()

def ambil_harga():
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker['last']

def simulasi_trading():
    print("=== BOT TRADING AI (SIMULASI) DIMULAI ===")
    saldo_virtual = 1000  # USDT palsu untuk latihan
    posisi_btc = 0
    
    while True:
        try:
            harga = ambil_harga()
            print(f"\nHarga {SYMBOL} saat ini: ${harga}")
            
            # LOGIKA SEDERHANA UNTUK LATIHAN
            if harga < 78000 and saldo_virtual > 0:
                print(">>> SINYAL: HARGA MURAH! Mencoba BELI.")
                posisi_btc = saldo_virtual / harga
                saldo_virtual = 0
                print(f"Status: Berhasil 'Beli' {posisi_btc:.5f} BTC (Simulasi)")
            
            elif harga > 82000 and posisi_btc > 0:
                print(">>> SINYAL: HARGA MAHAL! Mencoba JUAL.")
                saldo_virtual = posisi_btc * harga
                posisi_btc = 0
                print(f"Status: Berhasil 'Jual'! Saldo sekarang: ${saldo_virtual:.2f} USDT (Simulasi)")
            
            else:
                print(">>> STATUS: Menunggu momentum yang pas...")

            # Tunggu 10 detik sebelum cek lagi
            time.sleep(10)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    simulasi_trading()