PyXOSnip
========

Linux screen capture and screen recording program inspired by scrot.
Forked from `Escrotum <https://github.com/Roger/escrotum>` _.

Why?
----

Because scrot has glitches when selection is used in refreshing windows.
Because escrotum isn't in active maintainment. I also hate its name so I'm using this as an opportunity to change it.

PyXOSnip stands for Python X Orange Snipper. Orange being a name I attach to some of my projects, and Snipper becaues I'd like to replicate most of the functionality in Microsoft's built-in Snipping Tool for Windows 10 (which is a pretty good tool, to be honest).


Features
--------

* fullscreen screenshots
* screen recording
* partial(selection) screenshots
* window screenshot(click to select)
* screenshot by xid
* store the image to the clipboard

::

    usage: pyxosnip [-h] [-v] [-s] [-x XID] [-d DELAY]
                    [--selection-delay SELECTION_DELAY] [-c] [-C] [-e COMMAND]
                    [-r]
                    [FILENAME]

    positional arguments:
      FILENAME              image filename, default is
                            %Y-%m-%d-%H%M%S_$wx$pyxosnip.png

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         output version information and exit
      -s, --select          interactively choose a window or rectangle with the
                            mouse, cancels with Esc or Right Click
      -x XID, --xid XID     take a screenshot of the xid window
      -d DELAY, --delay DELAY
                            wait DELAY seconds before taking a shot
      --selection-delay SELECTION_DELAY
                            delay in milliseconds between selection/screenshot
      -c, --countdown       show a countdown before taking the shot (requires
                            delay)
      -C, --clipboard       store the image on the clipboard
      -e COMMAND, --exec COMMAND
                            run the command after the image is taken
      -r, --record          screen recording. Alt+Ctrl+s to stop the recording

      SPECIAL STRINGS
      Both the --exec and filename parameters can take format specifiers
      that are expanded by pyxosnip when encountered.

      There are two types of format specifier. Characters preceded by a '%'
      are interpreted by strftime(2). See man strftime for examples.
      These options may be used to refer to the current date and time.

      The second kind are internal to pyxosnip and are prefixed by '$'
      The following specifiers are recognised:
      	$f image path/filename (ignored when used in the filename)
      	$w image width
      	$h image height
      Example:
      	pyxosnip '%Y-%m-%d-%H%M%S_$wx$h_pyxosnip.png'
      	Creates a file called something like 2013-06-17-082335_263x738_pyxosnip.png

      EXIT STATUS CODES
      1 can't get the window by xid
      2 invalid pixbuf
      3 can't save the image
      4 user canceled selection
      5 can't grab the mouse
      6 error with ffmpeg

Install
-------

* Working on this, it's not on pip or AUR yet
* You can always clone the repo and install it with setup.py
