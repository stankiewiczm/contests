import urllib;
import urllib2;
import requests;

#urllib2.urlopen("http://img-9gag-ftw.9cache.com/photo/a1Zyx4Y_700b.jpg");


urllib.urlretrieve("http://img-9gag-ftw.9cache.com/photo/a1Zyx4Y_700b.jpg", "File1.jpg");


urllib2.urlopen("http://img-9gag-ftw.9cache.com/photo/a1Zyx4Y_700b.jpg");
data = urllib2.urlopen("http://img-9gag-ftw.9cache.com/photo/a1Zyx4Y_700b.jpg").read();

#with open("file.jpg", "wb") as code:
#    code.write(data);
    
r = requests.get(url);
with open("file3.jpg", "wb") as code:
    code.write(r.content);
