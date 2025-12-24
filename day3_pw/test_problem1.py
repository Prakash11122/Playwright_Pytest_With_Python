import pytest
from playwright.sync_api import Page,expect

def test_task(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # logo (CSS locator)
    page_logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    expect(page_logo).to_be_visible()


    # Products containing "computer" in href attribute
    products = page.locator('h2 > a[href*="computer"]')   # [href*="computer"] mimics XPath contains()
    print("Products count:",products.count())
    expect(products).to_have_count(4)


    print("First Computer product:", products.first.text_content())
    print("Last Computer product:", products.last.text_content())
    print("Nth Computer product:", products.nth(1).text_content())



    # Capture the product titles and print them
    product_titles= products.all_text_contents()
    print("All computer related product names:", product_titles)
    for pt in product_titles:
        print(pt)

    #x-path with starts-with()
    BuildProduct=page.locator("//h2//a[starts-with(text(),'Build')]")
    print("Build product count:",BuildProduct.count())
    expect(BuildProduct).to_have_count(BuildProduct.count())



    #X-Path text() - is presenting inner text of the elements
    registration_link=page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()












