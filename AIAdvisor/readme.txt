1. for all users�� python ��ġ
2. mysql python connector ��ġ
3. mysql�� base.py ���Ͽ��� �Ʒ��� ���� ����
import pymysql
pymysql.install_as_MySQLdb()
try:
    import MySQLdb as Database
except ImportError as e:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured("Error loading MySQLdb module: %s" % e)

if there is a c++ error when you use pip for install py package, add environmental variable on your system with name as vc100.
(pip c++ error �߻� �� ���� c++ compiler ��ġ�� vc10�� �̸����� �ϳ� ���� ȯ�溯���� �߰����ָ� �ȴ�)

Since django with version 1.9 is unstable, download version 1.8.13 which is latest one today(07.Jul.16)

to use hmmlearn, you need to install numpy with mkl which is available on the http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy


i made a requirements.txt using pipreqs. if you type "pip install -U -r requirements.txt " on your cmd window, then all of required packages will be installed automatically
