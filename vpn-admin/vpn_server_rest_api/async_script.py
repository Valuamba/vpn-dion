import sys
import asyncio

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


async def _read_stream(stream, cb):
    while True:
        line = await stream.readline()
        if line:
            cb(line)
        else:
            break


async def _stream_subprocess(cmd, stdout_cb, stderr_cb):
    try:
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        await asyncio.wait(
            [
                _read_stream(process.stdout, stdout_cb),
                _read_stream(process.stderr, stderr_cb),
            ]
        )
        rc = await process.wait()
        return process.pid, rc
    except OSError as e:
        # the program will hang if we let any exception propagate
        return e


def execute(*aws):
    """ run the given coroutines in an asyncio loop
    returns a list containing the values returned from each coroutine.
    """
    loop = asyncio.get_event_loop()
    rc = loop.run_until_complete(asyncio.gather(*aws))
    loop.close()
    return rc


def printer(label):
    def pr(*args, **kw):
        print(label, *args, **kw)

    return pr


def name_it(start=0, template="s{}"):
    """a simple generator for task names
    """
    while True:
        yield template.format(start)
        start += 1


def runners(cmds):
    """
    cmds is a list of commands to excecute as subprocesses
    each item is a list appropriate for use by subprocess.call
    """
    next_name = name_it().__next__
    for cmd in cmds:
        name = next_name()
        out = printer(f"{name}.stdout")
        err = printer(f"{name}.stderr")
        yield _stream_subprocess(cmd, out, err)


if __name__ == "__main__":
    cmds = (
        [
            "sh",
            "-c",
            """echo "$SHELL"-stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done""",
        ],
        [
            "bash",
            "-c",
            "echo 'hello, Dave.' && sleep 1 && echo dave_err 1>&2 && sleep 1 && echo done",
        ],
        [sys.executable, "-c", 'print("hello from python");import sys;sys.exit(2)'],
    )

    print(execute(*runners(cmds)))