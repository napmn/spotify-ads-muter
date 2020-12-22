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
        print('spotify was closed')
        exit()

    duration_sec = track['duration'] / 1000

    if state['state'] == 'playing':
        if track['name'] == 'Advertisement':
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
    else:
        time.sleep(5)


if __name__ == '__main__':
    spotify = Wasp()
    spotify.start_spotify()

    while True:
        check_for_ads(spotify)
