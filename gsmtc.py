import mysql.connector
import time

# Veritabanı bağlantısı için gerekli bilgileri girin
database = input("GSM Databaseinizin ismini girin (Ornek: hacerdedegsm, 120mgsm): ")
frmname = input("GSM Databaseinizin frm ismini girin (Ornek: gsm.frm, 120mgsm.frm): ")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= database
)
# Cursor oluştur
mycursor = mydb.cursor()

gsm = input("GSM giriniz: ")

dosya_adi = database + "_" + gsm + ".txt"

# Verileri veritabanında ara ve sonucu yazdır
try:
    # GSM ile eşleşen kaydı seç
    sql = f"SELECT * FROM {frmname} WHERE GSM = '{gsm}'"

    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for i in mycursor:
            tc = i[0]
            
            dosya.write(f"TC:{tc}, GSM: {gsm}\n".encode())
            
    print(f"Gsm {dosya_adi} dosyasına kaydedildi.")
     # Tüm sonuçları yazdır
    results = mycursor.fetchall()
    if len(results) > 0:
        for result in results:
            tc = result[0]
            gsm = result[1]

            print(f"TC: {tc}")
            time.sleep(5)
    else:
        print("Eşleşen veri yok.")

except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
