# 🚀 Kodyazabil.me - Kişisel Eğitim ve Portfolyo Platformu

**Kodyazabil.me**, Python, Django ve Dijital Erişilebilirlik üzerine odaklanmış bir eğitim platformu ve kişisel portfolyo projesidir.

Bu proje, görme engelli bireyler için erişilebilir yazılım geliştirme pratiklerini benimseyerek, modern web teknolojileri (Django & Tailwind CSS) ile geliştirilmiştir.

## 🛠 Kullanılan Teknolojiler

* **Backend:** Python 3.x, Django 5.x
* **Frontend:** HTML5, Tailwind CSS
* **Editör:** Django CKEditor (Zengin Metin Editörü)
* **Sunucu:** Nginx, Gunicorn, Systemd (Linux/Debian)
* **Veritabanı:** SQLite (Geliştirme) / PostgreSQL (Prodüksiyon - Opsiyonel)

---

## 💻 Kurulum (Local Development)

Bu projeyi kendi bilgisayarınızda (Lokal) çalıştırmak için aşağıdaki adımları izleyin.

### 1. Projeyi Klonlayın
Kullanıcı adınızı linkteki ilgili yere yazarak şu komutu çalıştırın:
`git clone https://github.com/kullaniciadiniz/kodyazabil.me.git`

Ardından proje klasörüne girin:
`cd kodyazabil.me`

### 2. Sanal Ortamı (Virtual Environment) Oluşturun
Python paketlerini izole etmek için sanal ortam kurun.

Windows için:
`python -m venv venv` komutunu ve ardından `.\venv\Scripts\activate` komutunu çalıştırın.

Linux/Mac için:
`python3 -m venv venv` komutunu ve ardından `source venv/bin/activate` komutunu çalıştırın.

### 3. Gereksinimleri Yükleyin
Gerekli kütüphaneleri kurmak için:
`pip install -r requirements.txt`

### 4. Veritabanını Oluşturun
`python manage.py migrate`

### 5. Sunucuyu Başlatın
`python manage.py runserver`

Tarayıcınızda http://127.0.0.1:8000/ adresine giderek projeyi görebilirsiniz.

---

## 🌍 Sunucu Kurulumu (Production)

Bu proje canlı sunucuda (Production) çalışırken güvenlik ve performans ayarlarını otomatik olarak yapar.

**Önemli:** Sunucuda settings.py dosyasının "Canlı Mod"da olduğunu anlaması için Gunicorn servis dosyasında veya ortam değişkenlerinde şu ayarın yapılması gerekir:
`export KODYAZABIL_PROD=True`

Bu değişken tanımlı olduğunda DEBUG = False olur ve güvenlik duvarları devreye girer.

---

## 🔄 Dağıtım ve Güncelleme Rehberi (Deployment Workflow)

Proje **Lokal (Bilgisayar)** ve **Prodüksiyon (Sunucu)** olmak üzere iki aşamalı yönetilir. Çakışmaları önlemek için aşağıdaki kurallara **kesinlikle** uyulmalıdır.

⚠️ **Temel Kural:** Üretim yeri **Lokal Bilgisayar**, tüketim yeri **Sunucu**dur. Asla sunucuda doğrudan kod değişikliği veya migration oluşturma işlemi yapılmamalıdır.

### 1. Senaryo: Kod veya Tasarım Güncellemesi
*(HTML, CSS, View veya Python mantığı değiştiğinde)*

**Lokal Bilgisayarda:**
Sırasıyla `git add .` , `git commit -m "Mesajınız"` ve `git push` komutlarını uygulayın.

**Sunucuda:**
Klasöre gidip `git pull` yapın ve ardından `sudo systemctl restart kodyazabil` komutuyla servisi yenileyin.

### 2. Senaryo: Veritabanı Modeli Değişikliği
*(Yeni tablo eklendiğinde veya model alanları değiştiğinde)*

**Lokal Bilgisayarda:**
Önce `python manage.py makemigrations` ve `python manage.py migrate` ile test edin.
Sonra `git add .` , `git commit -m "Veritabanı güncellendi"` ve `git push` ile gönderin.

**Sunucuda:**
Kodları çektikten (`git pull`) sonra sanal ortamı aktif edin ve sadece `python manage.py migrate` komutunu uygulayın. Son olarak `sudo systemctl restart kodyazabil` yapın.

### 3. Senaryo: Yeni Kütüphane Eklendi
*(pip install ile yeni bir paket kurulduğunda)*

**Lokal Bilgisayarda:**
`pip freeze > requirements.txt` ile listeyi güncelleyip gönderin (`git push`).

**Sunucuda:**
Kodları çektikten sonra `pip install -r requirements.txt` ile paketi kurun. Eğer CSS dosyası varsa `python manage.py collectstatic --noinput` yapın ve servisi yeniden başlatın.

---

## 🛑 Kritik Uyarılar (Asla Yapılmayacaklar)

1.  **Sunucuda makemigrations YAPMA:**
    Bu, dosya çakışmasına (conflict) neden olur. Migration dosyaları lokalde oluşturulup sunucuya gönderilmelidir.
    
2.  **Sunucuda Kod Değiştirme:**
    Sunucuda nano vb. ile dosya düzenlersen git pull işlemi hata verir. Değişikliği lokalde yapıp gönder.

3.  **Servisi Yeniden Başlatmayı Unutma:**
    `sudo systemctl restart kodyazabil` komutu çalıştırılmazsa, Gunicorn eski kodları kullanmaya devam eder.

---

## 🤝 İletişim

Geliştirici: **Bora FIRLANGEÇ**
Web: https://kodyazabil.me