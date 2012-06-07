# supervisor-stdout

A simple [supervisord](http://supervisord.org/) event listener to relay
process output to supervisor's stdout.

This is useful in situations where the output will be collected and set to
external logging framework, such as Heroku.

## Installation

Just install via pip or add to your requirements.txt:

    pip install supervisor-stdout

## Usage

An example supervisord.conf:

    [supervisord]
    nodaemon = true

    [program:web]
    command = ...
    stdout_events_enabled = true
    stderr_events_enabled = true

    [eventlistener:stdout]
    command = supervisor_stdout
    buffer_size = 100
    events = PROCESS_LOG
    result_handler = supervisor_stdout:event_handler
