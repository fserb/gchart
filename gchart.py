"""
Actually useful Google Chart API in Python
"""

import urllib
import webbrowser

def scale(seqs, maxv=None, minv=None):
  if minv is None: minv = min(min(s) for s in seqs)
  if maxv is None: maxv = max(max(s) for s in seqs)
  delta = maxv-minv
  if delta == 0:
    delta = minv
    minv *= 0.5
  for seq in seqs:
    data = []
    for s in seq:
      if s == None:
        data.append(None)
      else:
        data.append( (float(s) - minv)/delta )
    yield data


def st(seqs, maxv=None, minv=None):
  """
  Generate a standard encoded data for chart data. Also rescale as needed.
  """
  map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  dataset = []
  for seq in scale(seqs, maxv, minv):
    data = []
    for s in seq:
      if s == None:
        data.append('_')
      else:
        x = int(round(s*(len(map)-1), 0))
        data.append(map[x])
    dataset.append(''.join(data))
  return 's:'+','.join(dataset)


def text(seqs, maxv=None, minv=None):
  dataset = []
  for seq in scale(seqs, maxv, minv):
    data = []
    for s in seq:
      if s == None:
        data.append('-1')
      else:
        data.append('%.4f' % (s*100.0))
    dataset.append(','.join(data))
  return 't:' + '|'.join(dataset)


def url(**opts):
  k = opts.keys()
  k.sort()
  url = ('http://chart.apis.google.com/chart?' + 
         urllib.urlencode([ (p, opts[p]) for p in k ]))
  return url


def show(**opts):
  new = opts.get('new', 0)
  autoraise = opts.get('autoraise', 1)
  if 'new' in opts: del opts['new']
  if 'autoraise' in opts: del opts['autoraise']
  return webbrowser.open(url(**opts), new=new, autoraise=autoraise)


def save(filename, **opts):
  urllib.urlretrieve(url(**opts), filename+'.png')


def html(**opts):
  d = [ "<img src='%s'" % url(**opts) ]
  if 'chs' in opts:
    w,h = opts['chs'].split('x')
    d.append(" style='width:%spx;height:%spx'" % (w,h))
  if 'cht' in opts:
    d.append(" class='%s'" % opts['cht'])
  d.append(">")
  return ''.join(d)
