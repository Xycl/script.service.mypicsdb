script.service.mypicsdb
=======================

Automatically updates MyPicsDB

You can also call it over JSON-RPC:
```powershell
powershell Invoke-WebRequest -UseBasicParsing 10.0.0.8:8080/jsonrpc -ContentType "application/json" -Method POST -Body '{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"Addons.ExecuteAddon\",\"params\":{\"addonid\":\"script.service.mypicsdb\"}}'
```

