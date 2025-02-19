from hate.configuration.gcloud_syncer import GCloudSync

obj=GCloudSync()

obj.sync_folder_from_gcloud("hate_speech_detection_live","dataset.zip","dataset.zip")