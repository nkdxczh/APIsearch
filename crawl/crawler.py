from catcher import catcher

c = catcher()
base = 'https://docs.oracle.com/javase/8/docs/api/'
c.set_url(base)
c.catch()
c.close()
