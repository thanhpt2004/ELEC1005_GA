import amazon
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/amazon", methods=["POST"])
def amazon_api():
    """
    Retrieves product information from Amazon API based on the provided sections.

    Returns:
        A JSON response containing product names, prices, and ratings for each section.
    """
    amazon_instances = {}
    sections = request.get_json().get("sections", [])
    print(sections)
    result = {}

    for section in sections:
        print(section)
        amazon_instances[section] = amazon.Amazon(section)

    for section, instance in amazon_instances.items():
        urls = instance.define_urls()
        section_links = []
        section_ranks = []
        product_names = []
        product_prices = []
        product_ratings = []
        product_images = []

        for url in urls:
            print(url)
            instance.driver.get(url)
            instance.lazy_loading()
            plinks, pranks = instance.links_ranks()
            section_links.extend(plinks)
            section_ranks.extend(pranks)

        for link in section_links[:5]:
            content = instance.content(link)
            product_names.append(amazon.product_name(content))
            product_prices.append(amazon.product_price(content))
            product_ratings.append(amazon.product_rating(content))
            product_images.append(amazon.product_photo(content))

        result[section] = {
            "product_names": product_names,
            "product_prices": product_prices,
            "product_ratings": product_ratings,
            "product_images": product_images,
        }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5100)
