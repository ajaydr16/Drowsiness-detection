from pygame import mixer
mixer.init()
sound = mixer.Sound('notification.wav')
sound.play()
