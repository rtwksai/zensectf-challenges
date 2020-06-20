# AES it !!!

### Author: keiser

So Hemanth knew about Rithwik and hence had a challenge ready on a safer side for emergency purposes. He believes this would teach the concepts of AES way better than the previous question.

Connect to `nc chal.zense.co.in 6955` to access the challenge

Message from the author: It is requested that you test the exploit locally first and then try to implement the exploit by connecting, as results are fast if you test locally. Once you are able run the exploit successfully locally, run the exploit on the server to get the actual flag

Steps to reproduce the challenge locally:
- Download the file `server.py`
- Make a file named `secret.py` and add this in your file
```python3
FLAG = <some random flag>
KEY = <some random key of length as multiple of 16>
```
- Now fire up the server using `python3 server.py`
- Now open another terminal and join as client using `nc localhost 6955`