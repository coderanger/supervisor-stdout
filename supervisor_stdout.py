import sys

COLORS = tuple(range(30, 38))

def get_color(key):
    use_string = key if isinstance(key, basestring) else str(key)
    return COLORS[use_string.__hash__() % len(COLORS)]

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
    while 1:
        write_stdout('READY\n') # transition from ACKNOWLEDGED to READY
        line = sys.stdin.readline()  # read header line from stdin
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len'])) # read the event payload
        write_stdout('RESULT %s\n%s'%(len(data), data)) # transition from READY to ACKNOWLEDGED

def event_handler(event, response):
    line, data = response.split('\n', 1)
    headers = dict([ x.split(':') for x in line.split() ])
    print '\033[1;%sm%s\033[1;m | \033[1;%sm%s\033[1;m | %s' % (get_color(headers['processname']),
                                                              headers['processname'],
                                                              get_color(headers['channel']),
                                                              headers['channel'],
                                                              data),

if __name__ == '__main__':
    main()
