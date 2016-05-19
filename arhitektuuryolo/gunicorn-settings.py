#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_arhitektuuryolo.sock"

workers = 2
proc_name = "arhitektuuryolo"
#loglevel = 'debug'
