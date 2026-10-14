class Produk:
    BATAS_DISKON = 5000   
    PERSEN_DISKON = 5    

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        """Menampilkan informasi produk."""
        print(f"Nama Produk  : {self.nama}")
        print(f"Harga Produk : {rupiah(self.harga)}")

    def hitung_total(self, jumlah):
        """Menghitung total pembelian berdasarkan harga dan jumlah beli."""
        return self.harga * jumlah

    @staticmethod
    def hitung_diskon(total_semua):
        """Menghitung diskon 5% jika total seluruh pembelian lebih dari Rp5.000."""
        if total_semua > Produk.BATAS_DISKON:
            return total_semua * Produk.PERSEN_DISKON / 100
        return 0


def rupiah(angka):
    """Format angka menjadi format Rupiah, contoh: Rp10.000"""
    return "Rp" + f"{int(angka):,}".replace(",", ".")


def main():
    print("=== SISTEM PEMBELIAN PRODUK ===")
    jumlah_produk = int(input("Masukkan jumlah produk yang akan dibeli: "))

    total_seluruh = 0

    for i in range(1, jumlah_produk + 1):
        print(f"\n--- Produk ke-{i} ---")
        nama = input("Nama produk  : ")
        harga = int(input("Harga produk : "))
        jumlah_beli = int(input("Jumlah beli  : "))

        produk = Produk(nama, harga)
        total_produk = produk.hitung_total(jumlah_beli)
        total_seluruh += total_produk

        print()
        produk.tampilkan_info()
        print(f"Jumlah Beli  : {jumlah_beli}")
        print(f"Total        : {rupiah(total_produk)}")

    diskon = Produk.hitung_diskon(total_seluruh)
    total_bayar = total_seluruh - diskon

    print("\n=== HASIL PEMBELIAN ===")
    print(f"Total Pembelian : {rupiah(total_seluruh)}")
    print(f"Diskon 5%       : {rupiah(diskon)}")
    print(f"Total Bayar     : {rupiah(total_bayar)}")


if __name__ == "__main__":
    main()