# RESTful API olarak TO-DO Uygulaması

- TO-DO uygulaması, kullanıcıların kendilerine yapılacaklar listesi oluşturup bu listeye görevler ekledikleri bir uygulamadır.
- Bu proje `Python` programlama dilinde `Flask` framework kullanılarak geliştirilmiştir.
- Proje `Postman Mock Service` kullanılarak test edilmiştir.

# Uygulamanın özellikleri

### Kayıtlı Kullanıcılar
1. `username`: bugra `password`: ates   --> normal kullanıcı
2. `username`: tevfik `password`: fikret   --> normal kullanıcı
3. `username`: admin `password`: admin   --> admin  
4. `username`: admin2 `password`: admin2   --> admin

### Request örnekleri

  Tüm kullanıcılar için:
  
-  HTTP Request: `POST`      
    - URL: `/login`
    - Açıklama: `JWT oturum anahtarı almak için kullanılır`
-  HTTP Request: `POST` `GET` `DELETE`      
    - URL: `/todoapp/api/todolist`
    - Açıklama: `Bir liste oluşturmak, listenin özelliklerini görmek veya listeyi silmek için kullanılır`
-  HTTP Request: `POST` `GET`      
    - URL: `/todoapp/api/tasks`
    - Açıklama: `Bir görev oluşturmak veya görevi görmek için kullanılır`
-  HTTP Request: `PUT`     
    - URL: `/todoapp/api/tasks/<task_id>/isdone`
    - Açıklama: `ID'si girilen taskın yapılma durumunu değiştirmek için kullanılır`
-  HTTP Request: `PUT`     
    - URL: `/todoapp/api/tasks/<task_id>/task` 
    - Açıklama: `ID'si girilen taskın içeriğini değiştirmek için kullanılır`
-  HTTP Request: `DELETE`      
    - URL: `/todoapp/api/tasks/<task_id>`
    - Açıklama: `ID'sı girilen taskı silmek için kullanılır`
    
    Sadece admin kullanıcılar için:
    
 -  HTTP Request: `GET`      
     - URL: `/todoapp/api/tasks/<user_name>`
     - Açıklama: `İsmi girilen kullanıcıya ait mevcut veya silinen tüm görevlerini görmek için kullanılır`
 -  HTTP Request: `GET`
     - URL: `/todoapp/api/todolists`
     - Açıklama: `Mevcut tüm kullanıcılara ait listeleri görmek için kullanılır`
     
     
  ### Uygulamanın kullanımı
  
  - Öncelikle yukarıda kullanıcı adı - şifreleri verilmiş olan hesaplar ve `/login` endpointi kullanılarak bir JWT oturum anahtarı alınır. Bu anahtar diğer tüm requestler için kullanılacaktır. Sonrasında `/todoapp/api/todolist` endpointine listenin ismiyle request gönderilerek bir to-do listesi oluşturulur. Bu listeye ait özellikler yine aynı endpointle görülebilir veya silinebilir. Kullanıcı bir yapılacaklar listesine sahipse `/todoapp/api/tasks` endpointine görevin içeriği yazılarak request gönderilip yeni bir görev oluşturulabilir. Mevcut bir görevin yapılma durumunu değiştirmek için `/todoapp/api/tasks/<task_id>/isdone` endpointine görevin ID'si girilir ve true false olarak request gönderilir. Aynı şekilde mevcut bir görevin içeriğini değiştirmek için ise `/todoapp/api/tasks/<task_id>/task` endpointine görevin ID'si girilir ve yeni içerik girilerek request gönderilir. (Aşağıdaki ekran görüntülerini inceleyiniz.)
  
 - Eğer yukarıda verilmiş olan admin hesaplarından birisiyle JWT oturum anahtarı alınmışsa bu anahtar girilerek sadece adminlerin kullanabileceği endpointlere request gönderilebilir.
 
 ### Bir Postman hesabınız varsa hazır olarak oluşturulmuş requestlere buton aracılığıyla erişebilirsiniz: [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/27173767-be3d82c6-9b32-4bbc-8e16-9441ce8b8161?action=collection%2Ffork&collection-url=entityId%3D27173767-be3d82c6-9b32-4bbc-8e16-9441ce8b8161%26entityType%3Dcollection%26workspaceId%3Da9cccdbf-d6bf-4294-8052-75191770783a)
 
 
 # Kullanıma Dair Bazı Ekran Görüntüleri
 
 - Login
 ![login](https://github.com/bugrates0/todoapp-restapi/assets/127054766/01872ba5-286c-4e3d-b566-b230a2d8e3e8)
 
 
 - JWT anahtarını girme
![JWT ANAHTARI NASIL GİRİLİR](https://github.com/bugrates0/todoapp-restapi/assets/127054766/9d31f476-c4a0-4fa6-a031-1d81cac110ec)
 
 
 - Liste oluşturma
![liste oluşturma](https://github.com/bugrates0/todoapp-restapi/assets/127054766/da9372ec-c09d-4367-9ec1-026b63b0c2b2)
 
 
 - Liste silme
 ![liste silme](https://github.com/bugrates0/todoapp-restapi/assets/127054766/1fd87512-9bbd-45c2-b038-41afc33c2691)
  
  
 - Görev oluşturma
 ![task olusturma](https://github.com/bugrates0/todoapp-restapi/assets/127054766/7b896796-6b52-459b-b695-7bf11ea2a6ac)


 - Görev güncelleme
![taskupdate1](https://github.com/bugrates0/todoapp-restapi/assets/127054766/7b9b95d8-b901-4347-8724-5b4831eb0d45)
![taskupdate2](https://github.com/bugrates0/todoapp-restapi/assets/127054766/f13b22d5-f3bd-4c50-8c19-8f607c246224)






