# Agentic-Tracker

Sanal Ortam (Virtual Environment) Oluşturun
Paketlerin bilgisayarınızdaki diğer projelerle karışmaması için izole bir ortam oluşturun. Backend klasörünün içindeyken şu komutu çalıştırın:

python -m venv venv

Sanal Ortamı Aktifleştirin

İşletim sisteminize göre aşağıdaki komutlardan uygun olanı seçerek oluşturduğunuz ortamı aktif hale getirin. (Terminal satırının başında (venv) yazısını görmelisiniz.)

.\venv\Scripts\activate

⚠️ Windows Kullanıcıları İçin Önemli Not: Eğer yukarıdaki komutu çalıştırdığınızda kırmızı renkli bir "yetki (Execution Policy)" hatası alırsanız, PowerShell'in güvenlik engelini aşmak için önce şu komutu çalıştırın: Set-ExecutionPolicy Unrestricted -Scope CurrentUser. Ardından aktifleştirme komutunu tekrar deneyin.

Gerekli Kütüphaneleri Kurun

Sanal ortamınız aktifken (venv), projenin çalışması için gereken tüm paketleri tek seferde kurun:

pip install -r requirements.txt

Sunucuyu Başlatın

Tüm kurulumlar tamamlandıktan sonra FastAPI sunucusunu ayağa kaldırmak için şu komutu kullanın:

uvicorn main:app --reload

🌐 API'yi Test Etme
Sunucu başarıyla başladığında terminalde Application startup complete. mesajını göreceksiniz.

Tarayıcınızı açıp aşağıdaki adreslere gidebilirsiniz:

API Çalışıyor mu?: http://127.0.0.1:8000

Otomatik API Dokümantasyonu (Swagger UI): http://127.0.0.1:8000/docs (Tüm uç noktaları buradan test edebilirsiniz)