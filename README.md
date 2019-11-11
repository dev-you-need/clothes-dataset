This is a dataset of photos from Aliexpress product reviews.
379186 images, ~30Gb of data.
The dataset is great for example for training a model to find similar images.

First, you have to download images, this requires a script download.py.

Some EDA and photos you can found [here](https://github.com/deerslab/clothes-dataset/blob/master/eda.ipynb) 

##### Data description:

| Column   | Description                                                                                                                |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| id       | Unique identificator of Aliexpress product. Each product can have several colors.                                         |
| category | Clothing category, like skirt                                                                                              |
| color    | Color of current thing. The value does not always make sense - it is such as the seller filled it.                         |
| source   | Two value possible for each product: 'shop' and 'customer'. 'shop' is usually a good photo. Customer photo closer to life. |
| url      | url to image                                                                                                   |

Dataset cleaned semi-manual in a semi-manual way. Some images was annotated good/bad (photo of package for example). Then a model was trained that cleared the rest of the dataset.

If you find bad photos, or you want to add something then feel free to use pull request.
