import mysql.connector

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

# Verileri veritabanında ara ve sonucu yazdır
try:
    # GSM ile eşleşen kaydı seç
    sql = f"SELECT * FROM {frmname} WHERE GSM = '{gsm}'"

    # Sorguyu çalıştır
    mycursor.execute(sql)

     # Tüm sonuçları yazdır
    results = mycursor.fetchall()
    if len(results) > 0:
        for result in results:
            tc = result[0]
            gsm = result[1]
            print(f"TC: {tc}")
            print(f"GSM: {gsm}")
    else:
        print("Eşleşen veri yok.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
