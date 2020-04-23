## EBA Answer Parser
#### Gerekli Modüllerin Kurulumu
    pip install Pillow
	pip install colorama
	pip install requests

#### Kullanım Anlatımı
*Gerekli modülleri yüklediğinizi varsayarak anlatıyorum.*

Her şeyden önce kodların bulunduğu dizinde `answers` adında bir klasör açmalısınız. Ardından çözdüğünüz test(ler)in cevaplarını indirmek için `config` dosyası üzerinde çeşitli yerleri düzenlemeniz lazım.

`config` dosyasındaki `cookie` değişkenine  halihazırda açık olan EBA Akademi oturumunuzun çerezini girmelisiniz. Çerezi çekmeniz için çeşitli yöntemler var, ben Google Chrome'da bulunan F12 menüsünün Network sekmesi üzerinden çekmeyi tercih ediyorum.


Çerezi düzenledikten sonra düzenlemeniz gereken iki şey kalıyor: ```examid``` ve ```applicationids```.  İkisini de aynı şekilde Network sekmesi üzerinden çekebilirsiniz ancak bu iki veriyi testi bitirdikten sonra açarken gelen ```viewperformance.json``` isteğinden elde edebilirsiniz.

`examid`yi bir sefere mahsus değiştirmeniz yeterli olabiliyor. İlk kullanımdan sonra başka bir testin cevaplarını çekerken `examid`yi değiştirmenize gerek kalmıyor. Bu yüzden çözdüğünüz testlerin ayırt edici anahtarı `applicationid` oluyor. Birden çok testin cevaplarını çekebilmek amacıyla `config` dosyası üzerinde `applicationids` adında bir liste türünde değişken oluşturma gereği duydum, birden fazla testin `applicationid`'sini liste içine girebilirsiniz.

Ve hayır, **çözmediğiniz testlerin cevaplarını çekemezsiniz.**
