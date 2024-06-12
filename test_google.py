from selene import browser, be, have


def test_first():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second():
    browser.open('https://google.com')
    (browser.element('[name="q"]').should(be.blank).type('kljsfglkjsfdl;gjl;sdjfgl;kdjsfg;lkjsdfl;gjkdslf;gldfkjgl')
     .press_enter())
    browser.element('.card-section').should(have.text('По запросу kljsfglkjsfdl;gjl;sdjfgl;kdjsfg;lkj'
                                                      'sdfl;gjkdslf;gldfkjgl ничего не найдено.'))
