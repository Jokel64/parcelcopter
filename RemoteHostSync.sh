#rsync -delete -av -h -r -update /parcelcopter pi@10.42.0.153:/repo/parcelcopter.local
rsync -r -a -v -e ssh --delete ../parcelcopter pi@10.42.0.86:/home/pi/repo/remote