from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page):
    page.goto("http://www.automationpractice.pl/index.php") # passing url
    myurl=page.url
    print("Url of the application:",myurl)
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")# expected url

def test_verifyTitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    mytitle=page.title()
    print("Title of the page:",mytitle)
    expect(page).to_have_title("My Shop")
