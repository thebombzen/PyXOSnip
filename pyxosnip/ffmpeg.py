import os
import subprocess
from .util import cmd_exists


class Ffmpeg:
    def __init__(self, x, y, w, h, output):
        self.x, self.y = x, y
        self.w, self.h = w, h

        self.output = output

        self.display = os.environ['DISPLAY']
        if cmd_exists('ffmpeg'):
            self.binary = 'ffmpeg'
        elif cmd_exists('avconv'):
            self.binary = 'avconv'
        else:
            raise Exception('ffmpeg or avconv not found')

    def start(self):
        video_input = f'{self.display}+{self.x},{self.y}'
        video_size = f'{self.w}x{self.h}'
        # Based on presets from
        # EasyScreenCast GNOME Extension
        # Google's Media Core Technologies Live Encoding examples
        cmd = [
            self.binary,
            '-loglevel', 'error',
            # force overwrite file
            '-y',
            '-hide_banner',
            '-f', 'x11grab',
            '-video_size', video_size,
            # TODO get actual monitor refresh rate, via RandR, or pass via __init__
            '-framerate', '60',
            '-i', video_input,
            # Realtime grabbing should use x264. VP9 and later codecs too slow
            # TODO allow enabling a hardware encoder on the CLI
            '-c:v', 'libx264',
            # This is a very low CRF. should postproc it later.
            '-crf:v', '12',
            # Ultrafast turns off too many features
            # TODO make configurable
            '-preset:v', 'superfast'
            # Get threads automatically? Is it CPU threads?
            # ffmpeg and libx264 automatically multithread without -threads
            # You can set it to threads 0 to explicitly enable "autothreads"
            '-threads:v', '0',
            self.output]
        self.proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        self.proc.poll()

        return self.proc.returncode is None

    def stop(self):
        self.proc.communicate(input=b'q')
        self.proc.wait()
