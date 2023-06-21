<h2>initialize database</h2>
```bash
$ python init_db.py
```
<h2>run app</h2>
<h3>from star file folder:</h3>
```bash
$ uvicorn app:app
```
<h2>run tests</h2>
<h3>from star root folder:</h3>
```bash
$ pytest tests/test_cli.py
```
<h2>routes</h2>
<ul>
 <li>localhost:8000/ -> simple homepage</li>
 <li>localhost:8000/{username} -> plain text response, greets user</li>
 <li>localhost:8000/api/stars -> json response. list stars</li>
 <li>localhost:8000/api/throw/{star_name} -> plain text response. insert star</li>
</ul>

