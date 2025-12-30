import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
   # page.locator("#country").select_option("India")#by value 1
    #page.locator("#country").select_option(label="China")  # by label 2

    # selected_value=page.locator("#country").input_value()
    # print("Selected value",selected_value)

    page.locator("#country").select_option(index=3)

    # check number of options in dropdown
    dropdown_options=page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)


    page.wait_for_timeout(5000)



