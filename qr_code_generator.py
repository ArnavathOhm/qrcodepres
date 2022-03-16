import qrcode

img = qrcode.make("127.0.0.1:5000/?id=gAAAAABiMW6CGGcK8Uap1PVRq3BzmXqQCYqEozC6TFv3CBaMzqMMPQ245vEL01AsQe_3eXqaE_YH4gTjYGwLKB6hA1z42yLHrw==")
img.save('qrtest-id1.jpg')