import smtplib
longstring = """\
        _     _     _     _               _              _ 
       | |   (_)   | |   (_)             | |            | |
  _ __ | |__  _ ___| |__  _ _ __   __ _  | |_ ___   ___ | |
 | '_ \| '_ \| / __| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |
 | |_) | | | | \__ \ | | | | | | | (_| | | || (_) | (_) | |
 | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |  \__\___/ \___/|_|
 | |                               __/ |                   
 |_|                              |___/                    
                **author Kadir
"""
print longstring


emailGon = str(raw_input("Gonderen E-Mail Adres:"))

def baglan():
    emailPar = str(raw_input("Parola:"))
    sunucu = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    if (sunucu.login(emailGon, emailPar)):
        print "Oturum Basariyla Acildi"
        return sunucu

sunucu = baglan()

icerik = raw_input("Mail Icerigi").strip()

mailler = open("maillist.txt", "r")

alici = mailler.readlines()

try:
    for mail in alici:
        sunucu.sendmail(emailGon,mail, icerik)
    print "Mailler basarili bir sekilde gonderildi."

except EOFError:
    print "Mail gonderiminde hata"

mailler.close()
sunucu.quit()
