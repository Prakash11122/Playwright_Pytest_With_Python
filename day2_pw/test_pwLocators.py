import time
import re
from playwright.sync_api import Page, expect

# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()


def test_verify_pwlocators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    # 1) page.get_by_alt_text()
    logo=page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()#full text
    # expect(page.get_by_text("Welcome to")).to_be_visible()#patial text
    # expect(page.get_by_text(re.compile("Welcome to our store"))).to_be_visible()#

    # 3) page.get_by_role()
    page.goto("https://demowebshop.tricentis.com/register")
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading",name="Register")).to_be_visible()

    # 4) page.get_by_label()
    page.get_by_label("First name:").fill("prakash")
    page.get_by_label("Last name:").fill("pradhan")
    page.get_by_label("Email:").fill("prakash@gmail.com")
    page.wait_for_timeout(5000)

    # 5) page.get_by_placeholder()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Enter your full name").fill("Apple MacBook Pro")

    # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    # 7) page.get_by_test_id()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")






