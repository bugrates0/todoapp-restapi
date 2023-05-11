# RESTful API olarak TO-DO Uygulaması

- TO-DO uygulaması, kullanıcıların kendilerine yapılacaklar listesi oluşturup bu listeye görevler ekledikleri bir uygulamadır.
- Bu proje `Python` programlama dilinde `Flask` framework kullanılarak geliştirilmiştir.
- Proje `Postman Mock Service` kullanılarak test edilmiş, `render.com` sitesi aracılığıyla internette paylaşılmıştır.

# Uygulamanın özellikleri

### Kayıtlı Kullanıcılar
1. `username`: bugra `password`: ates   --> normal kullanıcı
2. `username`: tevfik `password`: fikret   --> normal kullanıcı
3. `username`: admin `password`: admin   --> admin  
4. `username`: admin2 `password`: admin2   --> admin

### Request örnekleri

  Tüm kullanıcılar için:
  
-  HTTP Request: `POST`      
    - URL: `https://todoapp-restapi.onrender.com/login`
    - Açıklama: `JWT oturum anahtarı almak için kullanılır`
-  HTTP Request: `POST` `GET` `DELETE`      
    - URL: `https://todoapp-restapi.onrender.com/todoapp/api/todolist`
    - Açıklama: `Bir liste oluşturmak, listenin özelliklerini görmek veya listeyi silmek için kullanılır`
-  HTTP Request: `POST` `GET`      
    - URL: `https://todoapp-restapi.onrender.com/todoapp/api/tasks`
    - Açıklama: `Bir görev oluşturmak veya görevi görmek için kullanılır`
-  HTTP Request: `PUT`     
    - URL: `https://todoapp-restapi.onrender.com/todoapp/api/tasks/<task_id>/isdone`
    - Açıklama: `ID'si girilen taskın yapılma durumunu değiştirmek için kullanılır`
-  HTTP Request: `PUT`     
    - URL: `https://todoapp-restapi.onrender.com/todoapp/api/tasks/<task_id>/task` 
    - Açıklama: `ID'si girilen taskın içeriğini değiştirmek için kullanılır`
-  HTTP Request: `DELETE`      
    - URL: `https://todoapp-restapi.onrender.com/todoapp/api/tasks/<task_id>`
    - Açıklama: `ID'sı girilen taskı silmek için kullanılır`
    
    Sadece admin kullanıcılar için:
    
 -  HTTP Request: `GET`      
     - URL: `https://todoapp-restapi.onrender.com/todoapp/api/tasks/<user_name>`
     - Açıklama: `İsmi girilen kullanıcıya ait mevcut veya silinen tüm görevlerini görmek için kullanılır`
 -  HTTP Request: `GET`
     - URL: `https://todoapp-restapi.onrender.com/todoapp/api/todolists`
     - Açıklama: `Mevcut tüm kullanıcılara ait listeleri görmek için kullanılır`
     
     
  ### Uygulamanın kullanımı
  
  - Öncelikle yukarıda kullanıcı adı - şifreleri verilmiş olan hesaplar ve `/login` endpointi kullanılarak bir JWT oturum anahtarı alınır. Bu anahtar diğer tüm requestler için kullanılacaktır. Sonrasında `/todoapp/api/todolist` endpointine listenin ismiyle request gönderilerek bir to-do listesi oluşturulur. Bu listeye ait özellikler yine aynı endpointle görülebilir veya silinebilir. Kullanıcı bir yapılacaklar listesine sahipse `/todoapp/api/tasks` endpointine görevin içeriği yazılarak request gönderilip yeni bir görev oluşturulabilir. Mevcut bir görevin yapılma durumunu değiştirmek için `/todoapp/api/tasks/<task_id>/isdone` endpointine görevin ID'si girilir ve true false olarak request gönderilir. Aynı şekilde mevcut bir görevin içeriğini değiştirmek için ise `/todoapp/api/tasks/<task_id>/task` endpointine görevin ID'si girilir ve yeni içerik girilerek request gönderilir.
  
 - Eğer yukarıda verilmiş olan admin hesaplarından birisiyle JWT oturum anahtarı alınmışsa bu anahtar girilerek sadece adminlerin kullanabileceği endpointlere request gönderilebilir.
 
 ### Bir Postman hesabınız varsa hazır olarak oluşturulmuş requestlere buton aracılığıyla erişebilirsiniz: [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/27173767-be3d82c6-9b32-4bbc-8e16-9441ce8b8161?action=collection%2Ffork&collection-url=entityId%3D27173767-be3d82c6-9b32-4bbc-8e16-9441ce8b8161%26entityType%3Dcollection%26workspaceId%3Da9cccdbf-d6bf-4294-8052-75191770783a)
 
 
 # Kullanıma Dair Bazı Ekran Görüntüleri
 
 - Login
 ![login](https://github.com/bugrates0/todoapp-restapi/assets/127054766/ea39c3ba-172d-4ada-b16a-9f87e30e2042)
 
 - JWT anahtarını girme
 ![JWT ANAHTARI NASIL GİRİLİR](https://github.com/bugrates0/todoapp-restapi/assets/127054766/b4153702-cebb-40ce-b65e-e5e9ba2dfbf5)
 
 - Liste oluşturma
![liste oluşturma](https://github.com/bugrates0/todoapp-restapi/assets/127054766/d14b70fd-9657-435e-b03d-27c93423ab85)
 
 - Liste silme
  ![liste silme](https://github.com/bugrates0/todoapp-restapi/assets/127054766/74417c33-de20-4ec8-9666-dfcd8e99a21a)
  
 - Görev oluşturma
 ![task olusturma](https://github.com/bugrates0/todoapp-restapi/assets/127054766/54af495e-931e-4252-bf40-b163109d5045)

 - Görev güncelleme
![taskupdate1](https://github.com/bugrates0/todoapp-restapi/assets/127054766/852bb3cf-8e30-4723-8ace-741824df209e)
![taskupdate2](https://github.com/bugrates0/todoapp-restapi/assets/127054766/e5ffb665-2da6-4da3-852b-3dc16a903d19)


# NOT:
- Uygulamayı internette paylaşmak için kullandığım `render.com` sitesinden kaynaklı olarak request gönderemediğim zamanlar oldu. Böyle bir şeyle karşılaşırsanız bana mail atabilirsiniz. Tekrar deploy ederek çözebilirim.


    



