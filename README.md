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
```


## MongoDB Installation Steps for macOS

To set up MongoDB on macOS, follow these steps:

1. **Install Homebrew** (if you haven't already):
   If you don't have Homebrew installed, you can install it by running:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Tap the MongoDB Formulae**:
   Add the official MongoDB tap to Homebrew:
   ```bash
   brew tap mongodb/brew
   ```

5. **Install MongoDB Community Edition**:
   Use the following command to install the MongoDB Community Edition:
   ```bash
   brew install mongodb-community
   ```

7. **Start MongoDB**:
   To start the MongoDB server, run:
   ```bash
   brew services start mongodb/brew/mongodb-community
   ```

9. **Check MongoDB Status**:
   Ensure that MongoDB is running by checking the service list:
   ```bash
   brew services list
   ```
   
   Look for `mongodb-community` and ensure its status is `started`.

11. **Connect to MongoDB** (Optional):
   You can test the connection to MongoDB using the mongo shell:
   ```bash
   mongo
   ```

