from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(
    app, uri='mongodb+srv://zacharynguyen:$$92ZacharY@cluster0-ulf1q.mongodb.net/test')


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
