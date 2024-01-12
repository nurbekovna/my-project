from settings import URL
from pars import get_url_text, get_links, get_data

def main():
    html = get_url_text(url=URL)
    if html is None:
        print("URL isn't working")
        return None

    links = get_links(html=html)
    for link in links:                    

        html = get_url_text(url=link)
        if html is not None:
            try:
                data = get_data(html=html)
                save_to_file(data, "name.txt")
            except AttributeError as ex:
                print(f"{link} - There is a mistake or there isn't enough data {ex}\n\n\n")
            else:
                print("\n\n", data, link, "\n")
                print("Data is ok")
        else:
            print(f"{link} - isn't working")

def save_to_file(data, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("Title: {}\n".format(data["title"]))
        file.write("Price (Soms): {}\n".format(data["price_soms"]))
        file.write("Price (Dollars): {}\n".format(data["price_dollars"]))
        file.write("Description: {}\n".format(data["description"]))
        for key, value in data.items():
            if key not in ["title", "price_soms", "price_dollars", "description"]:
                file.write("{}: {}\n".format(key, value))
        file.write("\n\n")

if __name__ == "__main__":
    main()

