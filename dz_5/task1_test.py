def test_count_emojis():
    nature_url = 'https://emojipedia.org/nature/'
    music_url = 'https://emojipedia.org/music/'
    science_url = 'https://emojipedia.org/science/'

    nature_count = count_emojis(nature_url)
    music_count = count_emojis(music_url)
    science_count = count_emojis(science_url)

    assert nature_count >= 0, "Количество эмодзи в разделе Nature должно быть неотрицательным"
    assert music_count >= 0, "Количество эмодзи в разделе Music должно быть неотрицательным"
    assert science_count >= 0, "Количество эмодзи в разделе Science должно быть неотрицательным"

    print("Тесты пройдены успешно")

test_count_emojis()
