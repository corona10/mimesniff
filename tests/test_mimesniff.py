import os
import unittest

import mimesniff


LOCAL_DIR = os.path.realpath(os.path.dirname(__file__))
TEXT_DIR = os.path.join(LOCAL_DIR, 'resources', 'text')
IMAGE_DIR = os.path.join(LOCAL_DIR, 'resources', 'image')
FONT_DIR = os.path.join(LOCAL_DIR, 'resources', 'font')
APPLICATION_DIR = os.path.join(LOCAL_DIR, 'resources', 'application')
AUDIO_DIR = os.path.join(LOCAL_DIR, 'resources', 'audio')
VIDEO_DIR = os.path.join(LOCAL_DIR, 'resources', 'video')


class TestMimesniff(unittest.TestCase):

    def check_mime(self, mime_dir, resources):
        for path, expected in resources:
            fpath = os.path.join(mime_dir, path)
            ret = mimesniff.what(fpath)
            self.assertEqual(expected, ret, '{} should be {} but got {}'.format(fpath, expected, ret))
            with open(fpath, 'rb') as fin:
                ret = mimesniff.what(fin)
                self.assertEqual(expected, ret, '{} should be {} but got {}'.format(fpath, expected, ret))

            with open(fpath, 'rb', buffering=0) as fin:
                ret = mimesniff.what(fin)
                self.assertEqual(expected, ret, '{} should be {} but got {}'.format(fpath, expected, ret))

            with open(fpath, 'rb') as fin:
                header = fin.read(512)
                ret = mimesniff.what(header)
                self.assertEqual(expected, ret, '{} should be {} but got {}'.format(fpath, expected, ret))

    def test_text(self):
        resources = [
                ('1.xml', 'text/xml; charset=utf-8'),
                ('sample1.html', 'text/html; charset=utf-8'),
                ('sample2.html', 'text/html; charset=utf-8'),
                ('korean.txt', 'text/plain; charset=utf-8')
        ]
        self.check_mime(TEXT_DIR, resources)

    def test_images(self):
        resources = [
                ('logo.png', 'image/png'),
                ('1.jpg', 'image/jpeg'),
                ('apollonian_gasket.gif', 'image/gif'),
                ('anim.gif', 'image/gif'),
                ('1.webp', 'image/webp')
        ]
        self.check_mime(IMAGE_DIR, resources)

    def test_fonts(self):
        resources = [
                ('sample.otf', 'font/otf'),
                ('sample.woff', 'font/woff'),
                ('sample.woff2', 'font/woff2'),
                ('sample.ttf', 'font/ttf')
        ]
        self.check_mime(FONT_DIR, resources)

    def test_application(self):
        resources = [
                ('change.wasm', 'application/wasm'),
                ('dummy.pdf', 'application/pdf'),
                ('samplec.ps', 'application/postscript'),
                ('Example.json.gz', 'application/x-gzip'),
                ('sample.rar', 'application/x-rar-compressed'),
                ('sample.ZIP', 'application/zip'),
                ('sample.ogg', 'application/ogg'),
        ]
        self.check_mime(APPLICATION_DIR, resources)

    def test_audio(self):
        resources = [
                ('sample.au', 'audio/basic'),
                ('sample.aif', 'audio/aiff'),
                ('sample.mp3', 'audio/mpeg'),
                ('sample.midi', 'audio/midi'),
                ('sample.wav', 'audio/wave')
        ]
        self.check_mime(AUDIO_DIR, resources)

    def test_video(self):
        resources = [
                ('sample.avi', 'video/avi'),
                ('sample.mp4', 'video/mp4')
        ]
        self.check_mime(VIDEO_DIR, resources)

    def test_unsupported_input(self):
        with self.assertRaises(NotImplementedError):
            mimesniff.what(1)

        with self.assertRaises(NotImplementedError):
            mimesniff.what(3.14)


if __name__ == '__main__':
    unittest.main()
