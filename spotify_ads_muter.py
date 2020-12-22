import math
import time

import pync
from wasp_spotify_bindings.core import Wasp


def check_for_ads(spotify: Wasp):
    try:
        track = spotify.get_track()
        state = spotify.get_state()
    except Exception:
        # spotify was closed
        exit()

    print(track, state)

    if state['state'] != 'playing':
        time.sleep(5)
        return

    duration_sec = track['duration'] / 1000

    if duration_sec < 40 and track['popularity'] == 0:
        # this check handles also video ads
        previous_volume = state['volume']
        mute_duration = math.floor(duration_sec - state['position']) - 0.5
        if mute_duration > 0:
            # weird bug occured that sometimes duration was negative
            pync.notify(
                f'Ad detected, muting spotify for {mute_duration} seconds',
                title='Spotify ads muter'
            )
            spotify.set_volume(0)
            time.sleep(mute_duration)
            spotify.set_volume(previous_volume)
    else:
        time.sleep(1)


if __name__ == '__main__':
    spotify = Wasp()
    spotify.start_spotify()

    while True:
        check_for_ads(spotify)
