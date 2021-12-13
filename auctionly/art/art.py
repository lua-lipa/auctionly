"""module containing art class"""
from auctionly import db # pylint: disable=E0401

class Art(db.Model):
    """Art class implemented to create art objects that can be passed between users"""
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    image = db.Column(db.String(150))
    art_category = db.Column(db.String(150))
    up_for_auction = db.Column(db.String(5))

    def __init__(self, name, owner_id, digital_image_path, description, art_category): # pylint: disable=R0913
        """creates an art object"""
        self.name = name
        self.owner_id = owner_id
        self.image = digital_image_path
        self.description = description
        self.up_for_auction = "False"
        self.art_category = art_category
        self.art_status = "With owner"

    def get_name(self):
        """returns name of the art"""
        return self.name

    def get_owner(self):
        """returns the owner of the art"""
        return self.owner_id

    def get_image(self):
        """returns the image of the art to displayed to other users"""
        return self.image

    def get_description(self):
        """returns a description of the art to be displayed alongside the image"""
        return self.description

    def get_up_for_auction(self):
        """returns whether this art piece is up for auction or just on exhibition"""
        return self.up_for_auction

    def get_art_category(self):
        """returns the category of the art so it can be displayed accordingly"""
        return self.art_category

    def get_art_status(self):
        """returns the status of the art i.e is it with the owner, shipping, authentication"""
        return self.art_status

    def get_art_id(self):
        """returns the id of the art object, needed for the shipment service"""
        return self.id
