# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep


url_sbis = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
driver.maximize_window()
try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.get(url_sbis)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    assert login.is_displayed(), 'Поле для ввода логина не отображается'
    login.clear()
    login.send_keys('fizz', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    assert password.is_displayed(), 'Поле для ввода пароля не отображается'
    password.send_keys('Qwerty123', Keys.ENTER)
    sleep(5)

    # Перейти в реестр Контакты
    acc_contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert acc_contacts.is_displayed(), 'Пункт "Контакты" аккордеона не отображается'
    acc_contacts.click()
    sleep(2)
    my_contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    assert my_contacts.is_displayed(), 'Пункт аккордеона Контакты -> Контакты не отображается'
    assert my_contacts.text == 'Контакты', 'Текст вложенного в Контакты подпункта отличается от эталона Контакты'
    my_contacts.click()
    sleep(2)

    # Отправить сообщение самому себе
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert add_btn.is_displayed(), 'Кнопка для создания сообщения не отображается'
    add_btn.click()
    sleep(8)
    search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content [name="ws-input_2023-06-13"]')
    assert search.is_displayed(), 'Поле поиска не отображается'
    search.send_keys('Fizik', Keys.ENTER)
    sleep(2)
    search.send_keys(Keys.ENTER)
    sleep(3)
    text_box = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert text_box.is_displayed(), 'Текстовое поле для ввода сообщение не отображается'
    text_box.send_keys('Але')
    assert text_box.text == 'Але', 'Сообщение в поле отличается от введенного'
    action_chains = ActionChains(driver)
    action_chains.key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()
    sleep(3)

    # Убедиться, что сообщение появилось в реестре
    list_msg = driver.find_elements(By.CSS_SELECTOR, '.controls-MasterDetail_details .controls-ListViewV')
    assert list_msg[0].text.find('Але') != -1, \
        'Сообщение с указанным текстом отсутствует'
    sleep(2)

    # Удалить это сообщение и убедиться, что удалили
    action_chains.context_click(list_msg[0]).perform()
    sleep(3)
    context_menu = driver.find_element(By.CSS_SELECTOR, '.controls-Popup')
    assert context_menu.is_displayed(), 'Контекстное меню не отображается'
    del_msg = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    assert del_msg.is_displayed(), 'В контекстном меню отсутствует опция удаления'
    del_msg.click()
    sleep(3)
    assert list_msg[0].text.find('Але') == -1, 'Сообщение не удалено'


finally:
    driver.quit()
