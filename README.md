# Spotify ads muter

Sets Spotify volume to zero when an ad is detected. Brings volume back up after ad is finished.

## Recommended Setup

- Firstly you need to have original [Spotify](https://www.spotify.com/us/download/other/) application installed
- Create python3 virtual environment we will called **venv** for example
(if you select different name you need to change it also in *run.sh* file).
and install necessary packages from *requirements.txt*
- Make run.sh executable: `chmod +x run.sh`
- Create symlink so the script can be used globally:
`ln -s {PROJECT_ABSOLUTE_PATH}/run.sh /usr/local/bin/spotify_ads_muter`

Now you can run spotify with muted ads from terminal or
copy the bundled application from *TODO* folder to your Applications
folder and you can run it as any other application - it will just
execute the script and use original Spotify installation.

### Hint

You can change application icon to Spotify icon or any other icon
you want ([tutorial](https://9to5mac.com/2019/01/17/change-mac-icons/)).
