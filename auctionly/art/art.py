"""module containing art class dictionary of art categories"""
from auctionly import db

art_categories = {
    "Still Life": 0,
    "Landscape": 0,
    "Seascape": 0,
    "Portraiture": 0,
    "Abstract": 0
}


def update_art_category_popularity(category):
    """add 1 onto an art categories popularity each time an art piece of it is added"""
    art_categories[category] = art_categories[category] + 1


class Art(db.Model):
    """Art class implemented to create art objects that can be passed between users"""
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    image = db.Column(db.String(150))
    art_category = db.Column(db.String(150))
    up_for_auction = db.Column(db.String(5))

    def __init__(self, name, owner_id, digital_image_path, description, art_category):
        """creates an art object"""
        self.name = name
        self.owner_id = owner_id
        self.image = digital_image_path
        self.description = description
        self.up_for_auction = "False"
        self.art_category = art_category
        self.art_status = "With owner"
        update_art_category_popularity(art_category)

    def get_name(self):
        """returns name of the art"""
        return self.name

    def set_name(self, new_name):
        """sets name of the art"""
        self.name = new_name

    def get_owner(self):
        """returns the owner of the art"""
        return self.owner_id

    def set_owner(self, new_owner_id):
        """sets the owner of the art which would be updated when art is bought"""
        self.owner_id = new_owner_id

    def get_image(self):
        """returns the image of the art to displayed to other users"""
        return self.image

    def set_image(self, new_digital_image_path):
        """sets a new path for the image of the art"""
        self.image = new_digital_image_path

    def get_description(self):
        """returns a description of the art to be displayed alongside the image"""
        return self.description

    def set_description(self, new_description):
        """updates the description of the art incase the owner would like to change something"""
        self.description = new_description

    def get_up_for_auction(self):
        """returns whether this art piece is up for auction or just on exhibition"""
        return self.up_for_auction

    def set_up_for_auction(self, new_up_for_aunction):
        """updates the up for auction attribute when the owner puts to art up for auction"""
        self.up_for_auction = new_up_for_aunction

    def get_art_category(self):
        """returns the category of the art so it can be displayed accordingly"""
        return self.art_category

    def set_art_category(self, new_art_category):
        """sets a new category for the art"""
        self.art_category = new_art_category

    def get_art_status(self):
        """returns the status of the art i.e is it with the owner, shipping, authentication"""
        return self.art_status

    def set_art_status(self, new_art_status):
        """updates the status of the art as it moves between owners, shipping and authentication"""
        self.art_status = new_art_status

    def get_art_id(self):
        """returns the id of the art object, needed for the shipment service"""
        return self.id

    def set_art_id(self, art_id):
        self.art_id = art_id
