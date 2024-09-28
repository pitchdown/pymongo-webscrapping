# PyMongo Web Scraping Project

This project is a Python-based web scraping and data analysis application that scrapes drink recipes from [Kulinaria.ge](https://kulinaria.ge) and stores the data in MongoDB.
It also performs various analytical operations on the stored data, such as calculating the average number of ingredients, cooking stages, and identifying the most prolific 
author and recipes with the most ingredients.

## Features

- **Web Scraping**: Scrapes drink recipes from multiple categories.
- **Data Storage**: Stores scraped data (ingredients, instructions, authors, images, etc.) into a MongoDB database.
- **Data Analysis**: Analyzes the data to find:
  - The average number of ingredients per recipe.
  - The average number of cooking stages.
  - The recipe with the most ingredients.
  - The author who posted the most recipes.

## Technologies Used

- **Python**: Main programming language.
- **BeautifulSoup**: For web scraping.
- **PyMongo**: For interacting with MongoDB.
- **Threading**: To speed up the scraping process by handling multiple pages concurrently.

## Setup

### Prerequisites

- Python 3.x
- MongoDB
- [MongoDB Compass](https://www.mongodb.com/products/compass) (optional, for GUI)
- Required Python libraries (you can install them using the `requirements.txt` file)

### Install Required Dependencies

You can install the necessary Python libraries using pip:

```bash
pip install -r requirements.txt
