# -*-: coding utf-8 -*-
""" Mopidy skill for Snips. """

from __future__ import unicode_literals

import time

from random import shuffle

from mpd import MPDClient
from .spotify import SpotifyClient

MAX_VOLUME = 70
GAIN = 4


class SnipsMopidy:
    """ Mopidy skill for Snips. """

    def __init__(self, spotify_refresh_token=None, speaker_index=None, locale=None):
        self.client = MPDClient
        self.client.connect('localhost', 6600)
        print(client.mpd_version)
        print(client.find("any", "house"))

        self.previous_volume = self.client.status.get('volume')

    def pause_mopidy(self):
        self.client.pause(1)

    def volume_up(self, level):
        if self.client is None:
            return
        level = int(level) if level is not None else 100
        current_volume = self.client.status.get('volume')
        self.client.setvol(min(
            current_volume + GAIN * level,
            self.max_volume))
        self.client.play()

    def volume_down(self, level):
        if self.client is None:
            return
        level = int(level) if level is not None else 100
        self.client.setvol(GAIN * level)
        self.client.play()
        print(self.client.volume)

    def set_volume(self, volume_value):
        if self.client is None:
            return
        self.client.setvol(volume_value)
        self.client.play()

    def set_to_low_volume(self):
        if self.client is None:
            return
        if self.client.status.get('state') != 'play':
            return None
        self.previous_volume = self.client.status.get('volume')
        self.client.setvol(min(6, self.client.status.get('volume')))
        self.client.play()

    def set_to_previous_volume(self):
        if self.client is None:
            return
        if self.previous_volume is None:
            return None
        self.client.setvol(self.previous_volume)
        if self.client.status.get('state') != 'play':
            self.client.play()

    def stop_mopidy(self):
        if self.client is None:
            return
        self.client.stop()

    def turn_on_radio(self, radio_name):
        if self.client is None:
            return None
        if self.tunein_service is None:
            return None
        res = self.tunein_service.search('stations', term=radio_name)
        if 'mediaMetadata' not in res:
            return "radio not found"
        if isinstance(res['mediaMetadata'], list):
            radio_id = res['mediaMetadata'][0]['id']
        elif isinstance(res['mediaMetadata'], dict):
            radio_id = res['mediaMetadata']['id']
        else:
            raise TypeError("Unknown type for tune in search metadata")
        radio_uri = self.tunein_service.get_media_uri(radio_id)
        try:
            self.client.play_uri(radio_uri.replace('http', 'x-rincon-mp3radio'))
        except Exception:
            # unknown problem playing radio uri...
            return None

    def play_playlist(self, name, _shuffle=False):
        if self.client is None:
            return
        if self.spotify is None:
            return
        tracks = self.spotify.get_tracks_from_playlist(name)
        if tracks is None:
            return None
        self.client.stop()
        self.client.clear()
        if _shuffle:
            shuffle(tracks)
        for track in tracks:
            self.client.add(track['track']['uri'])
        self.client.play()

    def play_artist(self, name):
        if self.client is None:
            return
        if self.spotify is None:
            return
        tracks = self.spotify.get_top_tracks_from_artist(name)
        if tracks is None:
            return None
        self.client.stop()
        self.client.clear()
        for track in tracks:
            self.client.add(track['uri'])
        self.client.play()

    def play_album(self, album, _shuffle=False):
        if self.client is None:
            return
        if self.spotify is None:
            return
        tracks = self.spotify.get_tracks_from_album(album)
        if tracks is None:
            return None
        self.client.stop()
        self.client.clear()
        if _shuffle:
            shuffle(tracks)
        for track in tracks:
            self.client.add(track['uri'])
        self.client.play()

    def play_song(self, name):
        if self.client is None:
            return
        if self.spotify is None:
            return
        track = self.spotify.get_track(name)
        if track is None:
            return None
        self.client.stop()
        self.client.clear()
        self.client.add(track['uri'])
        self.client.play()

    def play_next_item_in_queue(self):
        if self.client is None:
            return
        try:
            self.client.next()
        except Exception:
            print("Failed to play next item, maybe last song?")

    def play_previous_item_in_queue(self):
        if self.client is None:
            return
        try:
            self.client.previous()
        except Exception:
            print("Failed to play previous item, maybe first song?")

    def get_info(self):
        # Get info about currently playing tune
        info = self.client.status.get('song')
        return info['title'], None, None

    def add_song(self):
        # Save song in spotify
        title = self.status.get('song')
        self.spotify.add_song(None, title)

    def play(self):
        # Save song in spotify
        self.client.play()
