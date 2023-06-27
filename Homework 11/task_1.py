# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_url = 'https://sbis.ru/'
tensor_url = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
driver.maximize_window()
try:
    # Перейти на https://sbis.ru/
    driver.get(sbis_url)
    assert driver.current_url == sbis_url, 'Не верно открыт сайт'
    sleep(2)

    # Перейти в раздел "Контакты"
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts_txt = 'Контакты'
    assert contacts.text == contacts_txt, 'Неверный текст у кнопки "Контакты"'
    assert contacts.is_displayed(), 'Кнопка не отображается на странице'
    contacts.click()
    sleep(3)

    # Найти баннер Тензор, кликнуть по нему
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_url, 'Открыт неверный сайт'
    sleep(3)

    # Проверить, что есть блок новости "Сила в людях"
    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert news.text == 'Сила в людях', 'Нет блока новости "Сила в людях"'
    sleep(3)

    # Перейти в этом блоке в "Подробнее" и убедиться, что открывается https://tensor.ru/about
    link = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-link')
    assert link.text == 'Подробнее', 'Неверный текст у кнопки "Подробнее"'
    link.location_once_scrolled_into_view
    sleep(3)
    link.click()
    assert driver.current_url == tensor_about, 'Открыт неверный адрес сайта'
    sleep(3)
finally:
    driver.quit()
