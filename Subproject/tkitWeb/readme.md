

```
pip install tkitWeb  -i https://pypi.org/simple/
```

# 使用

```
import tkitWeb

th=tkitWeb.Http()
url="https://files.pythonhosted.org/packages/64/f8/434a36c186aefada16735bc6d8b489fbeaa0144419cf2a5f15033d0d129a/tkitFile-0.0.1.2.tar.gz"
name="tkitFile-0.0.1.2.tar.gz"
data=th.download(url,name,dirname='tfiles')
print(data)

```